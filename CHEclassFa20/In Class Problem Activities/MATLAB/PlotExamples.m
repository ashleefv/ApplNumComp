%close all
clear all
x = [1, 2, 3, 4];
y = [1, 4, 9, 16];
% y = x.^2;
figure(1)
plot(x,y,'o-','color',[142, 0, 178]/255)
xlabel('\beta x')
ylabel('x^2')
figure(2)
plot(x,y,'o-')
hold on
plot(x,2*y,'x-.','color',[0.4940, 0.1840, 0.5560],'linewidth',5,'markersize',12)
hold off
% set x- and y-axis limits
axis([1.5 3.5, 0, 100]) % [ xmin, xmax, ymin, ymax]

figure(3)
Y = [y;2*y;3*y;4*y];
hold on
for i = 1:4
    plot(x,Y(i,:),'o','MarkerSize',15,'DisplayName',['final value' num2str(Y(i,end))])%,'MarkerFaceColor','g')
end
hold off
%legend('y','y^2','y^3','y^4')
legend('-DynamicLegend')

figure(4)
hold on
plot(x,Y(1,:),'o')
plot(x,Y(4,:),'x')
hold off
figure(5)
hold on
Y1 = Y(1,:);
Y4 = Y(4,:);
plot(x,Y1)
plot(x,Y4)
hold off

figure(6)
Y = [y;2*y;3*y;4*y];
Yerror = .1*Y;
tiledlayout('flow')
for i = 1:2
    nexttile
    plot(x,Y(i,:),'o','MarkerSize',15,'DisplayName',['final value' num2str(Y(i,end))])%,'MarkerFaceColor','g')
    legend('-DynamicLegend')
end

figure(7)
errorbar(x,Y(1,:),Yerror(1,:))