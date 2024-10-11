from numpy import zeros
from random import choice, uniform
import matplotlib.pyplot as plt
from math import log, factorial

row = 100
col = 200
N = 50
Num_steps = 100000
Dump_interval = Num_steps/10 

# row = 20
# col = 20
# N = 5
# Num_steps = 1000
# Dump_interval = Num_steps/10       # should be around 1/10 of Num_steps, a bad choice (too frequent) can make the calculation very slow 

def Initialize(row,col,N):
    # Put all the particles on for example the left-hand side
    
    Positions_of_particles = []
    
    for col in range(col):
        for row in range(row):
            if N>0:
                Positions_of_particles.append((col, row))
                N -= 1
            else: break
    
    return Positions_of_particles

def Possible_transitions(Positions_of_particles):
    # Calculate the possible transitions from the positions
    Transitions = []
    for i in Positions_of_particles:
        col_i = i[0]
        row_i = i[1]
        if col_i<col-1 and (col_i+1, row_i) not in Positions_of_particles:
            Transitions.append((i,(col_i+1, row_i)))
        if col_i>0 and (col_i-1, row_i) not in Positions_of_particles:
            Transitions.append((i,(col_i-1, row_i)))
        if row_i<row-1 and (col_i, row_i+1) not in Positions_of_particles:
            Transitions.append((i, (col_i, row_i+1)))
        if row_i>0 and (col_i, row_i-1) not in Positions_of_particles:
            Transitions.append((i, (col_i, row_i-1)))
    # print(Transitions)
    return Transitions

def Perform_Transition(Positions_of_particles, Transitions):
    # Choose a random transition and update the positions
    Chosen_transition = choice(Transitions)
    Positions_of_particles.remove(Chosen_transition[0])
    Positions_of_particles.append(Chosen_transition[1])

    return Positions_of_particles

def Entropy_calc(Positions_of_particles, N):
    # use the min and max functions to obtain "Lattice_spread" 
    min_col = min(i[0] for i in Positions_of_particles)-1
    min_row = min(i[1] for i in Positions_of_particles)-1
    max_col = max(i[0] for i in Positions_of_particles)
    max_row = max(i[1] for i in Positions_of_particles)
    
    Lattice_spread = (max_col-min_col)*(max_row-min_row)
    # print(Lattice_spread)
    return log(factorial(Lattice_spread)/(factorial(N)*factorial(Lattice_spread - N)))

def Create_image(Positions_of_particles, TrNum): #TrNum keeps track of the step number in the loop. 
    #Create the array here
    Current_state = zeros([row, col], dtype=int)
    for i in Positions_of_particles:
        Current_state[i[1]][i[0]] = 1
    
    imgplot = plt.imshow(Current_state, cmap='binary')
    plt.savefig('Lattice' + str(TrNum) + '.png')

#Use the initialize function to create a list of all the particles positions
Positions_of_particles = Initialize(row, col, N)

#Set up the list with possible transitions
Transitions = Possible_transitions(Positions_of_particles)

#Remember to set up lists for the time stamp and the local entropy that can be updated inside the loop
Time_step = []
Local_Entropy = []
time = 0
#Start the loop. Both a for-loop and a while-loop will work.
for TrNum in range(1, Num_steps+1):
    #Update the positions lists using Perform_Transition()
    Positions_of_particles = Perform_Transition(Positions_of_particles, Transitions)
    
    #Calculate the present time: time += "KMC equation for time". Note that the time is updated in every step but only stored when the entropy is stored
    time += -log(uniform(0, 1))/len(Transitions)
    
    #Recalculate the possible transitions (too complex to update, just recalculate from scratch
    Transitions = Possible_transitions(Positions_of_particles)
    
    if TrNum % Dump_interval == 0:
        #Remember to store an image at a regular interval. Use for example: if TrNum % Dump_interval == 0:
        Create_image(Positions_of_particles, TrNum)
        
        #Update the entropy and time stamp lists, also at a regular interval. Make sure that the time step list reflects the total time passed at any given point.
        Time_step.append(time)
        Local_Entropy.append(Entropy_calc(Positions_of_particles, N))
    #If using a while-loop, update TrNum

#The code below creates the plots the local entropy as a function of time.
plt.clf()
plt.plot(Time_step, Local_Entropy)
plt.show()
