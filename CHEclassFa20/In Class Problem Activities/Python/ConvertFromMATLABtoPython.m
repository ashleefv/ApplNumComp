%% ICPL5matlab
% Used for comparison to Python function executing the same method.

%% Example: ax = b 
% Equation 1: $3x_1-0.1x_2-0.2x_3=7.85$. 
% Equation 2: $0.1x_1+7x_2-0.3x_3=-19.3$. 
% Equation 3: $0.3x_1-0.2x_2+10x_3=71.4$.
% Soln x = [3; -2.5; 7]

%% Initialize a matrix and b vector
a = [3, -.1, -.2; 0.1, 7, -0.3; 0.3, -.2, 10];
b = [7.85; -19.3; 71.4];

%% Solve for x
x = gaussElimin(a,b)
% no semicolon so x will print to the command window

%% Define Gaussian elimination function
function [x] = gaussElimin(a,b)
    %% Algorithm
    n = length(b);
    for k = 1:n-1
        for i = k+1:n
            if a(i,k) ~= 0
                lam = a(i,k)/a(k,k);
                a(i,k+1:n) = a(i,k+1:n) - lam*a(k,k+1:n);
                b(i)= b(i) - lam*b(k);
            end
        end
    end
    for k = n:-1:1
        b(k) = (b(k) - a(k,k+1:n)*b(k+1:n))/a(k,k);
    end
    x = b;
end
