tspan = linspace(0,10,101);
C0 = [6.25,0];
k1 = 0.15;
k2 = 0.6;
k3 = 0.1;
k4 = 0.2;
[t,y] = ode45(@(t,C) system_of_ODEs(t,C,k1,k2,k3,k4),tspan,C0);
plot(t,y)