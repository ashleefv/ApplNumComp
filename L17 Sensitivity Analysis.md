# **Lesson 17: Sensitivity Analysis**
This lesson focuses on sensitivity analysis, definitions, and an example walkthrough.

## **Related Readings**
[Reading 8](https://github.com/ashleefv/ApplNumComp/blob/master/RecommendedReading.md#reading-8)

## **Lecture Notes**
* Read the [lecture notes](/SensitivityAnalysis.pdf)

## **Example coding walkthrough**
  * Take sample skeleton code and fill in the blanks
  * Recreate code to fulfill [sample problem](https://github.com/ashleefv/ApplNumComp/blob/master/SensitivityAnalysis.pdf)
## **Sample skeleton code**
[Raw code](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/SensitivityExampleStarting.m)
* Note the use of each internalized function
```MATLAB
  function ICPL14
%% ICPL14 Local sensitivity analysis
clc
clear
close all
%% Define nominal values of the parameters
% four parameters a, b, c, and d
a =
parametersNominal = [a b c d];
%% Define ranges of the parameters for sensitivity analysis
% [lower bound; upper bound] for parameters (some variations needed if not uniformly 
% distributed)
parametersRanges =     
numPerturbations = size(parametersRanges,1); % number of rows
%% Define simulation independent variable range
x = linspace(0,1,100);
%% Initialize output vectors
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
* Note the figures for plotting the outputs of the sensitivity analysis
```MATLAB
%% Display the sensivity at a specific value of the independent variable
% user can specify which value of the independent variable at which to evaluate 
% the local sensitivity Here: the "end" is specified to determine the sensitivity 
% at the final value of x
figure(1)
bar(sensitivity(:,end)) 
ylabel('Normalized local sensitivity')
%% Display the senstivity as a function of the independent variable
% Determine if there is the sensitivity varies with the independent variable
figure(2)
plot(x,sensitivity)
legend
ylabel('Normalized local sensitivity')
xlabel('x')
%% Define the model that depends on the independent variable and parameters
function f = model(x,parameters)
a = parameters(1);

f=
```

##** Final working version**
[Raw code](/CHEclassFa20/In%20Class%20Problem%20Solutions/MATLAB/SensitivityExample.m)
* Note the parameters, the defined ranges and internal functions. 
```MATLAB
%% Local sensitivity analysis
function ICPL14
clc
clear
close all
%% Define nominal values of the parameters
% four parameters a, b, c, and d
a = 1;
b = 1;
c = 1;
d = 1;
parametersNominal = [a b c d];

%% Define ranges of the parameters for sensitivity analysis
% [lower bound; upper bound] for parameters (some variations needed if not 
% uniformly distributed)
parametersRanges = [-10 -10 -10 -10;
                     10  10  10  10];      
numPerturbations = size(parametersRanges,1); % number of rows

%% Define simulation independent variable range
x = linspace(0,1,100);

%% Initialize output vectors
% store f(x,p) at the nominal values, followed by lower bound and upper
% bound for each parameter in turn
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
* Note the re definition of each parameter as a unit from a matrix of the solution 
```MATLAB
%% Display the sensivity at a specific value of the independent variable
% user can specify which value of the independent variable at which to
% evaluate the local sensitivity
% Here: the "end" is specified to determine the sensitivity at the final
% value of x
figure(1)
bar(sensitivity(:,end)) 
ylabel('Normalized local sensitivity')

%% Display the senstivity as a function of the independent variable
% Determine if there is the sensitivity varies with the independent
% variable
figure(2)
plot(x,sensitivity)
legend
ylabel('Normalized local sensitivity')
xlabel('x')

%% Define the model that depends on the independent variable and parameters
function f = model(x,parameters)
a = parameters(1);
b = parameters(2);
c = parameters(3);
d = parameters(4);

f=a*exp(b*x) + c*exp(d*x);
```

## **Previous Lesson**
 * [L16 Further Exploration of GUIDE in MATLAB](/L16%20Further%20Exploration%20of%20GUIDE%20in%20MATLAB.md)

## **Next Lesson**
 * [L18 Publication Quality Figures](/L18%20Publication%20Quality%20Figures%20in%20MATLAB%20and%20Python.md)
