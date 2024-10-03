# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:39:30 2021

@author: Bruker
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
import math

t = 0.133   #tiden mellom hvert bilde/frame
temp = 292 # Temperatur på nanolab i kelvin, 19 grader C
eta = 0.001 #Viskositeten til vann ved 20 grader C i Pa*s
k_B = 1.380649*10**(-23) #Boltzmann konstant

S_E = k_B*temp/(6*math.pi*eta) #satte verdier i Stokes-Einstein equation



def diffusjon_og_radius(arr):          # regner it diffusjons konstant og hydrodynamisk radius og returnerer dem i hver sin liste.
    sortert = arr[arr[:,0].argsort()] #Sorterer listene etter lengden på trackingen

    x = np.argwhere(sortert == 10) #Finner indeksene til track med lengde 10 og lagrer som array
    x1 = x[0][0]  #Lagrer indeksen til første track med 10 i lengde

    riktige = np.delete(sortert, np.s_[0:x1], axis=0 ) #Sletter alle track som er kortere enn x1=10.


    diffusion = []
    radius = []

    for x in range(len(riktige)):
        diffusjon_konstant = (riktige[x,1])**2/(4*t) #regner ut diffusjons konstanten
        diffusion.append(diffusjon_konstant)    #Legger til utregnet verdi til listen
        radius.append(S_E/diffusjon_konstant)
        
    return diffusion, radius

def gange(liste, potens):
    my_new_list = [i * 10**potens for i in liste]
    return my_new_list

def gange_og_sette_sammen(l1,l2,l3, potens):
    L1 = gange(l1, potens)
    L2 = gange(l2, potens)
    L3 = gange(l3, potens)
    dataen = [L1, L2, L3, L1+L2+L3]
    return dataen


def lag_diffplot(data, xaxes, yaxes, titles):
    f,a = plt.subplots(2,2)
    a = a.ravel()
    for idx,ax in enumerate(a):
        ax.hist(data[idx], range=[0.1*10**(-2), 1], color='magenta', edgecolor='black')
        ax.set_title(titles[idx])
        ax.set_xlabel(xaxes[idx])
        ax.set_ylabel(yaxes[idx])
        
    f.suptitle('Histograms of diffusion constants')
    plt.tight_layout() 
    
    
def lag_radplot(data, xaxes, yaxes, titles):
    f,a = plt.subplots(2,2)
    a = a.ravel()
    for idx,ax in enumerate(a):
        ax.hist(data[idx], range=[0.1*10**(-1), 0.35*10], color='magenta', edgecolor='black')
        ax.set_title(titles[idx])
        ax.set_xlabel(xaxes[idx])
        ax.set_ylabel(yaxes[idx])
    f.suptitle('Histograms of hydrodynamic radius')
    plt.tight_layout() 
    
    
def gjennomsnitt(liste):
    snitt = sum(liste)/len(liste)
    return snitt
        
def standardavvik(liste, snitt):
    a = []
    for i in liste:
        a.append((i-snitt)**2)
    st = math.sqrt(sum(a)/len(liste))
    return st

arr1 = np.array([[1,1]])

with open("MSD_40x_PC_SB_particles_1_forsok3.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for lines in csv_reader:
        listen = []
        f=float(lines[-7])
        l=int(lines[2])
        listen.append(l)
        listen.append(f)
        arr1 = np.append(arr1, [listen], axis=0)
        
      
diff1, rad1 = diffusjon_og_radius(arr1)

arr2 = np.array([[1,1]])

with open("results_40x_PC_SB_particles_2.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for lines in csv_reader:
        listen = []
        f=float(lines[-7])
        l=int(lines[2])
        listen.append(l)
        listen.append(f)
        arr2 = np.append(arr2, [listen], axis=0)

diff2, rad2 = diffusjon_og_radius(arr2)

arr3 = np.array([[1,1]])

with open("results_40x_PC_SB_particles_3.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for lines in csv_reader:
        listen = []
        f=float(lines[-7])
        l=int(lines[2])
        listen.append(l)
        listen.append(f)
        arr3 = np.append(arr3, [listen], axis=0)
        
diff3, rad3 = diffusjon_og_radius(arr3)  



diffdata = gange_og_sette_sammen(diff1, diff2, diff3, 12)

xaxes = ['Diffusion constant [\u03bcm^2/s]','Diffusion constant [\u03bcm^2/s]','Diffusion constant [\u03bcm^2/s]','Diffusion constant [\u03bcm^2/s]']
yaxes = ['Frequency','Frequency', 'Frequency', 'Frequency']
titles = ['Sample A1','Sample A2','Sample A3','Sample A'] 

radiusdata = gange_og_sette_sammen(rad1, rad2, rad3, 6)

rxaxes = ['Hydrodynamic radius [\u03bcm]','Hydrodynamic radius [\u03bcm]','Hydrodynamic radius [\u03bcm]','Hydrodynamic radius [\u03bcm]']
ryaxes = ['Frequency','Frequency', 'Frequency', 'Frequency']
rtitles = ['Sample B1','Sample B2','Sample B3','Sample B'] 


lag_diffplot(diffdata, xaxes, yaxes, titles)
lag_radplot(radiusdata, rxaxes, ryaxes, rtitles)

print('Diffusjons konstant:')
n=1
for liste in diffdata:
    snitt = gjennomsnitt(liste)
    print('B',n,' & ',snitt, ' $\pm \ ', standardavvik(liste, snitt), '$ \\' )
    print(len(liste))
    n+=1
    #print(liste)
    #print('hei')

print('Radius:')    
n=1
for liste in radiusdata:
    snitt = gjennomsnitt(liste)
    print('B',n,' & ',snitt, ' $\pm \ ', standardavvik(liste, snitt), '$ \\' )
    n+=1

print(S_E)
