%% MATLABBasics.m
%   make a very simple plot of one function.
function MATLABBasics(varargin)

if nargin < 1
    xmin=0;
else 
    xmin = varargin{1};
end

if nargin < 2
    xmax=3; 
else 
    xmax = varargin{2};
end

if nargin < 3
    Nx=200;
else 
    Nx = varargin{3};
end

%% Alternative solution 
% Uses user-defined input if 3 inputs are provided
% Uses defaults otherwise

% if nargin < 3
%     % default values
%     xmin = 0; 
%     xmax = 3;
%     Nx = 200;
% else
%     xmin = varargin{1};
%     xmax = varargin{2};
%     Nx = varargin{3};
% end

%% set independent variable
x=linspace(xmin,xmax,Nx);

%% calculate function values
f = 3*x.^2;
g=x;
%% plot results
plot(x,f)
hold on
plot(x,g)
hold off
xlabel('x')
ylabel('functions of x')
legend('f(x) = 3x^2','g(x) = x','Location','Best');
title('A simple plot')
grid on
end