# **LaTeX Tutorial**

This lecture focuses on advanced LaTeX topics, specifically article writing, dissertaion options, and formatting. This is some of the most frequently requested inofrmation
and has the potential to be the most immediately useful.

### **Advantages of LaTeX for Technical or Long documents**
* Integration of templates from publishers, univeristies, conferences
* File size streamlining
* Easier integration with figure and equation numbering, cross referencing, table of contents, and modularizing chapters to include or exclude

* Sample Templates
  * [PLOS One Template Example](https://www.youtube.com/watch?v=2IpdTQhj6cg&ab_channel=AshleeN.FordVersypt)

  * [Elsevier Template Example](https://www.youtube.com/watch?v=vO9O7Nuk0XM&ab_channel=AshleeN.FordVersypt)
  
  * [OSU Thesis Template Example](https://www.youtube.com/watch?v=gHp1IWxEink&ab_channel=AshleeN.FordVersypt)
  
  * [UIUC Thesis Template](https://github.com/bardsoftware/template-thes-uiuc)

  * [OSU Thesis Template](https://github.com/mitchute/OSULaTeXTheisTemplate)
 
### **Try this Activity**
* [Coding activity](https://github.com/ashleefv/ApplNumComp/blob/master/LaTeX%20basics%20activity.pdf)
  
#### Activity
* Partner up, one person is the coder (actually doing the coding), the other is the navigator (watches the screen, reads values from the assignment, gives suggestions, and proofreads)
* Discuss
* Switch roles, stay with the same partner,try part 2 of the activity
* Discussion

### **Activity Example Solution**
* [Sample Solution to the activity](https://www.youtube.com/watch?v=KSrDadBdp7w&feature=emb_title&ab_channel=AshleeN.FordVersypt)

### **Tutorial and Walkthrough**
Demonstrating power of LaTeX

* Demonstrating how to create a figure, after integrating the correct packages
```LaTeX
<code>
\begin{figure}[h!]
\centering
\includegraphics[scale=0.5]{LaTeX_diagram}
\caption{LaTeX diagram}
\label{fig:universe}
\end{figure}
</code>
```
* Demonstrating how to create an equation
```LaTeX
<code>
\begin{equation}
\frac{d}{dt}=\int_0^\infty
\label{eq:integral}
\end{equation}
</code>
```
* Commenting and Uncommenting
```LaTeX
<code>
%\usecolortheme{beetle}
%\usecolortheme{crane}
%\usecolortheme{dolphin}
%\usecolortheme{dove}
%\usecolortheme{fly}
%\usecolortheme{lily}
%\usecolortheme{orchid}
%\usecolortheme{rose}
%\usecolortheme{seagull}
%\usecolortheme{seahorse}
</code>
```
* uncomment by removing the percent sign
```LaTeX
<code>
%\usecolortheme{beetle}
%\usecolortheme{crane}
%\usecolortheme{dolphin}
\usecolortheme{dove}
\usecolortheme{fly}
%\usecolortheme{lily}
%\usecolortheme{orchid}
%\usecolortheme{rose}
%\usecolortheme{seagull}
%\usecolortheme{seahorse}
</code>
```
See how the colors look. 
Try with multiple variations of colors and themes commented and uncommented. 
