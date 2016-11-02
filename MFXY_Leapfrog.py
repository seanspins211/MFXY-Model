# 2nd order Leapfrog method on MFXY
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


speedFactor=100 #speeds up animation
dt  = 0.0001 #step size
T   = 100.0 #time interval length
N   = 100 #number of particles
e   = 1.0
pi = np.pi

#initial positions on unit cirle
q_array=np.zeros((int(T/dt),N))
q_array[0,:]=2*pi*np.random.rand(N)-pi #random initial values.
#print q_array
p_array=np.zeros((int(T/dt),N)) #set all ICs to zero.
# momentum is conserved, sum of p always zero.
#p_array[0,:]=2*pi*np.random.rand(3)-pi #random initial values.




t = np.arange(0,T,dt)

y = np.ones(N) #needed to broadcast in for loop

for i in range(len(t)-1):
    '''
    p1 = p0 #can remove for speed
    p2 = p1 - dt*e/N*sums
    q1 = q0 + dt*0.5*p1
    q2 = q1 + dt*0.5*p2
    '''
    q1 = q_array[i,:]+ 0.5*dt*p_array[i,:]

    xx = q1.reshape(N,1)


    AT = (xx + y)
    A  =  np.transpose(xx+y)
    sines = np.sin(AT-A)
    sums  = np.sum(sines,axis=1)

    p_array[i+1,:] = p_array[i,:] - e/N*dt*sums
    q_array[i+1,:] = q1 + dt*0.5*p_array[i+1,:]











    #phases = ( phases + np.pi) % (2 * np.pi ) - np.pi


fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1.5, 1.5), ylim=(-1.5, 1.5),aspect='equal')
ax.grid()

line, = ax.plot([], [], 'o', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    #line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = np.cos(q_array[i*speedFactor,:])
    thisy = np.sin(q_array[i*speedFactor,:])


    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*speedFactor*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(t)/speedFactor),
                              interval=25, blit=False, init_func=init)

#ani.save('MFXY_FEuler.mp4', fps=100)
plt.show()

'''
plt.plot(np.cos(q1),np.sin(q1),color='b',marker='o')
#plt.plot(q2,v2)
#plt.plot(q3,v3)
plt.show()

plt.plot(q1,v1)
plt.plot(q2,v2)
plt.plot(q3,v3)
plt.show()
#plt.plot(t,E)
#plt.show()
'''
