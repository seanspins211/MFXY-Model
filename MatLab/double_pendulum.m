function double_pendulum(q, timeArray, plotSlice)
%clear All; clf;

t = timeArray;
% plot circle
theta = linspace(-pi,pi,200);
xc = cos(theta);
yc = -sin(theta);
plot(xc,yc)
% place first set of points on circle
hold on
h = plot(cos(q(1,:)),sin(q(1,:)),'or');

axis([-1.1,1.1,-1.1,1.1]); %equal
axis square;
hold off;
set(gcf,'renderer','zbuffer'); 
set(gca,'nextplot','replacechildren');


    for i=1:plotSlice:length(t)-1
        if (ishandle(h)==1)
            
            Xcoord=cos(q(i,:));
            Ycoord=sin(q(i,:));
            set(h,'XData',Xcoord,'YData',Ycoord);
            drawnow;
                              
        end
        
    end


