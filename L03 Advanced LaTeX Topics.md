# **Lesson 3: Advanced LaTeX Topics**

This lesson focuses on LaTeX templates for technical and/or longer documents, specifically for writing papers, theses, and dissertations.

## **Instructional Videos**
* [LaTeX templates thesis and dissertation examples](https://www.youtube.com/watch?v=gHp1IWxEink&feature=emb_title&ab_channel=AshleeN.FordVersypt)
   
[![](http://img.youtube.com/vi/gHp1IWxEink/0.jpg)](http://www.youtube.com/watch?v=gHp1IWxEink "")
 
* [LaTeX templates Elsevier example](https://www.youtube.com/watch?v=vO9O7Nuk0XM&feature=emb_title&ab_channel=AshleeN.FordVersypt)
   
[![](http://img.youtube.com/vi/vO9O7Nuk0XM/0.jpg)](http://www.youtube.com/watch?v=vO9O7Nuk0XM "")
 
* [LaTeX templates PLOS One example](https://www.youtube.com/watch?v=2IpdTQhj6cg&feature=emb_title&ab_channel=AshleeN.FordVersypt)
   
[![](http://img.youtube.com/vi/2IpdTQhj6cg/0.jpg)](http://www.youtube.com/watch?v=2IpdTQhj6cg "")
 
## **Reflection**
* For a scientific journal in your field, perform an internet search to find the link to an online .tex template or instructions for using a TeX template . If you're not familiar with any scientific journals yet, try "tex template _ journal" where _ is the name of your field.
* Download the template you found and look through the .tex file like in the LaTeX Templates PLoS Example video. What are some of the similarities? Differences?

## **Advantages of LaTeX for Technical and/or Longer Documents**
* Version control
* Integration of templates for conferences, publishers, universities
* File size reduction, e.g., Dr. Ford Versypt's 256 page thesis is only 2.9 MB
* Reduce headaches with figure numbering, equation numbering, cross-referencing, table of contents, or turning on or off chapters (e.g., using \include)

## **Activity**
* Create a presentation using the Beamer package in LaTeX. [Beamer presentation template](https://github.com/ashleefv/ApplNumComp/blob/master/CHEclassFa20/In%20Class%20Problem%20Activities/LaTeX/BeamerPresTemplate.tex)
* Either run the template in Overleaf or get the [Beamer package from CTAN](https://ctan.org/pkg/beamer?lang=en)
* Enable various themes and color schemes to demonstrating LaTeX template functionality. Edit by commenting or uncommenting (via % at the start of the line) various themes and running
```Latex
\usecolortheme{albatross}
%\usecolortheme{beaver}
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
%\usecolortheme{whale}
%\usecolortheme{wolverine}

%\setbeamertemplate{footline} % To remove the footer line in all slides uncomment this line
%\setbeamertemplate{footline}[page number] % To replace the footer line in all slides with a simple slide count uncomment this line
```
* Enable various stylistic themes

```Latex
% The Beamer class comes with a number of default slide themes
% which change the colors and layouts of slides. Below this is a list
% of all the themes, uncomment each in turn to see what they look like.

%\usetheme{default}
%\usetheme{AnnArbor}
%\usetheme{Antibes}
\usetheme{Bergen}
%\usetheme{Berkeley}
%\usetheme{Berlin}
%\usetheme{Boadilla}
%\usetheme{CambridgeUS}
%\usetheme{Copenhagen}
%\usetheme{Darmstadt}
%\usetheme{Dresden}
%\usetheme{Frankfurt}
%\usetheme{Goettingen}
%\usetheme{Hannover}
%\usetheme{Ilmenau}
%\usetheme{JuanLesPins}
%\usetheme{Luebeck}
%\usetheme{Madrid}
%\usetheme{Malmoe}
%\usetheme{Marburg}
%\usetheme{Montpellier}
%\usetheme{PaloAlto}
%\usetheme{Pittsburgh}
%\usetheme{Rochester}
%\usetheme{Singapore}
%\usetheme{Szeged}
%\usetheme{Warsaw}
```
* Edit text on the slides and duplicate slides as necessary to fill out a presentation
* Remove or comment out irrelevant slide types

## **Templates**
* [OSU LaTeX Thesis Template](https://github.com/mitchute/OSULaTeXTheisTemplate)
* [UIUC Thesis Template](https://github.com/bardsoftware/template-thes-uiuc)
* [UB Thesis Template](https://www.overleaf.com/latex/templates/thesis-template-for-university-at-buffalo/gvttxscsrwzm)
* [Elsevier Template](https://www.elsevier.com/authors/policies-and-guidelines/latex-instructions)
* [PLOS One Template](https://journals.plos.org/plosone/s/latex)
* [Full Beamer Template](https://bitbucket.org/ashleefv/checlassfa20/src/master/In%20Class%20Problem%20Activities/LaTeX/BeamerPresTemplate.tex)

## **References for Further Exploration**
* [Math into LaTeX: An Introduction to LaTeX and AMS-LaTeX](https://www.springer.com/gp/book/9780817641313)
* [Short Math Guide for LaTeX](http://tug.ctan.org/info/short-math-guide/short-math-guide.pdf)
* For more practice see [Beamer user guide](https://www.overleaf.com/learn/latex/beamer)

## **Previous Lesson**
* [L02 LaTeX Basics](/L02%20LaTeX%20Basics.md)

## **Next Lesson**
* [L04 MATLAB Basics](/L04%20MATLAB%20Basics.md)
