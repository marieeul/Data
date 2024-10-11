import numpy as np
import itertools as it
import matplotlib.pyplot as plt
import pickle

def Lattice_shape(N): #The function determines the lattice shapes that you will be using in this exercise, given N particles.
    if N == 4:
        return (2,2)
    elif N == 6:
        return (2,3)
    elif N == 8:
        return (2,4)
    elif N == 12:
        return (3,4)
    elif N == 16:
        return (4,4)
    elif N == 20:
        return (5,4)
    elif N == 24:
        return (6,4)


def Count_AB(Lattice):
    m_AB = 0        #Should take an array, representing the lattice, and find the number of AB-interactions. Use PERIODIC BOUNDARY conditions!
#    print(Lattice)
#    print(m_AB)
#    print(len(Lattice[0]))  

    for row in range(len(Lattice)):
        for i in range(len(Lattice[row])):
            if i != len(Lattice[row])-1:
    #            print("print")
                if Lattice[row][i] != Lattice[row][i+1]:
                    m_AB += 1
            if row != len(Lattice)-1:
                if Lattice[row][i] != Lattice[row+1][i]:
        #            print("hei")
                    m_AB += 1
                    
#    for row in range(len(Lattice)):
#        for i in range(len(Lattice[row])):
#            if i <= len(Lattice[row])-2:
#    #            print("print")
#                if Lattice[row][i] != Lattice[row][i+1]:
#                    m_AB += 1
#            elif i == len(Lattice[row])-1:
#                if Lattice[row][i] != Lattice[row][0]:
#                    m_AB+= 1
#            if row <= len(Lattice)-2:
#                if Lattice[row][i] != Lattice[row+1][i]:
#        #            print("hei")
#                    m_AB += 1
#            elif row == len(Lattice)-1:
#                if Lattice[row][i] != Lattice[0][i]:
#                    m_AB+= 1
        
    return m_AB


def Create_arrays_and_count(Number_of_particles):
    m_AB = []#A list that keeps track of the number of AB-interactions for each configuration.
    
            
    for config in it.product('AB', repeat=Number_of_particles):  #Use itertools.product() to generate all possible unique lattice configurations.
#        print(config)
        N_A = 0 #itertools returns all unique combinations, including thos with N_A not = N_B. Select those lists where N_A = N_B
        for i in config:
            if i=='A':
                N_A += 1
#        print(N_A)
        if N_A == Number_of_particles-N_A:
#            print("heheh")
        
        
            Lattice=np.array(config)     #itertools returns a list so you will have to convert the list to an array below.
            ny_lattice = np.reshape(Lattice, Lattice_shape(Number_of_particles))
            m_AB.append(Count_AB(ny_lattice))#should append the result of calling Count_AB(Lattice) on a given configuration config
#            print(ny_lattice)
    return m_AB


liste = [4, 6, 8, 12, 16, 20, 24]
#liste = [4, 6, 8, 12]
for i in liste: #You will be calculating the density of states for the given system sizes
    m_AB = Create_arrays_and_count(i) #Call the correct function to create a list of all possible configuration AB-interactions
#    print(m_AB)
    Available_microstates = list(set(m_AB)) #Finds all uniqe macrostates
#    print(Available_microstates)
    Available_microstates.sort() #Sorts this list in ascending order, for plotting purposes.
    m_AB_degeneracy = [m_AB.count(i) for i in Available_microstates] #For each macrostate, this list should return the degeneracy. Use list_comprehension and list.count()
    
    #Creates a bar chart of density of states: x-axis = microstate, y-axis = degeneracy
    y_pos = np.arange(len(Available_microstates))
    plt.bar(y_pos, m_AB_degeneracy)
    plt.xticks(y_pos, Available_microstates, fontsize=7, rotation=30)
    plt.savefig('Density_of_states' + str(i))
    plt.clf()

    #To compare the variance of density of states as system size increases, you must normalize the interaction energies (number of AB-interactions)
    Normalization_factor = Available_microstates[-1] #The normalization factor should be the highest possible number of AB-interactions for a given system size
    Normalized_mAB = [i/Normalization_factor for i in m_AB] #Create a normalized version of m_AB by deviding each instance by the Normalization_factor
    print(np.var(Normalized_mAB)) #Calculate and print the variance of Normalized_mAB. Use np.var().


#Saves m_AB and i for future use for system size = i_max (in this case 24)
with open('m_AB.pkl', 'wb') as f:
    pickle.dump([m_AB,i], f)