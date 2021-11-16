clc;
clear all;

Kc_vec= [1,2,3,4,5];
tau=300;
K= 1;
step_time = 3500;
figure(1)
for i=1:5
    Kc=Kc_vec(i);
    sim('EX12P1');
    time= simout(:,1);
    yd = simout(:,2);
    output = simout(:,3);
    plot(time, output)
    hold on
end

plot(time, yd)
legend('Kc=1','Kc=2','Kc=3','Kc=4','Kc=5','yd')
v= [0 3500 -8 12];
axis(v)
hold off

clear K;

K_vec= [4,5];
figure(2)
for i=1:2
    K=K_vec(i);
    G=tf([K],[tau 1]);
    G.outputd=120;
    bode(G)
    hold on
    
end
legend('K=4','K=5')

K_vec= [4,5];
figure(3)
for i=1:2
    K=K_vec(i);
    G=tf([K],[tau 1]);
    G.outputd= 120; %.outputd=120 is used to give time delay
    
    nyquist(G)
    hold on
    
end




