# **Lesson 18: Publication Quality Figures**
This lesson focuses on developing publication quality images in MATLAB and Python.

## **MATLAB**
* [export_fig](https://github.com/altmany/export_fig) is highly recommended for figures from MATLAB into publication quality figures with a simple, online accessible script
* The documentation details the commands in a clear way
* [Sample publication using export_fig](/Ford%20Versypt%2C%20Harrell%2C%20and%20McPeak%2C%20Computers%20and%20Chem%20Eng%202017.pdf)
* Sample code snippet for using export_fig after the package has been downloaded and unzipped in a directory in the MATLAB path
```MATLAB
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
## **Python**
* [mpltex](https://github.com/liuyxpp/mpltex) is recommended producing publication quality images using matplotlib in Python
* The documentation provides nice examples for use

## **Markdown Examples**
* Several of the Ford Versypt Lab github repositories have README.md files that demonstrate various Markdown features
   * [ACEInhib](https://github.com/ashleefv/ACEInhibPKPD) 
   * [BeeNestABM](https://github.com/ashleefv/BeeNestABM)
   * The ApplNumComp repository also uses Markdown throughout
* [Journal of Open Source Software](https://joss.theoj.org/) uses Markdown for paper.md files for the journal submission process

## **Previous Lesson**
 * [L17 Sensitivity Analysis](/L17%20Sensitivity%20Analysis.md)

## **Next Lesson**
 * [L19 GUIs in Python](/L19%20GUIs%20in%20Python.md)
