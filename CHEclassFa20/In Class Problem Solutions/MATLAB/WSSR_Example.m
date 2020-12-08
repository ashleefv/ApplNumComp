%% Parameter estimation function for PK-PD model for ACE inhibition

function param_estimation
format long e
close all
%% Take data from plots
% X is a vector of time points. Ydata is a matrix of Ang I, Ang II, and
% PRA values at each of the time points estimated from Shionori data during
% inhibition by ACE inhibitor drugs
paramsfile = strcat('params_',drugname,renalfunction,'.mat');
params = matfile(paramsfile);
%PK_params = matfile(strcat('PK_',paramsfile));
AngIIvalue = params.AngIIvalue;
PRAvalue = params.PRAvalue;
Xdata = params.Xdata; % row vector for measurement time points
sim_time_end = 24;
Ydata = [AngIvalue;...% AngII row vector for measured values
    AngIIvalue;%...%ANGI row vector for measured values
    PRAvalue];% PRA row vector for measured values
sigma = [AngIerror;...% AngII row vector for stddev values
    AngIIerror;%...%ANGI row vector for stddev values      
    PRAerror]; % PRA row vector for stddev values
Ydata_weighted = Ydata./sigma;
% Guesses for coefficients
VmaxoverKm = 1;
k_cat_Renin = 1;
k_feedback =  1;
feedback_capacity = 250;
k_cons_AngII = 1;
% package the coefficients
coefficientsguess(1) = VmaxoverKm;
coefficientsguess(2) = k_cat_Renin;
coefficientsguess(3) = k_feedback;
coefficientsguess(4) = feedback_capacity;
coefficientsguess(5) = k_cons_AngII;
LB = [0,0,0,250,0]; % lower bound %feedback lower bound
UB = []; % upper bound
OPTIONS = optimoptions(@lsqcurvefit,'Algorithm','trust-region-reflective',...
    'TolX', 1e-6, 'TolFun', 1e-6, 'StepTolerance', 1e-13, 'MaxFunEvals', 1000, 'MaxIter', 3000); % use default for first guess
tic
[coefficients, resnorm_fitted] = lsqcurvefit(@(coefficients,Xdata) model(coefficients, Xdata, sigma), coefficientsguess, Xdata, Ydata_weighted, LB, UB, OPTIONS)
toc

%% Create Ycalc matrix for model output at Xdata values
Ycalc_weighted = model(coefficients,Xdata,sigma);
Ycalc = Ycalc_weighted.*sigma;
resnorm = sum((Ycalc(1,:)-Ydata(1,:)).^2 + (Ycalc(2,:)-Ydata(2,:)).^2 + (Ycalc(3,:)-Ydata(3,:)).^2)
resnorm_weighted = sum((Ycalc_weighted(1,:)-Ydata_weighted(1,:)).^2 + (Ycalc_weighted(2,:)-Ydata_weighted(2,:)).^2 + (Ycalc_weighted(3,:)-Ydata_weighted(3,:)).^2)
for i = 1:3
    residual(i,:) = Ydata(i,:) - Ycalc(i,:);
    RMSE(i) = sqrt(mean(residual(i,:).^2)); 
end
