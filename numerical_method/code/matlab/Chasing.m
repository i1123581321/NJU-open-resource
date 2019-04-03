function x = Chasing(A, f, n)

    U_beta = zeros(n, n);

    % calculate {beta_i}
    U_beta(1, 2) = A(1, 2) / A(1, 1); % beta1 = b1 / c1
    for i = 2 : n - 1
        U_beta(i, i + 1) = A(i, i + 1) / (A(i, i) - A(i, i - 1) * U_beta(i - 1, i));
    end
    for i = 1 : n
        U_beta(i, i) = 1;
    end
    fprintf('U_beta:\n');
    disp(U_beta)

    % solve Ly=f
    y = zeros(n, 1);
    y(1) = f(1) / A(1, 1);
    for i = 2 : n
        y(i) = (f(i) - A(i, i - 1) * y(i - 1)) / (A(i, i) - A(i, i - 1) * U_beta(i - 1, i));
    end
    fprintf('y:\n');
    disp(y);

    % solve Ux=y
    x = zeros(n, 1);
    x(n) = y(n);
    for i = n - 1 : -1 : 1
        x(i) = y(i) - U_beta(i, i + 1) * x(i + 1);
    end

end