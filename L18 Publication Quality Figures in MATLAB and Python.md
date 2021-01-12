# **Lesson 18: Publication Quality Figures**
This lesson focuses on developing publication quality images in MATLAB and Python and exporting them for use in other software.

### **Introductory Videos**
 * None for this lesson
 #### **Comprehension Check**
  * None for this lesson
### **export_fig for MATLAB**
* [export_fig](https://github.com/altmany/export_fig) introduction to export_fig, a tool for exporting figures from MATLAB into publication quality figures with a simple, online accessible script
* [Sample publication with images](/Ford%20Versypt%2C%20Harrell%2C%20and%20McPeak%2C%20Computers%20and%20Chem%20Eng%202017.pdf)
 * This is a paper with a number of images produced by use of export fig, for good visual presentation of the preserving power of this tool
* [Sample code](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/export_fig_example.m) for using export fig
 * Below is a sample code to create a figure and can then be used for export fig.
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
### **mpltex for Python**
  * Program for producing publication quality images using matplotlib from Python
  * [mpltex](https://github.com/liuyxpp/mpltex)
### **Markdown Examples**
* [ACEInhib](https://github.com/ashleefv/ACEInhibPKPD) Example of Markdown and simulations
  * This is a model for a drug delivery simulation, demonstrating the power of an ACE inhibitor
* [BeeNestABM](https://github.com/ashleefv/BeeNestABM) Example of markdown and agent based model
 * This model was actually designed within GUIDE, and is a good example of how powerful GUIDE can be given sufficient data and some mathematical interpretation
* Journal of Open Source Software information- how to publish, access open source code
  * These are examples of markdown, and can be used as a good example of the power of the language.
### **Additional Resources**
* None for this lesson

### **Previous Lesson**
 * [L17 Sensitivity Analysis](/L17%20Sensitivity%20Analysis.md)
### **Next Lesson**
 * [L19 Python GUIs](/L19%20GUIs%20in%20Python.md)
