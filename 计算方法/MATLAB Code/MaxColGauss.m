function x = MaxColGauss(A, b, n)
%Elimination with Maximal Column Pivoting

% STEP 1
    for k = 1 : n - 1
% STEP 2
        %find maximal column
        max = abs(A(k, k));
        i = k;
        for j = k + 1 : n
            if abs(A(j, k)) > max
                max = abs(A(j, k));
                i = j;
            end
        end
        fprintf('The maximal column is %d\n', i);
% STEP 3
        if max == 0
            fprintf('No unique solution');
        end
% STEP 4
        if i ~= k
            %swap(A(k, :), A(i, :))
            for j = k : n
                    tmp = A(k, j);
                    A(k, j) = A(i, j);
                    A(i, j) = tmp;
            end
            %swap(b(k), b(i))
            tmp = b(k);
            b(k) = b(i);
            b(i) = tmp;
        end
        %eliminate terms
% STEP 5    这边可以把LU分解的L得出来，之后试试输出
        for i = k + 1 : n
            % l(i, k) = A(i, k) / A(k, k);
            l = A(i, k) / A(k, k);
            for j = k + 1 : n
                % A(i, k) = A(i, k) - l(i, k) * A(k, j);
                A(i, j) = A(i, j) - l * A(k, j);
            end
            % b(i) = b(i) - l(i, k) * b(k);
            b(i) = b(i) - l * b(k);
        end
    end
% STEP 6
    if (A(n, n) == 0)
        fprintf('No unique solution');
    end
% STEP 7
    x(n) = b(n) / A(n, n);
    for i = n - 1 : -1 : 1
        x(i) = b(i);
        for j = i + 1 : n
            x(i) = x(i) - A(i, j) * x(j);
        end
        x(i) = x(i) / A(i, i);
    end
end

