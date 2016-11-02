# Forward Euler
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


dt  = 0.0005
N   = 3.0
e   = 1.0
pi = np.pi

#initial positions on unit cirle
q1_n  = 0.
q2_n  = 2.
q3_n  = -2.
#initial momenta
v1_n  = 0.
v2_n  = 0.
v3_n  = 0.

#E_0 = (v_n**2/2) + q_n**(-12)-2*q_n**(-6)

t = np.arange(0,1,dt)
q1 = np.zeros_like(t)
q2 = np.zeros_like(t)
q3 = np.zeros_like(t)
v1 = np.zeros_like(t)
v2 = np.zeros_like(t)
v3 = np.zeros_like(t)
#E = np.zeros_like(t)

q1[0] = q1_n
q2[0] = q2_n
q3[0] = q3_n
v1[0] = v1_n
v2[0] = v2_n
v3[0] = v3_n
#E[0] = 0

for i in range(len(t)-1):

    q1_np1  = q1_n + dt*v1_n
    v1_np1  = v1_n - dt*e/N*(np.sin(q1_n-q2_n)+np.sin(q1_n-q3_n))
    q1_n    = q1_np1
    v1_n    = v1_np1

    q2_np1  = q2_n + dt*v2_n
    v2_np1  = v2_n - dt*e/N*(np.sin(q2_n-q1_n)+np.sin(q2_n-q3_n))
    q2_n    = q2_np1
    v2_n    = v2_np1

    q3_np1  = q3_n + dt*v3_n
    v3_np1  = v3_n - dt*e/N*(np.sin(q3_n-q1_n)+np.sin(q3_n-q2_n))
    q3_n    = q3_np1
    v3_n    = v3_np1


    #phases = ( phases + np.pi) % (2 * np.pi ) - np.pi
    q1[i+1] = q1_n
    v1[i+1] = v1_n
    q2[i+1] = q2_n
    v2[i+1] = v2_n
    q3[i+1] = q3_n
    v3[i+1] = v3_n

    #E[i+1] = (E_0-((v_n**2)/2 + q_n**(-12)-2*q_n**(-6)))/E_0


fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

line, = ax.plot([], [], 'o', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    #line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [ np.cos(q1[i]), np.cos(q2[i]), np.cos(q3[i])]
    thisy = [ np.sin(q1[i]), np.sin(q2[i]), np.sin(q3[i])]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(q1)),
                              interval=25, blit=False, init_func=init)

ani.save('MFXY_FEuler.mp4', fps=15)
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
