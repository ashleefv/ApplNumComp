# ApplNumComp: An Open Access Introductory Course for Applied Numerical Computing

This repository contains a set of lessons on Applied Numerical Computing covering Git for version control, LaTeX for typesetting, and MATLAB and Python for high-level programming and scientific computing. 

Note: this site is based on the Fall 2020 course offering: CHE 4753/5753 Applied Numerical Computing for Scientists & Engineers at Oklahoma State University created and taught by Ashlee N. Ford Versypt, Ph.D. and assisted by Duncan H. Mullins. The translation of course materials to the online lessons here was supported by a mini-grant from the [Computer Aids in Chemical Engineering (CACHE) Corporation](https://cache.org/). This material is based upon work supported by the National Science Foundation under Grant No. 2133411 (formerly 1845117) to Dr. Ford Versypt. 

Course repository:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15313369.svg)](https://doi.org/10.5281/zenodo.15313369)

Paper: 
[![DOI](https://jose.theoj.org/papers/10.21105/jose.00143/status.svg)](https://doi.org/10.21105/jose.00143)

ASEE Conference proceedings paper about the course: A. N. Ford Versypt, "An Interdisciplinary Elective Course to Build Computational Skills
for Mathematical Modeling in Science and Engineering," in ASEE Annual Meeting,
Tampa, FL, 2019. [Online](https://peer.asee.org/32072).

## Statement of Need
An introductory course on Applied Numerical Computing was developed for upper division undergraduate and graduate students interested in research and industrial projects involving mathematical modeling using computational tools. The class was designed to fill a gap distinct from introductory programming and numerical methods courses and was intended to be very practical. Graduate students new to computational research were the primary student group targeted for the course topics. We have previously detailed the course [FordVersypt 2019](https://doi.org/10.18260/1-2--32072) and the final course project [Ruggiero 2018]( https://doi.org/10.22369/issn.2153-4136/9/1/3). No single textbook covers all of the topics in the Applied Numerical Computing course. As the course emphasized best practices for reproducible research computing, we sought to apply the concept to the course materials for a reproducible computing educational experience. Here, we have curated a set of open educational resources for others to engage with the course lessons outside of the institution's learning management system and outside of the formal course. The main repository is organized into a set of lessons as Markdown-formatted text-based open-source webpages that include code snippets, explanatory text, reflection questions, sample solution software files, links to supplemental videos, related references, and other instructional materials. Each lesson can be considered as a stand alone module on a particular computational topic; however, there are conceptual links between some of the lessons. Many of the lessons include detailed MATLAB or Python coding examples, or both as in the case for Lesson 10: Python and MATLAB Plotting. For instance, Lesson 13: Parameter Estimation in Python provides a worked example for fitting parameters to one differential equation and the solution .py file followed by a second example for fitting parameters to multiple differential equations. Related Lessons 11 and 12 provide supportive general information and complimentary content with examples in MATLAB. Documentation associated with MATLAB or Python often only shows much simpler examples. Open-source worked examples are limited for even just solving multiple differential equations simultaneously independently from the parameter estimation. The full list of lessons is available [here](https://github.com/ashleefv/ApplNumComp#lessons). Other supporting materials include a list of [suggested readings](https://github.com/ashleefv/ApplNumComp/blob/master/RecommendedReading.md) with links to the sources, the full set of [computational assignments](https://github.com/ashleefv/ApplNumComp#computational-assignments), and the course [learning objectives](https://github.com/ashleefv/ApplNumComp#course-learning-objectives).

## Course Description
Practical software tools for computational problem solving in science and engineering: version control (e.g., Git), mathematical typesetting (e.g., LaTeX), graphical user interfaces, and high level programming languages with libraries of solvers and visualization tools (e.g., Python and MATLAB). Application of numerical computing methods to solve systems of differential and algebraic equations and to estimate model parameters using optimization.

## Prerequisites
* Junior, Senior, or Graduate Student status
* Differential equations and/or Calculus III
* Basic familiarity with at least one programming language and introductory terminology such as program, for loop, if statement, etc. (e.g., C/C++, Fortran, Python, MATLAB, Maple, Java, Polymath, VBA). Note that these expectations are at the level of a first year engineering introductory computer programming class.
* Or consent of the instructor

## Course Learning Objectives
Upon completion of this course, you should be able to
* utilize Git for version control using common commands: status, add, commit, push, pull
* write scientific reports and similar documents in the LaTeX typesetting language using an article template and include equations, figures, tables, document hierarchy, cross referencing, and citations (using BibTeX) in the documents
* use best practices for computational problem solving and research and scientific computing as described in publications provided as assigned readings
* develop graphical user interfaces for interactive applied numerical computing
* program well-documented, readable code in the high-level languages of Python and MATLAB that uses libraries, built-in functions, and user-defined functions
  * to solve systems of linear and nonlinear equations,
  * to numerically integrate functions and data,
  * to solve systems of ordinary and partial differential equations, 
  * to estimate parameters for mathematical models using optimization and data fitting tools, 
  * to create publication quality figures 

## Reading Materials
A full list of recommended and optional reading materials that complement the course lessons are available [here](https://github.com/ashleefv/ApplNumComp/blob/master/RecommendedReading.md).

## Note on Accessibility
All of the YouTube videos produced by Dr. Ford Versypt have captions transcribed by Otter.ai and edited by Dr. Ford Veryspt and Duncan Mullins. PDF versions of all video transcripts are available upon request.

## Lessons
* [L01 Git for Version Control](/L01%20Git%20for%20Version%20Control.md)
  * Downloading, installing, and using Git for version control.
* [L02 LaTeX Basics](/L02%20LaTeX%20Basics.md)
  * Downloading, installing, and using LaTeX for typesetting and computational writing.
* [L03 Advanced LaTeX Topics](/L03%20Advanced%20LaTeX%20Topics.md)
  * Walkthrough of LaTeX functionality, examples, and templates for journals or thesis writing.
* [L04 MATLAB Basics](/L04%20MATLAB%20Basics.md)
  * Basic MATLAB functionality.
* [L05 MATLAB Basics Continued](/L05%20MATLAB%20Basics%20Cont.md)
  * Learning MATLAB functions, how to write modules, and sample problems.
* [L06 Python Basics](/L06%20Python%20Basics.md)
  * Learning basics of Python and converting an existing MATLAB code into Python.
* [L07 MATLAB Functions](/L07%20MATLAB%20Functions.md)
  * Introducing MATLAB built-in functions: nonlinear equation solving, integration, ODE IVPs.
* [L08 Python Functions](/L08%20Python%20Functions.md)
  * Introducing Python built-in functions: nonlinear equation solving, integration, and basic ODEs.
* [L09 MATLAB to Python Conversion](/L09%20MATLAB%20to%20Python%20Conversion.md)
  * Converting MATLAB code into Python code, using a system of ODEs.
* [L10 Python and MATLAB Plotting](/L10%20Python%20and%20MATLAB%20Plotting.md)
  * Plotting capabilities of Python and MATLAB.
* [L11 Parameter Estimation in MATLAB](/L11%20Parameter%20Estimation%20in%20MATLAB.md)
  * Estimating parameters in MATLAB and examples.
* [L12 Advanced Parameter Estimation in MATLAB](/L12%20Advanced%20Parameter%20Estimation%20in%20MATLAB.md)
  * Further capabilities of MATLAB for parameter estimation.
* [L13 Parameter Estimation in Python](/L13%20Parameter%20Estimation%20in%20Python.md)
  * Parameter estimatation in Python  and examples.
* [L14 Introduction to GUIs and GUIs in MATLAB](/L14%20Introduction%20to%20GUIs.md)
  * Graphical User Interfaces (GUIs) and an overview of the MATLAB tools for creating them.
* [L15 GUI Examples in MATLAB](/L15%20MATLAB%20and%20GUIDE.md)
  * Using GUIDE in MATLAB and designing callbacks.
* [L16 Further Exploration of GUIDE in MATLAB](/L16%20Further%20Exploration%20of%20GUIDE%20in%20MATLAB.md)
  * Editing apps with GUIDE.
* [L17 Sensitivity Analysis](/L17%20Sensitivity%20Analysis.md)
  * Conducting a sensitivity analysis.
* [L18 Publication Quality Figures in MATLAB and Python](/L18%20Publication%20Quality%20Figures%20in%20MATLAB%20and%20Python.md)
  * Creating publication quality images in MATLAB and Python.
* [L19 GUIs in Python](/L19%20GUIs%20in%20Python.md)
  * Creating GUIs in Python and PyQt5.
* [L20 Validation and Verification](/L20%20Validation%20and%20Verification.md)
  * Validation and verification.
* [L21 Agent Based Modeling and Open Source Software](/L21%20Agent%20Based%20Modeling%20and%20Open%20Source%20Software.md)
  * Agent based modeling and a variety of tools and examples of open source software.
* [L22 Reproducible Research Computing](/L22%20Reproducible%20Research%20Computing.md)
  * Presenting the case for reproducible research computing.

## Recommended Software
* [Anaconda Python 3.x](https://www.anaconda.com/products/individual)
  * Online editor: [Google Colab](https://colab.research.google.com/)
* MATLAB through [OSU software downloads for OSU students and faculty only](https://ceat.okstate.edu/itservices/software-downloads/mathworks-matlab-simulink.html)
  * Online editor: [MATLAB Online](https://matlab.mathworks.com/)
* [Git](https://www.atlassian.com/git/tutorials/install-git)
  * Online repository location: [GitHub](https://github.com/) or [Bitbucket](https://bitbucket.org/)
* LaTeX
  * [MiKTeX](https://miktex.org/download)
  * [MacTeX for Mac users](http://www.tug.org/mactex/)
  * Preferred editor: [Texmaker](https://www.xm1math.net/texmaker/download.html)
  * Online editor: [Overleaf](https://www.overleaf.com)

## Computational Assignments
The assignments, related files, and grading rubrics are available in the [Assignments folder of this repository](https://github.com/ashleefv/ApplNumComp/tree/master/Assignments). The overviews for the assignments are as follows:
1.	Version control in Git and document typesetting in LaTeX 
    *	Create a Git repository to track versions of assignment files (in this and subsequent assignments)
    *	Produce a LaTeX document with several required components using research or major course work as the topic
2.	Programming in MATLAB while developing best practices for scientific computing (version control, commenting, and documentation)
    *	Write a function to define a system of ODEs
    *	Provide well-documented code following specified standards
    *	Generate an HTML output file from MATLAB documenting the code
3.	Using built-in functions and library routines for numerical methods (specifically ODE solvers) in MATLAB and Python
    *	Solve a system of ODEs using numerical solvers in MATLAB and Python
    *	Plot the results
    *	Generate an HTML file to document the code from MATLAB
    *	Generate a Jupyter Notebook file and a LaTeX file to document the code from Python
4.	Parameter estimation of dynamic models using MATLAB and Python
    *	Solve a system of ODEs using numerical solvers in MATLAB and Python
    *	Use an optimization routine to iterate the ODE model parameters to fit data
    *	Plot the results
    *	Generate an HTML file to document the code from MATLAB
    *	Generate a Jupyter Notebook file and a LaTeX file to document the code from Python
5.	Develop a GUI in MATLAB starting with an existing computational model
    *	Create a GUI in MATLAB to take user inputs and display simulation results from a set of user-defined functions provided by the instructor
6.	"Final Project": Design and construct a GUI in MATLAB, verify code implementation, and review content covered throughout the course
    *	Develop a GUI for MATLAB that takes a user-specified number of ODEs and explicit equations as input, solves the system of ODEs using ode45 in MATLAB, returns and exports the solution vector, and plots the solution vector components against the independent variable
    *	Verify that the GUI works for test cases from the systems of ODEs used in Computational Assignments 3 and 4

## Course Implementation Tips
* A. N. Ford Versypt, An Interdisciplinary Elective Course to Build Computational Skills for Mathematical Modeling in Science and Engineering, Proceedings of the ASEE Annual Conference, Tampa, FL, 2019. [DOI: 10.18260/1-2--32072](https://strategy.asee.org/an-interdisciplinary-elective-course-to-build-computational-skills-for-mathematical-modeling-in-science-and-engineering).
* “Teaching Computational Skills for Chemical Engineers,” Webinar, AIChE Education Division, Feb 2020. [Archived recording](https://www.aiche.org/academy/webinars/teaching-computational-skills-chemical-engineers-0)

## Community guidelines
For third parties wishing to 1) contribute to the module, 2) report issues or problems with the module, 3) or seek support, you may submit an issue suggesting an edit or modification. Dr. Ford Versypt can be contacted via her university email address ashleefv@buffalo.edu for further support.

(c) 2025 Ashlee N. Ford Versypt and Duncan H. Mullins
