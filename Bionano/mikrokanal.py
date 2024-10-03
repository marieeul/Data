# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 08:22:21 2021

@author: Bruker
"""

import csv
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.optimize import curve_fit


# Konstanter
pix_til_m = (500/210)*10**(-6) #kan også bruke 2.25um/px, dette er 2.38um/px
l = 75*10**(-6) #Tykkelsen på kanalen i m, hvor langt lyset beveger seg i væsken
v = 40*10**(3)/(500*75*60)  #fart i m/s
temp = 292 # Temperatur på nanolab i kelvin, 19 grader C
eta = 0.001 #Viskositeten til vann ved 20 grader C i Pa*s
k_B = 1.380649*10**(-23) #Boltzmann konstant, m2 kg s-2 K-1
epsilon = 8 #m^3/mol m

S_E = k_B*temp/(6*math.pi*eta) #innsatte verdier i Stokes-Einstein equation

#Strekning fra kanalene møtes til linjene hvor intensiteten er målt
s1 = (298.0419+126)*pix_til_m 
s2 = s1+218.1857*pix_til_m
s3 = s2 + 281.0640*pix_til_m
s4 = s3 + 183.1338*pix_til_m

t1 = s1/v
t2 = s2/v
t3 = s3/v
t4 = s4/v


def opne_og_lese_til_liste(navn):
    listen = [] #intensitet
    x = [] #hvor jeg er på tvers av kanalen

    with open(navn, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for lines in csv_reader:
            f=float(lines[1])
            l=int(lines[0])
            x.append(l*pix_til_m)
            listen.append(f)
            
    return listen, x

def lag_plot(data, x_data, fitted_data, xaxes, yaxes, titles): 
    f,a = plt.subplots(4,1)
    a = a.ravel()
    ny_x = [i*10**(6) for i in x_data]
    for idx,ax in enumerate(a):
        ax.plot(ny_x, fitted_data[idx], color='magenta', label='Fitted curve')
        ax.scatter(ny_x, data[idx], s=3, label='Our data')
        ax.set_title(titles[idx])
        ax.set_xlabel(xaxes[idx])
        ax.set_ylabel(yaxes[idx])
        ax.legend()
    f.suptitle('Concentration profiles')
    f.set_figheight(12)
    
    plt.tight_layout() 
    
def regn_absorbans(liste):
    A = [math.log10(I_0/i) for i in liste]
    return A

def regn_konsentrasjon(liste):
    c = [i/(epsilon*l) for i in liste]
    # print(c)
    return c    



def normalisering(c):
    mini = gjennomsnitt(c[-50:])
    maks = gjennomsnitt(c[:50])
    norm = [(i-mini)/(maks-mini) for i in c]
    return norm

def C0(liste):
    c_final = sum(liste[150:])/len(liste[150:])
    c_initial = sum(liste[1:50])/len(liste[1:50])
    c_0 =  c_initial - c_final
    return c_0

def gjennomsnitt(liste):
    snitt = sum(liste)/len(liste)
    return snitt



def c(x, Dt, x_shift, c_0):
        return c_0/2 + c_0/2*erf(-(x-x_shift)/(2*(Dt)**0.5))

def curve_fitting(c_data, x_data, t0):
    popt, cvar = curve_fit(c, x_data, c_data)
    Dt = popt[0]
    return Dt/t0, Dt, popt[1], popt[2], cvar

def hydro_radius(D):
    r = S_E/D
    return r


def standardavvik(liste):
    a = []
    snitt = sum(liste)/len(liste)
    for i in liste:
        a.append((i-snitt)**2)
    st = math.sqrt(sum(a)/len(liste))
    return st
    
linje0, x0 = opne_og_lese_til_liste("linje0.csv")
linje1, x1 = opne_og_lese_til_liste("linje1.csv")
linje2, x2 = opne_og_lese_til_liste("linje2.csv")
linje3, x3 = opne_og_lese_til_liste("linje3.csv")
linje4, x4 = opne_og_lese_til_liste("linje4.csv")



    
I_0 = sum(linje0[225:412])/len(linje0[225:412])


A1 = regn_absorbans(linje1[3:200])
A2 = regn_absorbans(linje2[3:200])
A3 = regn_absorbans(linje3[3:200])
A4 = regn_absorbans(linje4[3:200])
A0 = regn_absorbans(linje0[103:300])

c1 = regn_konsentrasjon(A1)
c2 = regn_konsentrasjon(A2)
c3 = regn_konsentrasjon(A3)
c4 = regn_konsentrasjon(A4)
c0 = regn_konsentrasjon(A0)



c0_norm = normalisering(c0)
c1_norm = normalisering(c1)
c2_norm = normalisering(c2)
c3_norm = normalisering(c3)
c4_norm = normalisering(c4)



D1, Dt1, x_shift1, c_01, covar1 = curve_fitting(c1_norm, x1[:197], t1)
D2, Dt2, x_shift2, c_02, covar2 = curve_fitting(c2_norm, x2[:197], t2)
D3, Dt3, x_shift3, c_03, covar3 = curve_fitting(c3_norm, x3[:197], t3)
D4, Dt4, x_shift4, c_04, covar4 = curve_fitting(c4_norm, x4[:197], t4)

r1 = hydro_radius(D1)
r2 = hydro_radius(D2)
r3 = hydro_radius(D3)
r4 = hydro_radius(D4)

perr1 = np.sqrt(np.diag(covar1))
perr2 = np.sqrt(np.diag(covar2))
perr3 = np.sqrt(np.diag(covar3))
perr4 = np.sqrt(np.diag(covar4))

print('Diffusjons konstant')
print('Line 1 & ',D1, ' $\pm \ ', perr1[0]/t1, '$ \\')
print('Line 2 & ',D2, ' $\pm \ ', perr2[0]/t2, '$ \\')
print('Line 3 & ',D3, ' $\pm \ ', perr3[0]/t3, '$ \\')
print('Line 4 & ',D4, ' $\pm \ ', perr4[0]/t4, '$ \\')
print('Totalt &', gjennomsnitt([D1, D2, D3, D4]), '$\pm \ ', standardavvik([D1, D2, D3, D4]))

print('Hydrodynamic radius')
print('Line 1 & ',r1, ' $\pm \ ', standardavvik([r1, hydro_radius(D1+perr1[0]/t1), hydro_radius(D1-perr1[0]/t1)]), '$ \\')
print('Line 2 & ',r2, ' $\pm \ ', standardavvik([r2, hydro_radius(D2+perr2[0]/t2), hydro_radius(D2-perr2[0]/t2)]), '$ \\')
print('Line 3 & ',r3, ' $\pm \ ', standardavvik([r3, hydro_radius(D3+perr3[0]/t3), hydro_radius(D3-perr3[0]/t3)]), '$ \\')
print('Line 4 & ',r4, ' $\pm \ ', standardavvik([r4, hydro_radius(D4+perr4[0]/t4), hydro_radius(D4-perr4[0]/t4)]), '$ \\')
print('Totalt &', gjennomsnitt([r1, r2, r3, r4]), '$\pm \ ', standardavvik([r1, r2, r3, r4]), '$ \\')




xaxes = ['Distance [\u03bcm]','Distance [\u03bcm]','Distance [\u03bcm]','Distance [\u03bcm]'] #husk å gjøre om til meter
yaxes = ['Concentration','Concentration', 'Concentration', 'Concentration']
titles = ['Line 1','Line 2','Line 3','Line 4'] 


lag_plot([c1_norm, c2_norm, c3_norm, c4_norm], x1[:197], [[c(z, Dt1, x_shift1, c_01) for z in x1[:197]], [c(z, Dt2, x_shift2, c_02) for z in x1[:197]], [c(z, Dt3, x_shift3, c_03) for z in x1[:197]], [c(z, Dt4, x_shift4, c_04) for z in x1[:197]]],xaxes, yaxes, titles)

