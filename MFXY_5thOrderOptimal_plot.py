import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

speedFactor=100 #speeds up animation

q_array = np.loadtxt("txtFiles/5orderOptimal_q_2.txt")
p_array = np.loadtxt("txtFiles/5orderOptimal_p_2.txt")
parameters = np.loadtxt("txtFiles/5orderOptimal_parameters_2.txt")
dt ,T ,N ,e  = parameters
N = int(N)
t = np.arange(0,T,dt)
#print q_array[:5,:]

pSum = np.sum(p_array,axis=1)

plt.plot(t,pSum)
plt.show()

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

ani = animation.FuncAnimation(fig, animate, np.arange(1, q_array.shape[0]/speedFactor),
                              interval=25, blit=False, init_func=init)

#ani.save('MFXY_FEuler.mp4', fps=100)
plt.show()
