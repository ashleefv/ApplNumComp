x = 1:2:101;
y = 2*x+5;
plot(x,y,'Linewidth',5)
xlabel('x','FontName','Arial','FontSize',20)
ylabel('y','FontName','Arial','FontSize',20)
legend('y','Location','Best')

get(gca);set(gca,'FontSize',20,'FontName','Arial');
set(gcf, 'Color', 'w','Units', 'inches', 'Position', [0 0 3.5 2.5]);
export_fig('test','-r1000',  '-q101', '-painters', '-eps', '-png', '-tiff');