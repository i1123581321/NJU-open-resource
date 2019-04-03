function x = SOF(A, b, n, x0, omega)
    x = zeros(n, 1);
    iteration_count = 0;
    while iteration_count == 0 || norm(x-x0, inf) > 10^(-6)
        x0 = x;
        for i = 1 : n
            x(i) = b(i)
            for j = 1 : i - 1
                x(i) = x(i) - A(i, j) * x(j);
            end
            % Be careful while handling x_i^(k)
            % since the value in x(i) has already changed.
            x(i) = x(i) - A(i, i) * x0(i);
            for j = i + 1 : n
                x(i) = x(i) - A(i, j) * x(j);
            end
            x(i) = x(i) * omega / A(i, i) + x0(i);
        end
        iteration_count = iteration_count + 1;
    end
    fprintf('Iteration Count: %d\n', iteration_count);
    x = x0;
end
% Test Case
% A = [-4 1 1 1; 1 -4 1 1; 1 1 -4 1; 1 1 1 -4]; b = [1; 1; 1; 1];
