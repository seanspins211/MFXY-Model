import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



dt  = 0.0005 #step size
T   = 1.0 #time interval length
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

xx = q_array[0,:].reshape(N,1)
y = np.ones(N)

print (xx +y)
print np.transpose(xx+y)
sins=np.sin(xx+y-np.transpose(xx+y))
print sins
print np.sum(sins,axis=1)
