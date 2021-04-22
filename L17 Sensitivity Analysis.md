# **Lesson 17: Sensitivity Analysis**
This lesson focuses on sensitivity analysis, definitions, and an example walkthrough.

## **Related Readings**
[Reading 8](https://github.com/ashleefv/ApplNumComp/blob/master/RecommendedReading.md#reading-8)

## **Lecture Notes**
* Read the [lecture notes](/SensitivityAnalysis.pdf)

## **Instructional Video**
* [Sensitivity analysis](https://youtu.be/snJ048TJWKY)
 
[![](http://img.youtube.com/vi/snJ048TJWKY/0.jpg)](https://youtu.be/snJ048TJWKY "")
 
* Note: this recording is from the 2019 synchronous session when the lecture order was different than in this repository.
 
## **Activity**
* Create a function .m file
```MATLAB
function SensitivityExample
clc
clear
close all
```
* Define nominal values of the parameters: four parameters a, b, c, and d
```MATLAB
a = 1;
b = 1;
c = 1;
d = 1;
parametersNominal = [a b c d];
```
* Define ranges of the parameters for sensitivity analysis
```MATLAB
% [lower bound; upper bound] for parameters (some variations needed if not uniformly 
% distributed)
parametersRanges = [-10 -10 -10 -10;
                     10  10  10  10];      
numPerturbations = size(parametersRanges,1); % number of rows
```
* Define simulation independent variable range
```MATLAB
x = linspace(0,1,100);
```
* Initialize output vectors
```MATLAB
% store f(x,p) at the nominal values, followed by lower bound and upper bound 
% for each parameter in turn
output = zeros(numPerturbations*length(parametersNominal)+1,length(x)); 
sensitivity = zeros(numPerturbations*length(parametersNominal)+1,length(x)); 
outputNominal = model(x,parametersNominal);
output(1,:) = outputNominal;

for i = 1:length(parametersNominal)
    for n = 1:numPerturbations
        parametersPerturbed = parametersNominal;
        parametersPerturbed(1,i) = parametersRanges(n,i);
        ParamChange = (parametersRanges(n,i)-parametersNominal(i))...
            ./parametersNominal(i);
        output(numPerturbations*i+n-1,:) = model(x,parametersPerturbed);
        sensitivity(numPerturbations*i+n-1,:) = ...
            (output(numPerturbations*i,:)-outputNominal)...
            /outputNominal/ParamChange;
    end
end
```
* Display the sensivity at a specific value of the independent variable
```MATLAB
% user can specify which value of the independent variable at which to evaluate 
% the local sensitivity Here: the "end" is specified to determine the sensitivity 
% at the final value of x
figure(1)
bar(sensitivity(:,end)) 
ylabel('Normalized local sensitivity')
```
![Expected Graph 1](/Lesson_images/Figure1_L17.jpg)

* Display the senstivity as a function of the independent variable
```MATLAB
% Determine if there is the sensitivity varies with the independent variable
figure(2)
plot(x,sensitivity)
legend
ylabel('Normalized local sensitivity')
xlabel('x')
```
![Expected Graph 2](/Lesson_images/Figure2_L17.jpg)

* Define the model that depends on the independent variable and parameters
```MATLAB
function f = model(x,parameters)
a = parameters(1);
b = parameters(2);
c = parameters(3);
d = parameters(4);

f=a*exp(b*x) + c*exp(d*x);
```
* Solution [.m file](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/SensitivityExample.m)

## **Previous Lesson**
 * [L16 Further Exploration of GUIDE in MATLAB](/L16%20Further%20Exploration%20of%20GUIDE%20in%20MATLAB.md)

## **Next Lesson**
 * [L18 Publication Quality Figures](/L18%20Publication%20Quality%20Figures%20in%20MATLAB%20and%20Python.md)
