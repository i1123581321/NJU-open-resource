function x = Guass(A, b, n)

    for k = 1 : n
        
        previous_a = A(k, k);
        for j = k : n
            A(k, j) = A(k, j) / previous_a;
        end
        b(k) = b(k) / previous_a;
        disp(A);
        disp(b);

        for i = k + 1 : n

            l = A(i, k);  % coefficient

            
            for j = k : n
                A(i, j) = A(i, j) - l * A(k, j);
            end
            disp(A);

            b(i) = b(i) - l * b(k);
            disp(b);
        end
    end

    x(n) = b(n) / A(n, n);
    for i = n - 1 : -1 : 1
        x(i) = b(i);
        for j = i + 1 : n
            x(i) = x(i) - A(i, j) * x(j);
        end
        x(i) = x(i) / A(i, i);
    end
    
end