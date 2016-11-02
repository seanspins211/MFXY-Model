# 2nd order Leapfrog method on MFXY
import numpy as np

def main(parameters = np.array([0.001,10.0,10,1.0])):
    dt ,T ,N ,e  = parameters
    N = int(N)




    #dt  = 0.001 #step size
    #T   = 100.0 #timenp interval length
    #N   = 10 #number of particles
    #e   = 1.0
    pi = np.pi

    a1 = 0.339839625839110000
    a2 =-0.088601336903027329
    a3 = 0.5858564768259621188
    a4 =-0.603039356536491888
    a5 = 0.3235807965546976394
    a6 = 0.4423637942197494587
    b1 = 0.1193900292875672758
    b2 = 0.6989273703824752308
    b3 =-0.1713123582716007754
    b4 = 0.4012695022513534480
    b5 = 0.0107050818482359840
    b6 = 0.0589796254980311632
    #initial positions on unit cirle
    q_array=np.zeros((int(T/dt),N))
    q_array[0,:]=2*pi*np.random.rand(N)-pi #random initial values.
    #print q_array
    p_array=np.zeros((int(T/dt),N)) #set all ICs to zero.
    # momentum is conserved, sum of p always zero.
    #p_array[0,:]=2*pi*np.random.rand(3)-pi #random initial values.
    def sums(q,N0):
        xx = q.reshape(N0,1)
        y = np.ones(N0)

        AT = (xx + y)
        A  =  np.transpose(xx+y)
        sines = np.sin(AT-A)
        sums  = np.sum(sines,axis=1)
        return sums


    t = np.arange(0,T,dt)

     #needed to broadcast in for loop

    for i in range(len(t)-1):
        '''
        p1 = p0 #can remove for speed
        p2 = p1 - dt*e/N*sums
        q1 = q0 + dt*0.5*p1
        q2 = q1 + dt*0.5*p2
        '''
        p0 = p_array[i,:]
        q0 = q_array[i,:]

        p1 = p0 - dt*b1*e/N*sums(q0,N)
        q1 = q0 + dt*a1*p1
        p2 = p1 - dt*b2*e/N*sums(q1,N)
        q2 = q1 + dt*a2*p2
        p3 = p2 - dt*b3*e/N*sums(q2,N)
        q3 = q2 + dt*a3*p3
        p4 = p3 - dt*b4*e/N*sums(q3,N)
        q4 = q3 + dt*a4*p4
        p5 = p4 - dt*b5*e/N*sums(q4,N)
        q5 = q4 + dt*a5*p5
        p6 = p5 - dt*b6*e/N*sums(q5,N)
        q6 = q5 + dt*a6*p6

        p_array[i+1,:] = p6
        q_array[i+1,:] = q6

    return q_array,p_array
para = np.array([0.001, 10.0,100,1.0])
np.savetxt("txtFiles/5orderOptimal_parameters_2.txt",para)
qa,pa = main(para)
np.savetxt("txtFiles/5orderOptimal_q_2.txt",qa)
np.savetxt("txtFiles/5orderOptimal_p_2.txt",pa)







    #phases = ( phases + np.pi) % (2 * np.pi ) - np.pi
