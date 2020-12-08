%% Example: Ax = B 
% Equation 1: $3x_1-0.1x_2-0.2x_3=7.85$. 
% Equation 2: $0.1x_1+7x_2-0.3x_3=-19.3$. 
% Equation 3: $0.3x_1-0.2x_2+10x_3=71.4$.
% Soln x = [3; -2.5; 7]

%% Initialize A matrix and B column vector
A = [3, -.1, -.2; 0.1, 7, -0.3; 0.3, -.2, 10];
B = [7.85; -19.3; 71.4];

x = A\B