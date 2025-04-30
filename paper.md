---
title: 'ApplNumComp: An Open Access Introductory Course for Applied Numerical Computing'
tags:
  - Git
  - LaTeX
  - MATLAB
  - Python
  - computational science and engineering
authors:
  - name: Ashlee N. {Ford Versypt}^[Corresponding author]
    orcid: 0000-0001-9059-5703
    affiliation: "1, 2, 3, 4"
  - name: Duncan H. Mullins
    orcid: 0000-0001-7173-9695
    affiliation: "1, 2"
affiliations:
 - name: School of Chemical Engineering, Oklahoma State University
   index: 1
 - name: Department of Chemical and Biological Engineering, University at Buffalo, The State University of New York
   index: 2
 - name: Department of Engineering Education, University at Buffalo, The State University of New York
   index: 3
 - name: Institute for Computational and Data Sciences, University at Buffalo, The State University of New York
   index: 4   
date: 22 April 2021
bibliography: paper.bib

---

# Summary
ApplNumComp is a repository of open educational resources supporting an introductory course on Applied Numerical Computing. Topics include Git for version control, LaTeX for typesetting, reproducible research computing, and MATLAB and Python for high-level programming and scientific computing applications of solving systems of differential equations, estimating parameters for models using regression, creating publication quality figures, and developing graphical user interfaces. The lessons can be used collectively for a similar course at another institution, for independent study by an online learner, or for incorporation of individual lessons (modules or examples) into other courses that involve related topics. 
 
# Statement of Need
An introductory course on Applied Numerical Computing was developed for upper division undergraduate and graduate students interested in research and industrial projects involving mathematical modeling using computational tools. The class was designed to fill a gap distinct from introductory programming and numerical methods courses and was intended to be very practical. Graduate students new to computational research were the primary student group targeted for the course topics. We have previously detailed the course [@FordVersypt2019] and the final course project [@Ruggiero2018].

No single textbook covers all of the topics in the Applied Numerical Computing course. As the course emphasized best practices for reproducible research computing, we sought to apply the concept to the course materials for a reproducible computing educational experience. Here, we have curated a set of open educational resources for others to engage with the course lessons outside of the institution's learning management system and outside of the formal course. The main repository is organized into a set of lessons as Markdown-formatted text-based open-source webpages that include code snippets, explanatory text, reflection questions, sample solution software files, links to supplemental videos, related references, and other instructional materials. Each lesson can be considered as a stand alone module on a particular computational topic; however, there are conceptual links between some of the lessons. Many of the lessons include detailed MATLAB or Python coding examples, or both as in the case for Lesson 10: Python and MATLAB Plotting. For instance, Lesson 13: Parameter Estimation in Python provides a worked example for fitting parameters to one differential equation and the solution .py file followed by a second example for fitting parameters to multiple differential equations. Related Lessons 11 and 12 provide supportive general information and complimentary content with examples in MATLAB. Documentation associated with MATLAB or Python often only shows much simpler examples. Open-source worked examples are limited for even just solving multiple differential equations simultaneously independently from the parameter estimation. The full list of lessons is available [here](https://github.com/ashleefv/ApplNumComp#lessons). Other supporting materials include a list of [suggested readings](https://github.com/ashleefv/ApplNumComp/blob/master/RecommendedReading.md) with links to the sources, the full set of [computational assignments](https://github.com/ashleefv/ApplNumComp#computational-assignments), and the course [learning objectives](https://github.com/ashleefv/ApplNumComp#course-learning-objectives).

Our experiences with the course and materials have been positive. Over the 5 course offerings, 63 graduate students and 27 undergraduate students took the course. The students were majoring in the following 12 fields: chemical engineering, mechanical engineering, aerospace engineering, civil engineering, environmental engineering, chemistry, plant and soil sciences, mathematics, electrical and computer engineering, petroleum engineering, physics, and industrial engineering. Most similar electives for cross-listed undergradaute/graduate credit averaged 10 students in a term, while this course averaged 18 per term. Typically, similar electives are offered only once in four semesters. This course has been popular enough to offer each fall semester. There was a drop in graduate enrollment in the course in 2020, likely due to COVID-19 induced reductions in the overall number of new graduate students in science and engineering fields at the university. The course has become highly recommended for first year graduate students in computational research groups across campus and for all first year mechanical and aerospace engineering graduate students. Additionally, it is included in the interdisciplinary Data Science minor available to undergraduate students. The conference proceedings paper detailing the course [@FordVersypt2019] has been dowloaded from the [American Society for Engineering Educaion Papers on Engineering Education Repository](https://peer.asee.org/an-interdisciplinary-elective-course-to-build-computational-skills-for-mathematical-modeling-in-science-and-engineering) 140 times as of June 23, 2021. In January 2021, the authors left the university where the course was developed, and multiple faculty have reached out to request access to the course materials either for offering the course themselves in the future or for sharing the materials with their students for self-paced learning. The ApplNumComp GitHub repsitory is already filling that direct need. The repository has also been disseminated through the [Computer Aids for Chemical Engineering website](https://cache.org/computational-tools-development). The authors and the Computer Aids for Chemical Engineering Corporation trustees have been in discussion about how to further disseminate lessons in modular form from ApplNumComp into a variety of chemical engineering courses across other universities. The authors have already presented these materials at conferences for the American Society for Engineering Education and the American Institute for Chemical Engineers (AIChE) and a [webinar]( https://www.aiche.org/academy/webinars/teaching-computational-skills-chemical-engineers) for the AIChE. A workshop proposal is being developed for sharing the materials in other venues such as the Chemical Engineering Summer School, held once every five year for junior faculty, with the next offering scheduled in 2022.
 
# Author Contributions
Ashlee N. Ford Versypt developed the Applied Numerical Computing course at Oklahoma State University and taught it annually 2016-2020. The materials presented here were developed and delivered in a hybrid of in-person, online synchronous, and online asynchronous formats in Fall 2020. Duncan H. Mullins, a PhD student from Dr. Ford Versypt’s lab, took the course in Fall 2019, served as a teaching assistant for the course in 2020, and aided in conversion of the course to this online open-access version.

# Acknowledgments
This material is based upon work supported by the National Science Foundation under Grant No. 1845117 and a minigrant from Computer Aids for Chemical Engineering Corp., both to Ashlee N. Ford Versypt.

# References
