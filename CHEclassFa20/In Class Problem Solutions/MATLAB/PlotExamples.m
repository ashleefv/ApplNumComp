x = [1, 2, 3, 4];
y = [1, 4, 9, 16];
plot(x,y)
xlabel('some numbers')
ylabel('x^2')

hold on
plot(y) % overlaps original plot with 2nd curve. red/orange color
hold off
plot(y) % replaces any plot with blue single curve

% set x- and y-axis limits
axis([0, 6, 0,20])%[xmin, xmax, ymin, ymax]

xmin = 1.0;
xmax = 5.0;
ymin = 0;
ymax = 20;
axis([xmin, xmax, ymin, ymax])



% symbols, colors, and linestyles
plot(x,y,'ro--','MarkerSize',16,'LineWidth',1.25)
plot(x,y,'ro')
figure(2)
errorbar(y,.1*y)
figure(3)
plot(x,y,'DisplayName',['final y value' num2str(y(end))])
legend('-DynamicLegend')

figure(1)
subplot(221)
plot(x,y,'ro--','MarkerSize',16,'LineWidth',1.25)
subplot(222)
plot(x,y,'o','MarkerFaceColor',[255, 124, 25]/256)
subplot(223)
errorbar(y,.1*y)
subplot(224)
errorbar(y,.1*y,'b')

figure(2)
tiledlayout('flow') %tiledlayout(2,2)
nexttile
plot(x,y,'ro--','MarkerSize',16,'LineWidth',1.25)
nexttile
plot(x,y,'o','MarkerFaceColor',[255, 124, 25]/256)
nexttile
errorbar(y,.1*y)
nexttile
errorbar(y,.1*y,'b')
help plot

% evenly spaced sampled time at specied intervals
time_inc = 0.2; % units of s
time_start = 0; % s
time_end = 5; %s
time = time_start:time_inc:time_end;

% compare to linspace
time = linspace(0,5,26); %start, end, number of points
t = time;

%% ICP
% red dashes for t vs. t, blue squares for t^2 vs. t, and green triangles
% for t^3 vs. t

figure(4)
plot(t,t,'r--') % 'DisplayName','t vs. t'
hold on
plot(t,t.^2,'bs')
plot(t,t.^3,'g^')
hold off
legend('t vs. t','t^2 vs. t','t^3 vs. t','location','best')
