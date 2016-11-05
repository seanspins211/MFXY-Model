% 5th order optimal symplectic algorithm applied to MFXY model


% Need subarray to store intermediate values.
tic

dt = 0.0005; %time step
T  = 100.0; %Total time
N  = 100; %number of spins
e  = 1.0; %coupling stregth

reductionFactor = 100;
subArrDim = fix(T/dt/reductionFactor);

plotSlice = 50; %controls the speed of animation

% coefficients for 5th order optimal symplectic algorithm
% http://iopscience.iop.org/article/10.1088/0951-7715/5/2/011/meta
a1 = 0.339839625839110000;
a2 =-0.088601336903027329;
a3 = 0.5858564768259621188;
a4 =-0.603039356536491888;
a5 = 0.3235807965546976394;
a6 = 0.4423637942197494587;
b1 = 0.1193900292875672758;
b2 = 0.6989273703824752308;
b3 =-0.1713123582716007754;
b4 = 0.4012695022513534480;
b5 = 0.0107050818482359840;
b6 = -0.0589796254980311632;

%initial positions on unit cirle
q_array=zeros(fix(T/dt), N);
q_array(1,:)= random('Uniform',-pi,pi,[1,N]); %random initial values.
p_array=zeros(fix(T/dt),N);%all momenta set to zero

reduced_q = zeros(subArrDim, N);
reduced_q(1,:)= random('Uniform',-pi,pi,[1,N]);
reduced_p = zeros(subArrDim, N);

temp_q = zeros(reductionFactor, N);
temp_q(1,:) = q_array(1,:);
temp_p = zeros(reductionFactor, N);

steps = fix(T/dt);

for k = 1:(steps-1)
    l = k-fix(k/reductionFactor)*reductionFactor;
    if l == 0
        l = reductionFactor;
        %see source above for explanation of numerical method
        p0 = temp_p(l,:);%p_array(k,:);
        q0 = temp_q(l,:);%q_array(k,:);

        p1 = p0 - dt*b1*e/N*sumUp(q0,N);
        q1 = q0 + dt*a1*p1;
        p2 = p1 - dt*b2*e/N*sumUp(q1,N);
        q2 = q1 + dt*a2*p2;
        p3 = p2 - dt*b3*e/N*sumUp(q2,N);
        q3 = q2 + dt*a3*p3;
        p4 = p3 - dt*b4*e/N*sumUp(q3,N);
        q4 = q3 + dt*a4*p4;
        p5 = p4 - dt*b5*e/N*sumUp(q4,N);
        q5 = q4 + dt*a5*p5;
        p6 = p5 - dt*b6*e/N*sumUp(q5,N);
        q6 = q5 + dt*a6*p6;

        temp_p(1,:) = p6;
        temp_q(1,:) = q6;
        
        reduced_q(fix(k/reductionFactor)+1,:) = q6;
        reduced_p(fix(k/reductionFactor)+1,:) = p6;
        
        
    else
        %OptimalSymp(temp_q(l,:),temp_p(l,:));
        %see source above for explanation of numerical method
        p0 = temp_p(l,:);%p_array(k,:);
        q0 = temp_q(l,:);%q_array(k,:);

        p1 = p0 - dt*b1*e/N*sumUp(q0,N);
        q1 = q0 + dt*a1*p1;
        p2 = p1 - dt*b2*e/N*sumUp(q1,N);
        q2 = q1 + dt*a2*p2;
        p3 = p2 - dt*b3*e/N*sumUp(q2,N);
        q3 = q2 + dt*a3*p3;
        p4 = p3 - dt*b4*e/N*sumUp(q3,N);
        q4 = q3 + dt*a4*p4;
        p5 = p4 - dt*b5*e/N*sumUp(q4,N);
        q5 = q4 + dt*a5*p5;
        p6 = p5 - dt*b6*e/N*sumUp(q5,N);
        q6 = q5 + dt*a6*p6;

        temp_p(l+1,:) = p6;
        temp_q(l+1,:) = q6;
    end
end
disp(toc)
%modified function taken from:
%https://www.mathworks.com/matlabcentral/fileexchange/27212-animated-double-pendulum
double_pendulum(reduced_q, 0:dt*reductionFactor:T-dt, plotSlice);
%double_pendulum(reduced_q, 0:subArrDim, true,plotSlice);
%{
%Plot conservation of angular momentum
%plot(0:dt:T-dt,sum(p_array,2))
theta = linspace(-pi,pi);
xc = cos(theta);
yc = -sin(theta);
plot(xc,yc);
axis equal
%x = linspace(0,10,1000);
%y = sin(x);
%plot(x,y)
hold on
p = plot(cos(q_array(1,:)),sin(q_array(1,:)),'o','MarkerFaceColor','red');
hold off
axis manual

for k = 2:plotSlice:length(q_array(:,1))
    p.XData = cos(q_array(k,:));
    p.YData = sin(q_array(k,:));
    drawnow
end
%}
