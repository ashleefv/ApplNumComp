# **Lesson 7: MATLAB Functions**

This lesson introduces built-in MATLAB functions for common classes of numerical methods for solving nonlinear equations, numerical integration, and ordinary differential equations (initial value problems).

## **Instructional Videos**
 * [Numerical methods](https://www.youtube.com/watch?v=430j9WP1uTQ&feature=emb_title&ab_channel=AshleeN.FordVersypt)
 
  [![](http://img.youtube.com/vi/430j9WP1uTQ/0.jpg)](http://www.youtube.com/watch?v=430j9WP1uTQ "")
* [Using MATLAB to solve a system of linear equations](https://www.youtube.com/watch?v=C4Ineu8uqGg&feature=emb_title&ab_channel=AshleeN.FordVersypt)
  
  [![](http://img.youtube.com/vi/C4Ineu8uqGg/0.jpg)](http://www.youtube.com/watch?v=C4Ineu8uqGg "")
* [MATLAB solvers](https://www.youtube.com/watch?v=8g_LB9J0RAQ&feature=emb_title&ab_channel=LearnChemE)
  
  [![](http://img.youtube.com/vi/8g_LB9J0RAQ/0.jpg)](http://www.youtube.com/watch?v=8g_LB9J0RAQ "")

## **Reflection Question**
* Find the MATLAB documentation for one of the built-in functions shown in the videos.

## **Optimization Functions**
* https://www.mathworks.com/help/matlab/optimization.html
* Solving nonlinear equations
    * fzero
    * fsolve
* Non-linear data-fitting
    * lsqcurvefit
* General optimization (minimization)
    * fminbnd
    * fmincon
* Example 1 code snippet
```MATLAB
OPTIONS = optimoptions(@lsqcurvefit, 'Algorithm', 'trust-region-reflective', 'TolX', 1e-6, 'TolFun', 1e-6, 'StepTolerance', 1e-13, 'MaxFunEvals', 1000, 'MaxIter', 3000);
[coefficients, resnorm] = lsqcurvefit(@(coefficients,Xdata) myModel(coefficients, Xdata, ModelParameters), coefficientsGuess, Xdata, Ydata, LB, UB, OPTIONS)
```

## **Numerical Integration Functions**
* mathworks.com/help/matlab/numerical-integration-and-differentiation.html
    * quad, quadl, quadv --> integral
    * trapz
* Example 2 code snippet
```MATLAB
function quad_example    
   for tt=2:numberTimePoints
   % functions and NR for the polynomial    
   % order in polyfits    
   numeratorY=(cdrugt0(1:NR)-cdrug(1:NR,tt))'...        
   .*radius(1:NR).*radius(1:NR);    
   % fit numerator integrand with 10th order polynominal    
   numerator_coef=polyfit(radius,numeratorY,10);    
   cumulrel_num(tt)=quad(@(r) CRIN(numerator_coef,r),0,1,TOL);    
   end
end

function cumulrel_integrandnum = CRIN(numerator_coef,r)    
   cumulrel_integrandnum = polyval(numerator_coef,r)
end
```

* Example 3 code snippet to determine the cumulative amount over time of a chemical leaking from a sphere under certain conditions is
Q(t)=100%∗3∫10(cdrug(r,0)−cdrug(r,t))r2dr
```MATLAB
for t=2:numberTimePoints    
    Q(t) = 100*(3*dr*trapz((cdrugt0(1:NR) - cdrug(1:NR,t))'.*radius(1:NR) .*radius(1:NR)));
end   
```


## **References for Further Exploration**
* [Algorithms for finding the root of nonlinear equations](https://www.youtube.com/watch?v=ujcZc5sPX4c&ab_channel=LearnChemE)

## **Previous Lesson**
 * [L06 Python Basics](/L06%20Python%20Basics.md)

## **Next Lesson**
 * [L08 Python Functions](/L08%20Python%20Functions.md)
