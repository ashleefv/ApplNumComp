%% Parameter Estimation Example
% ParamEstimExample.m

% read in the xdata, ydata
ParamEstimData

% define initial parameters guesses
a0 = 1;
b0 = -1.6;
c0 = -0.75;
d0 = -2.7;

% guesses for where to start parameter estimation
parameters0 = [a0, b0, c0, d0]; 

%parameters = lsqnonlin(@(sumExponentials-ydata).^2,parameters0); % in MATLAB documentation x is the parameters, not the xaxis or xdata
[parameters, resnorm, residuals, exitflag, output] = lsqcurvefit(@sumExponentials, parameters0,xdata,ydata); % in MATLAB documentation x is the parameters, not the xaxis or xdata
% plot the data
figure(1)
plot(xdata,ydata,'o')

xforplotting = linspace(xdata(1),xdata(end),100);
yforplotting = sumExponentials(parameters,xforplotting);
hold on
plot(xforplotting,yforplotting)

yAtInitialGuess = sumExponentials(2*parameters,xforplotting);
plot(xforplotting,yAtInitialGuess,'g')
hold off
legend('data', 'model with fitted parameters','initial guesses*2 in the model')

parameters
resnorm
figure(2)
plot(xdata,residuals)

% defining the function to fit
function output = sumExponentials(parameters,x)
    a = parameters(1);
    b = parameters(2);
    c = parameters(3);
    d = parameters(4);
    
    y = a*exp(b*x)+c*exp(d*x);
    output = y;
end