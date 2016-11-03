function double_pendulum(q, timeArray, movie, plotSlice)
%clear All; clf;

%nframes=duration*fps;

%sol=ode45(@double_pendulum_ODE,[0 duration], ivp);
%t = linspace(0,duration,nframes);
t = timeArray;
%y=deval(sol,t);

%phi1=y(1,:)'; dtphi1=y(2,:)';
%phi2=y(3,:)'; dtphi2=y(4,:)';
%l1=ivp(8); l2=ivp(9);
% phi1=x(:,1); dtphi1=x(:,2);
% phi2=x(:,3); dtphi2=x(:,4);
% l1=ivp(8); l2=ivp(9);

%h=plot(0,0);
theta = linspace(-pi,pi,200);
xc = cos(theta);
yc = -sin(theta);
plot(xc,yc)
hold on
h = plot(cos(q(1,:)),sin(q(1,:)),'or');

axis([-1.1,1.1,-1.1,1.1]); %equal
axis square;
hold off;
set(gcf,'renderer','zbuffer'); 
set(gca,'nextplot','replacechildren');
v = VideoWriter('test.avi');
open(v);

    for i=1:plotSlice:length(t)-1
        if (ishandle(h)==1)
            
            Xcoord=cos(q(i,:));
            Ycoord=sin(q(i,:));
            set(h,'XData',Xcoord,'YData',Ycoord);
            drawnow;
            frame = getframe;
            writeVideo(v,frame);
            if movie==false
                pause(t(i+1)-t(i));
            end
            
        end
        
    end

    close(v);
