%% FANUC R-2000iC/165F
% 
clear all
syms q1 q2 q3 q4 q5 q6 d1 d2 d3 d4 d5 d6 real

%% Forward kinematics
T = Tz(d1)*Rz(q1)*Ty(d2)*Rx(q2)*Tz(d3)*Rx(q3)*Tz(d4)*Ty(d5)*Ry(q4)*Rx(q5)*Ty(d6)*Ry(q6);
T = simplify(T);

disp('Forward kinematics');
disp(T);



%% Skew theory
%matrices of transformations
T0 = [1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1];
T1 = T0*Tz(d1)*Rz(q1)*Ty(d2);
T2 = T1*Rx(q2)*Tz(d3);
T3 = T2*Rx(q3)*Tz(d4)*Ty(d5);
T4 = T3*Ry(q4);
T5 = T4*Rx(q5);
%T6 = T;
O6 = T(1:3,4);

Z0 = T0(1:3,3);
O0 = T0(1:3,4);
J1 = simplify([cross(Z0,O6-O0);Z0]);

X1 = T1(1:3,1);
O1 = T1(1:3,4);
J2 = simplify([cross(X1,O6-O1);X1]);

X2 = T2(1:3,1);
O2 = T2(1:3,4);
J3 = simplify([cross(X2,O6-O2);X2]);

Y3 = T3(1:3,2);
O3 = T3(1:3,4);
J4 = simplify([cross(Y3,O6-O3);Y3]);

X4 = T4(1:3,1);
O4 = T4(1:3,4);
J5 = simplify([cross(X4,O6-O4);X4]);

Y5 = T5(1:3,2);
O5 = T5(1:3,4);
J6 = simplify([cross(Y5,O6-O5);Y5]);

%% Numerical method

T0 = T;
T0 = inv(T0(1:3,1:3));
T0=[T0,zeros(3,1);0 0 0 1];
Td =  Rzd(q1)*Tz(d1)*Ty(d2)* Rx(q2)*Tz(d3)* Rx(q3)*Tz(d4)*Ty(d5)* Ry(q4)* Rx(q5)* Ry(q6)*Ty(d6)*T0; J1 = simplify(Jcol(Td));
Td =  Rz(q1)*Tz(d1)*Ty(d2)*Rxd(q2)*Tz(d3)* Rx(q3)*Tz(d4)*Ty(d5)* Ry(q4)* Rx(q5)* Ry(q6)*Ty(d6)*T0; J2 = simplify(Jcol(Td));
Td =  Rz(q1)*Tz(d1)*Ty(d2)* Rx(q2)*Tz(d3)*Rxd(q3)*Tz(d4)*Ty(d5)* Ry(q4)* Rx(q5)* Ry(q6)*Ty(d6)*T0; J3 = simplify(Jcol(Td));
Td =  Rz(q1)*Tz(d1)*Ty(d2)* Rx(q2)*Tz(d3)* Rx(q3)*Tz(d4)*Ty(d5)*Ryd(q4)* Rx(q5)* Ry(q6)*Ty(d6)*T0; J4 = simplify(Jcol(Td));
Td =  Rz(q1)*Tz(d1)*Ty(d2)* Rx(q2)*Tz(d3)* Rx(q3)*Tz(d4)*Ty(d5)* Ry(q4)*Rxd(q5)* Ry(q6)*Ty(d6)*T0; J5 = simplify(Jcol(Td));
Td =  Rz(q1)*Tz(d1)*Ty(d2)* Rx(q2)*Tz(d3)* Rx(q3)*Tz(d4)*Ty(d5)* Ry(q4)* Rx(q5)*Ryd(q6)*Ty(d6)*T0; J6 = simplify(Jcol(Td));


%% Numerical Print Results to Visual See

Jacobian_num = [J1, J2, J3, J4, J5, J6];
disp('Numerical method');
disp(Jacobian_num);


%% Skew Print Results to Visual See
Jacobian_skew = [J1, J2, J3, J4, J5, J6];
disp('Skew theory');
disp(Jacobian_skew);
%% Check 3 methods
disp('Numerical method - Skew theory');
dif = simplify(Jacobian_num - Jacobian_skew);
disp(dif);
%% data 
% q1 = 0;
% q2 = 0;
% q3 = 0;
% q4 = 0;
% q5 = 0;
% q6 = 0;
% d1 = 0;
% d2 = 312;
% d3 = 1075;
% d4 = 225;
% d5 = 1280;
% d6 = 215;

%% Kinematic Singularity analysis
%1 case
%2 case
%3 case
