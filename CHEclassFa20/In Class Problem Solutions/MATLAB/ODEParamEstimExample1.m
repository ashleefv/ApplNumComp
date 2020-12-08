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