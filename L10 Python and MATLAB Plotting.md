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
plt.show() #somewhat like hold on in matlab
```
![Expected Graph 1](/Lesson_images/Figure1_L10.png)
* Continue from the Python code above to add two more plots
```Python
plt.plot(t,t**2,'bs')
plt.plot(t,t**3,'g^')

#plt.axis([0, 20, 0, 30])
plt.savefig('exampleplot.png')
plt.show()
```
![Expected Graph 2](/Lesson_images/Figure2_L10.png)
* Continue from the Python code above to tile subplots on the same figure
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
* Work through several plotting examples sequentially, increasing complexity with each graph, debugging.
* These plots exhibit the ability of MATLAB to run functions, as well as different methods of plotting: delineating the dataset, noting a function in terms of another variable, and manually typing the equations in the plot line
* Additionally, figure 3 demonstrates some of the options a user can specify within the 
```MATLAB
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
```
![Expected Graph 1](/Lesson_images/figure1_L10.jpg)
![Expected Graph 2](/Lesson_images/figure2_L10.jpg)
![Expected Graph 3](/Lesson_images/Figure3_L10.jpg)
* The following figures demonstrate how to run loops, only plot portions of those loops,how to plot multiple plots in the same window, and how to plot errorbars
```MATLAB
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
```
![Expected Graph 4](/Lesson_images/Figure4_L10.jpg)
![Expected Graph 5](/Lesson_images/Figure5_L10.jpg)
* Another example of MATLAB plotting functionalities
[Raw MATLAB code](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/PlotExamples.m)
```MATLAB
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
```
* Demonstrating tile layouts with the following figures, as well as demonstrating that each of separate tiles is unique figure.
* Also demonstrating the ability to force intervals on graphs.
```MATLAB
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

```
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
