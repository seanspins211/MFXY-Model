# Forward Euler method on MFXY
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


speedFactor=100 #speeds up animation
dt  = 0.0005 #step size
T   = 100.0 #time interval length
N   = 3 #number of particles
e   = 1.0
pi = np.pi

#initial positions on unit cirle
q_array=np.zeros((int(T/dt),N))
q_array[0,:]=2*pi*np.random.rand(N)-pi #random initial values.
#print q_array
p_array=np.zeros((int(T/dt),N)) #set all ICs to zero.
# momentum is conserved, sum of p always zero.
#p_array[0,:]=2*pi*np.random.rand(3)-pi #random initial values.

#use to set values manually
#q_array[0,:]=np.array([0.,2.,-2.])


t = np.arange(0,T,dt)

y = np.ones(N) #needed to broadcast in for loop

for i in range(len(t)-1):
    q_array[i+1,:] = q_array[i,:] + dt*p_array[i,:]

    xx = q_array[i,:].reshape(N,1)


    AT = (xx +y)
    A  =  np.transpose(xx+y)
    sines = np.sin(AT-A)
    sums  = np.sum(sines,axis=1)
    '''
    for j in range(N):
        sinArray = -np.sin(q_array[i,:]-q_array[i,j])
        #print sinArray
    '''
    p_array[i+1,:] = p_array[i,:] - dt*e/N*sums




    #phases = ( phases + np.pi) % (2 * np.pi ) - np.pi

    #E[i+1] = (E_0-((v_n**2)/2 + q_n**(-12)-2*q_n**(-6)))/E_0


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
    #thisx = [ np.cos(q1[i]), np.cos(q2[i]), np.cos(q3[i])]
    #thisy = [ np.sin(q1[i]), np.sin(q2[i]), np.sin(q3[i])]

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
