function x = JacobiRecursive(A, b, n, x0)
    x = zeros(n, 1);
    D = zeros(n, n);
    L = zeros(n, n);
    U = zeros(n, n);
    f = zeros(n, 1);
    iteration_count = 1;
    % get Diag (also work with "diag(diag(A))")
    for i = 1 : n
        D(i, i) = A(i, i);
    end

    % get Lower (also work with "D - tril(A)")
    for i = 2 : n
        for j = 1 : i - 1
            L(i, j) = -A(i, j);
        end
    end

    % get Upper (also work with "D - triu(A)")
    for i = 1 : n - 1
        for j = i + 1 : n
            U(i, j) = -A(i, j);
        end
    end

    B = inv(D) * (L + U);
    f = inv(D) * b;

    if vrho(B) > 1
        error('Not convergent\n');
    end
    x = B * x0 + f;
    while norm(x-x0, inf) > 10^(-4)
        x0 = x;
        x = B * x0 + f;
        iteration_count = iteration_count + 1;
    end
    fprintf('Iteration Count: %d\n', iteration_count);
end

% Test data
% A = [8 -3 2; 4 11 -1; 6 3 12]; b = [20; 33; 36];
% ans = [3, 2, 1];