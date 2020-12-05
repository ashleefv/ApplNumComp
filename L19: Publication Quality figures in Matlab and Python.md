# **Publication Quality Images**
This lesson focuses on developing publication quality images in Matlab and Python, and exporting them for use.

## **Introductory videos**
 * None for this lesson
 
### **Export Fig for Matlab publications**
* [Export Fig](https://github.com/altmany/export_fig) introduction
* [Sample Publication with images](https://github.com/ashleefv/ApplNumComp/blob/master/Ford%20Versypt%2C%20Harrell%2C%20and%20McPeak%2C%20Computers%20and%20Chem%20Eng%202017.pdf)
* Sample code for using export fig
```matlab
x = 1:2:101;
y = 2*x+5;
plot(x,y,'Linewidth',5)
xlabel('x','FontName','Arial','FontSize',20)
ylabel('y','FontName','Arial','FontSize',20)
legend('y','Location','Best')

get(gca);set(gca,'FontSize',20,'FontName','Arial');
set(gcf, 'Color', 'w','Units', 'inches', 'Position', [0 0 3.5 2.5]);
export_fig('test','-r1000',  '-q101', '-painters', '-eps', '-png', '-tiff');
```
### **Mpltex for Python publications**
  * Program for producing publication quality images using matplotlib from Python
  * [mpltex](https://github.com/liuyxpp/mpltex)
### **Markdown Examples**
* [ACEInhib](https://github.com/ashleefv/ACEInhibPKPD) Example of markdown and simulations
* [BeeNestABM](https://github.com/ashleefv/BeeNestABM) Example of markdown and agent based model
* Journal of Open Source Software information- how to publish, access open source code

### **Additional Resources**
* None for this lesson
