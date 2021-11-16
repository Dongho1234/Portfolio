
clc; clear all; close all;
C_0 = 0.5;
v_0 = 0.1; 
gamma = 0.1;
N = 20; 
Lc = 5;
sigma = 5; 
sim_time = 150; 

%---------------Part B--------------------------------------------------
sim('Problem2Partb');
time=simout(:,1);
C=simout(:,2);
v=simout(:,3);
lamda=simout(:,4);

%Graph of C 
figure(1)
plot(time,C)
hold on
title('graph of C'), xlabel('time in yr'), ylabel('C')

%Graph of v
figure(2)
plot(time,v)
hold on
title('graph of v'), xlabel('time in yr'), ylabel('v')

%Graoh of lamda
figure(3)
plot(time,lamda)
hold on
title('graph of lamda'), xlabel('time in yr'), ylabel('lamda')

%---------------Part C--------------------------------------------------
figure(4)
% starting from 0.1,steps up to 1 increasing by 0.1
% v_diff or v(0) changes as one cycle is done. 
for i= 0.1:0.1:1
    
    v_diff= i;
   
    sim('Problem2Partc');
    C_1=simout(:,2);
    v_1=simout(:,3);
    plot(v_1,C_1)
    hold on 
    
end
legend('v(0)=0.1','v(0)=0.2','v(0)=0.3','v(0)=0.4','v(0)=0.5','v(0)=0.6','v(0)=0.7','v(0)=0.8','v(0)=0.9','v(0)=1')
xlabel('v')
ylabel('C')
title('v vs C')


%---------------Part D--------------------------------------------------
%Steady State 
%roots function is used to find the roots of C polyomial. Furthermore, C
%cannot be negative that C_root(2) is used to bring only positive number.
C_root = roots([gamma gamma*sigma*Lc -sigma*Lc*N]);
C_eq = C_root(2);
v_eq = 1-gamma*(C_eq+sigma*Lc)/N;


%Components of steady state Matrix A 
a1 =  -N*sigma*Lc/(C_eq+sigma*Lc)^2-gamma;
a2 = 0;
a3 = -(1-v_eq)*v_eq*N/(C_eq+sigma*Lc)^2;
a4 = (N-2*v_eq*N)/(C_eq+sigma*Lc)-gamma;

%Component of steady state Matrix C 
c1 = sigma*Lc/(C_eq+sigma*Lc)^2;

sim('Problem2Partdlinearization')
time_linear=simout(:,1);
C_linear=simout(:,2);
V_linear=simout(:,3);
Lamda_linear=simout(:,4);

figure(5)
subplot(3,2,1)
plot(time_linear, C_linear+C_eq)
title('C linear'),legend('C linear'),xlabel('time in yr'),ylabel('C linear')
subplot(3,2,2)
plot(time, C)
title('C'),legend('C'),xlabel('time in yr'),ylabel('C')
subplot(3,2,3)
plot(time_linear, V_linear+v_eq)
title('V linear'),legend('V linear'),xlabel('time in yr'),ylabel('V linear')
subplot(3,2,4)
plot(time, v)
title('V'),legend('V'),xlabel('time in yr'),ylabel('V')
subplot(3,2,5)
plot(time_linear, Lamda_linear+C_eq/(C_eq+25))
title('Lamda linear'),legend('Lamda linear'),xlabel('time in yr'),ylabel('Lamda Linear')
subplot(3,2,6)
plot(time, lamda)
title('Lamda'),legend('Lamda'),xlabel('time in yr'),ylabel('Lamda')


figure(6)
plot(time_linear, C_linear+C_eq, time, C)
title('C linear & C'),legend('C linear', 'C'),xlabel('time in yr'),ylabel('C linear')
figure(7)
plot(time_linear, V_linear+v_eq, time, v)
title('V linear & V'),legend('V Linear','V'),xlabel('time in yr'),ylabel('V Linear')
figure(8)
plot(time_linear, Lamda_linear+C_eq/(C_eq+25), time, lamda)
title('Lamda Linear & Lamda'),legend('Lamda linear','lamda'),xlabel('time in yr'),ylabel('Lamda Linear')





    
    