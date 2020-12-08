%% Intro Demo
x = linspace(0,10,101);
newoutput = f(x)
plot(x,newoutput)
xlabel('position (m)','FontSize',12,'Color',[250,100,000]/256)
ylabel({'velocity' ; '(m/s)'} )

y = 0:100;
secondoutput  = f(y)
figure(2)
plot(y,secondoutput)
function newoutput = f(x)
newoutput = 4*x.^2+5;
end