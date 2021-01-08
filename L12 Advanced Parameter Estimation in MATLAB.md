# **Lesson 12: Advanced Parameter Estimation in MATLAB**
This lesson focuses on parameter estimation with more advanced examples in MATLAB.

### **Introductory videos**
None for this lesson

#### **Comprehension Check**
    * None for this lesson
### **Example MATLAB Plotting**
* Working examples together
* [Prompts for practice](https://github.com/ashleefv/ApplNumComp/blob/master/Lecture%2014%20Examples.pdf)

### **Example 1**
* [Sample code](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/ODEParamEstimExample1.m)
* Note the 2 separate parameter estimatation method options 
* Also note the separate graphs and loops that can modify the logic flow of the code.
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
%parameters = lsqcurvefit(@(parameterguesses,tdata) model (parameterguesses,tdata) ,parameterguesses, tdata, xdata)
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

function output = system_of_ODEs(t,x,parameters)
    b1 = parameters(1);
    b2 = parameters(2);
    dxdt = b1-b2*x;
    output = dxdt;
end
end
```

### **Example 2**
* [Sample Code](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/ODEParamEstimExample2.m)
* Note the commented out second option for describing a datast and parameters coding.
* Also note the plotting tiles
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
%parameters = lsqcurvefit(@(parameterguesses,tdata) model (parameterguesses,tdata) ,parameterguesses, tdata, xdata)
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
```
* Note the separate outputs, the flipping of the matrix of solutions
```MATLAB
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
### **Additional Example**
* [Weighted sum of squared residuals in parameter estimation](https://github.com/ashleefv/ApplNumComp/blob/master/WSSR.pdf)
### **Additional Resources**
* None for this lesson

### **Previous Lesson**
 * [L11 Parameter Estimation for MATLAB](/L11%20Parameter%20Estimation%20for%20MATLAB.md)
### **Next Lesson**
 * [L13 Python Parameter Estimation](/L13%20Python%20Parameter%20Estimation.md)
