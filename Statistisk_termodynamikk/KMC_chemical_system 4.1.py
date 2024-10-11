from random import uniform #will be used to pick random numbers between 0 and 1
from math import log
import matplotlib.pyplot as plt #Will be used to create the relevant plots


#Part 1
N_a = 1000 #Number of particles of type A
N_b = 1000 #Number of particles of type B
N_c = 0 #Number of particles of type C

k_f = 1 #Kinetic forward constant
k_r = 1 #Kinetic reverse constant



def Probability_forward(k_f, k_r, N_a, N_b, N_c): #To simplify later on. Calculates the probability of a forward transition. NOTE: the reverse probability is 1 - forward.
    return k_f*N_a*N_b/(k_f*N_a*N_b+k_r*N_c) #Use equation 2 in the pdf


#Part 2
Num_trans = 0 #Sets up transition counter
equilibrium = False #Sets up equilibrium check
N_a_time = [N_a] #Sets up vector describing number of A particles
N_b_time = [N_b] #Sets up vector describing number of B particles
N_c_time = [N_c] #Sets up vector describing number of C particles
Time_step = [0] #Sets up vector describing the time passed after each transitions

while not equilibrium:
    
    P_f = Probability_forward(k_f, k_r, N_a, N_b, N_c)
    P_r = 1 - P_f
    rho = uniform(0, 1)

    if P_f > rho: #Use uniform(0,1) (generates random number) to select either forward or reverse reaction
        #Update the particle counts according to the reaction equation
        N_a -= 1
        N_b -= 1
        N_c += 1
        
    else: #If the random number is higher than forward probability, the reverse transition is picked
        #Update the particle counts according to the reaction equation
        N_a += 1
        N_b += 1
        N_c -= 1

    #Remember to update your parameters as the simulation runs, for plotting.
    Num_trans += 1
    N_a_time.append(N_a)
    N_b_time.append(N_b)
    N_c_time.append(N_c)
    Time_step.append(Time_step[-1]-log(rho)/(k_f*N_a*N_b+k_r*N_c))

    #Remember to add an equilibrium condition to change equilibrium from False to True if equilibrium has been reached.
    # if P_f < 0.5 or Num_trans == 10000:
    #     equilibrium = True
    
    if Num_trans == 1500:
         equilibrium = True
    #k_r*N_c == k_f*N_a*N_b
        
    
    


#Part 3
#Show plot of number of each particle as a function of time. plt.plot(x-axis, y-axis, color)
plt.plot( Time_step, N_a_time , 'r')
plt.plot(Time_step, N_b_time, 'b')
plt.plot(Time_step, N_c_time , 'g')
plt.show()

