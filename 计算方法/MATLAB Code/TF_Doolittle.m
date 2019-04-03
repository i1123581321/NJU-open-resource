function [L, U] = TF(A, n)
%Triangular Factorization、Triangular decomposition
% LU-decomposition

    L = zeros(n, n);
    U = zeros(n, n);

    for j = 1 : n
        U(1, j) = A(1, j);
    end
    L(1, 1) = 1;    %Don't forget L(m, m)'s initialization
    for i = 2 : n
        L(i, 1) = A(i, 1) / U(1, 1);
    end
    for s = 2 : n
        for j = s : n
            U(s, j) = A(s, j);
            for k = 1 : s - 1
                U(s, j) = U(s, j) - L(s, k) * U(k, j);
            end
        end
        L(s, s) = 1;    %Don't forget L(m, m)'s initialization
        for i = s + 1 : n
            L(i, s) = A(i, s);
            for k = 1 : s - 1
                L(i, s) = L(i, s) - L(i, k) * U(k, s);
            end
            L(i, s) = L(i, s) / U(s, s);
        end
    end
    
end