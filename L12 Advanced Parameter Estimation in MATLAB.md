# **Lesson 12: Advanced Parameter Estimation in MATLAB**
This lesson focuses on parameter estimation with more advanced examples in MATLAB.

## **Activity**
* [Instructions for examples 1 and 2](https://github.com/ashleefv/ApplNumComp/blob/master/Lecture%2014%20Examples.pdf)

### **Example 1**
* This example considers fitting parameters to one differential equation.
```MATLAB
function ODEParamEstimExample1
tdata = [0 0.5 1.0 5.0 30]; % independent variable, x-axis
xdata = [0 0.5 1.2 2.5 2.7]; % dependent variable, y-axis
x0 = 0; % initial condition

% Parameter guesses
b1guess = 1;
b2guess = 1;
parameterguesses = [b1guess, b2guess];

% Estimate parameters b1 & b2
parameters = lsqcurvefit(@(parameterguesses,tdata)model(parameterguesses,tdata,x0),parameterguesses, tdata, xdata)

% Plots
plot(tdata,xdata,'o')
hold on
tforplotting = linspace(tdata(1),tdata(end),101);
xatguesses = model(parameterguesses, tforplotting,x0);
plot(tforplotting,xatguesses)
xatsoln = model(parameters,tforplotting,x0);
plot(tforplotting,xatsoln,'g')
legend('data','x at guesses', 'x at soln parameters')

% Define the function for the model that is fitted to data. 
% This model has output that matches the observed dependent variables. E.g., one could solve multiple ODEs defined by system_of_ODEs, but the output from a subset of ODE solutions might be compared to the data via this function called model. 
function output = model(parameters,t,x0)
    for i = 1:length(t)
        if t(i) == 0 
            tsoln = 0;
            xsoln = x0;
            output(i) = xsoln;
        else
            tspan = [0 t(i)]; 
            [tsoln, xsoln] = ode23s(@(t,x) system_of_ODEs(t,x,parameters), tspan, x0);
            output(i) = xsoln(end);
        end
    end
end

% Define the ODE that is solved inside the model function.
function output = system_of_ODEs(t,x,parameters)
    b1 = parameters(1);
    b2 = parameters(2);
    dxdt = b1-b2*x;
    output = dxdt;
end
end
```
* Output
```MATLAB
parameters =

    1.4309    0.5303
```
![Expected Graph 1](/Lesson_images/Figure1_L12.jpg)
* Solution [.m file](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/ODEParamEstimExample1.m)

### **Example 2**
* This example considers fitting parameters to multiple differential equations.
```MATLAB
function ODEParamEstimExample2
tdata = [0.5 1.0 5.0 20]; % independent variable, x-axis
xdata = [99 98 50 3; 2 4 35 7]; % dependent variables, y-axis
% alternative
% x1 = [99 98 50 3];
% x2 = [2 4 35 7];
% xdata = [x1; x2];

x0 = [100 1]; % initial conditions [ x1(0) x2(0)];

% Parameter guesses
b1guess = 1;
b2guess = 1;
parameterguesses = [b1guess, b2guess];

% Estimate parameters b1 & b2
parameters = lsqcurvefit(@(parameterguesses,tdata)model(parameterguesses,tdata,x0),parameterguesses, tdata, xdata)

tforplotting = linspace(tdata(1),tdata(end),101);
xatguesses = model(parameterguesses, tforplotting,x0);
xatsoln = model(parameters,tforplotting,x0);
% Plots
figure(1)
tiledlayout('flow') 
nexttile
plot(tdata,xdata(1,:),'o')
xlabel('t')
ylabel('x1')
hold on
plot(tforplotting,xatguesses(1,:))
plot(tforplotting,xatsoln(1,:),'g')
legend('data','x1 at guesses', 'x1 at soln parameters')
hold off
nexttile
plot(tdata,xdata(2,:),'o')
xlabel('t')
ylabel('x2')
hold on
plot(tforplotting,xatguesses(2,:))
plot(tforplotting,xatsoln(2,:),'g')
legend('data','x2 at guesses', 'x2 at soln parameters')
hold off

% Define the function for the model that is fitted to data. 
% This model has output that matches the observed dependent variables. E.g., one could solve multiple ODEs defined by system_of_ODEs, but the output from a subset of ODE solutions might be compared to the data via this function called model. 
function output = model(parameters,t,x0)
    for i = 1:length(t)
        if t(i) == 0 
            tsoln = 0;
            xsoln = x0;
            output(i,:) = ysoln;
        else
            tspan = [0 t(i)]; 
            [tsoln, xsoln] = ode23s(@(t,x) system_of_ODEs(t,x,parameters), tspan, x0);
            output(i,:) = xsoln(end,:);
        end
    end
    output = output';
end

% Define the ODEs that are solved inside the model function.
function output = system_of_ODEs(t,x,parameters)
    b1 = parameters(1);
    b2 = parameters(2);
    x1 = x(1);
    x2 = x(2);
    dxdt(1) = -b1*x1*x2;
    dxdt(2) = b1*x1*x2-b2*x2;
    output = dxdt';
end
end
```
* Output
```MATLAB
parameters =

    0.0109    0.2100
```
![Expected Graph 2](/Lesson_images/Figure2_L12.jpg)
* Solution [.m file](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/ODEParamEstimExample2.m)

## Homework Exercise
* Parameter estimation of ODE models for chemical kinetics
  - [Problem statement](https://github.com/ashleefv/ChESS2022/blob/master/5%20Interactive%20Coding%20Templates/J5_ParEstKinetics.ipynb)
  - [MATLAB Live Script problem](https://github.com/ashleefv/ChESS2022/blob/master/5%20Interactive%20Coding%20Templates/M5_ParEstKinetics.mlx)
  - [MATLAB Live Script solution](https://github.com/ashleefv/ChESS2022/blob/master/5%20Interactive%20Coding%20Templates/M5_ParEstKinetics_solution.mlx)

## **Reference for Further Exploration**
* Weighted sum of squared residuals in parameter estimation [theory and example](https://github.com/ashleefv/ApplNumComp/blob/master/WSSR.pdf)

## **Previous Lesson**
 * [L11 Parameter Estimation in MATLAB](/L11%20Parameter%20Estimation%20in%20MATLAB.md)

## **Next Lesson**
 * [L13 Parameter Estimation in Python](/L13%20Parameter%20Estimation%20in%20Python.md)
