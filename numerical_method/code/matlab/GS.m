function x = GS(A, b, n, x0)
    x = zeros(n, 1);

    M = tril(A);
    N = diag(diag(A)) - triu(A);
    B = inv(M) * N;
    f = inv(M) * b;
    disp(B);
    disp(f);

    iteration_count = 0;
    while iteration_count == 0 || norm(x-x0, inf) > 10^(-4)
        x0 = x;
        x = B * x + f;
        iteration_count = iteration_count + 1;
    end
    fprintf('Iteration Count: %d\n', iteration_count);
    x = x0;
end