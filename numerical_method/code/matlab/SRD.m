% unfinished

function L = SRD(A, n)
    % square root decomposition of positive definite matrix
    L = zeros(n, n);
    for j = 1 : n
        L(j, j) = A(j, j);
        for k = 1 : j - 1
            L(j, j) = L(j, j) - L(j, k);
        end
        L(j, j) = sqrt()
    end
end