clc; clear all; close all;

K= 3;
tau1 = 2;
tau2 = 6;
Km = 1; 
taum = 0.2;

num1 = [K];
num2 = [Km];
denom1 = conv([tau1 1],[tau2 1]);
denom2 =[taum 1];


num = conv(num1, num2);
denom = conv(denom1, denom2);
GpH = tf(num,denom);

a_vec = [0 1 3 5];
%Part A
for i=1:4
    a = a_vec(i);
    GpH.outputd= a;
    bode(GpH)
    hold on
end
legend('a=0','a=1','a=3','a=5')

%Part B
for i=1:4
    a =a_vec(i);
    figure(i+1)
    GpH.outputd= a;
    margin(GpH)
    [GM, PM, WCP, WCG] = margin(GpH);
    GM_dB = 20*log10(GM); %Change it to dB
    data(i,1) = a;  %Matrix  i = row 1,2,3,4,5= column
    data(i,2) = GM_dB;
    data(i,3) = PM;
    data(i,4) = WCP;
    data(i,5) = WCG;
    
end
data



