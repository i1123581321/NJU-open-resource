function x = GaussSeidel(A, b, n, x0)
    x = zeros(n, 1);

    iteration_count = 0;
    while iteration_count == 0 || norm(x-x0, inf) > 10^(-4)
        x0 = x;
        for i = 1 : n
            x(i) = b(i)
            for j = 1 : i - 1
                x(i) = x(i) - A(i, j) * x(j);
            end
            for j = i + 1 : n
                x(i) = x(i) - A(i, j) * x(j);
            end
            x(i) = x(i) / A(i, i);
        end
        iteration_count = iteration_count + 1;
    end
    fprintf('Iteration Count: %d\n', iteration_count);
    x = x0;
end