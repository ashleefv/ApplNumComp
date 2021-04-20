# **Lesson 10: Python and MATLAB Plotting**

This lesson introduces 2D and 3D visualization in Python and MATLAB.

## **Introductory videos**
 * [Plotting examples from Dr. Ford Versypt's research](https://www.youtube.com/watch?v=Pykrn0DpesA&feature=emb_title&ab_channel=AshleeN.FordVersypt)
  
 [![](http://img.youtube.com/vi/Pykrn0DpesA/0.jpg)](http://www.youtube.com/watch?v=Pykrn0DpesA "")
* Dr. Ford Versypt's [Google Scholar profile](https://scholar.google.com/citations?user=Xaj6qbIAAAAJ) for the work shown in the video

## **Reflection Questions**
* Find an example of common type of 2D or 3D visualization from your research or science, engineering, or mathematics coursework. 
* Browse through the MATLAB and Python example galleries. Which type, if any, of the examples are similar to visualization example you found for question 1?
    * [Python gallery](https://matplotlib.org/stable/gallery/index.html)
    * [MATLAB gallery](https://www.mathworks.com/help/matlab/examples.html?category=graphics&s_tid=CRUX_topnav)


## **Python Plotting**
* Python uses 
```Python
import matplotlib.pyplot as plt
```
to access style functions similar to Matlab

* Python example code for plotting that demonstrates Python's ability to subplot/create tiles for multiple graphs in a single window
```Python
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,101,1)
plt.plot(t,t,'r--')
plt.ylabel('t')
plt.plot(t,t**2,'bs')
plt.plot(t,t**3,'g^')

plt.savefig('exampleplot.png')
plt.show()
```
![Expected Graph 2](/Lesson_images/Figure2_L10.png)
* Add tile subplots on the same figure
```Python
fig = plt.figure(figsize=(10.0,3.0))

axes1 = fig.add_subplot(1,3,1)
axes2 = fig.add_subplot(1,3,2)
axes3 = fig.add_subplot(1,3,3)

axes1.set_ylabel('t')
axes1.plot(t,t,'r--')
axes2.set_ylabel('t^2')
axes2.plot(t,t**2,'bs')
axes3.set_ylabel('t^3')
axes3.plot(t,t**3,'g^')

fig.tight_layout()
plt.show()
```
![Expected Graph 3](/Lesson_images/Figure3_L10.png)
* Solution [.py file](/CHEclassFa20/In%20Class%20Problem%20Solutions/Python/PlotExamples.py)

## **MATLAB Plotting**
* Note: to plot Y vs. X in MATLAB, use plot(x,y)
* Define x and y vectors, customize the line color, style, and symbol, and format x- and y-axis labels 
```MATLAB
close all
clear all
x = [1, 2, 3, 4];
y = [1, 4, 9, 16];
% y = x.^2;
figure(1)
plot(x,y,'o-','color',[142, 0, 178]/255)
xlabel('\beta x')
ylabel('x^2')
```
![Expected Graph 1](/Lesson_images/figure1_L10.jpg)
* Add another curve and adjust the axis limits
```MATLAB
figure(2)
plot(x,y,'o-')
hold on
plot(x,2*y,'x-.','color',[0.4940, 0.1840, 0.5560],'linewidth',5,'markersize',12)
hold off
% set x- and y-axis limits
axis([1.5 3.5, 0, 100]) % [ xmin, xmax, ymin, ymax]
```
![Expected Graph 2](/Lesson_images/figure2_L10.jpg)
* Add a for loop to plot multiple curves and to set the legend entries dynamically
```MATLAB
figure(3)
Y = [y;2*y;3*y;4*y];
hold on
for i = 1:4
    plot(x,Y(i,:),'o','MarkerSize',15,'DisplayName',['final value = ' num2str(Y(i,end))])%,'MarkerFaceColor','g')
end
hold off
%legend('y','y^2','y^3','y^4')
legend('-DynamicLegend')
```
![Expected Graph 3](/Lesson_images/Figure3_L10.jpg)
* Add multiple plots on the same figure using hold on and hold off
```MATLAB
figure(4)
hold on
plot(x,Y(1,:),'o')
plot(x,Y(4,:),'x')
hold off
```
![Expected Graph 4](/Lesson_images/Figure4_L10.jpg)
```MATLAB
figure(5)
hold on
Y1 = Y(1,:);
Y4 = Y(4,:);
plot(x,Y1)
plot(x,Y4)
hold off
```
![Expected Graph 5](/Lesson_images/Figure5_L10.jpg)
* Display multiple subplots on one figure using tiles
```MATLAB
figure(6)
Y = [y;2*y;3*y;4*y];

tiledlayout('flow')
for i = 1:2
    nexttile
    plot(x,Y(i,:),'o','MarkerSize',15,'DisplayName',['final value = ' num2str(Y(i,end))])
    legend('-DynamicLegend')
end
```
![Expected Graph 6](/Lesson_images/Figure6_L10.jpg)
* Display error bars on a plot
```MATLAB
Yerror = .1*Y;
figure(7)
errorbar(x,Y(1,:),Yerror(1,:))
```
![Expected Graph 7](/Lesson_images/Figure7_L10.jpg)
* Related MATLAB plotting sample [.m file](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/PlotExamples.m)

## **References for Further Exploration**
* [MATLAB graphics documentation](https://www.mathworks.com/help/matlab/graphics.html)
* [Python graphics documentation](https://matplotlib.org/)
* [MATLAB line specifications](https://www.mathworks.com/help/matlab/ref/linespec.html)
* [MATLAB default color order](http://math.loyola.edu/~loberbro/matlab/html/colorsInMatlab.html)
* [Python gallery](https://matplotlib.org/stable/gallery/index.html)
* [MATLAB gallery](https://www.mathworks.com/help/matlab/examples.html?category=graphics&s_tid=CRUX_topnav)

## **Previous Lesson**
 * [L09 MATLAB to Python Conversion](/L09%20MATLAB%20to%20Python%20Conversion.md)

## **Next Lesson**
 * [L11 Parameter Estimation in MATLAB](/L11%20Parameter%20Estimation%20in%20MATLAB.md)
