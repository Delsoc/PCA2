#EFORRLSA (Moeller, 2002)
#Interlocking of learning and orthonormalization in RRLSA

import numpy as np
import math
from copy import deepcopy

def eforrlsa(units):

    #Anlegen der lokalen Variablen
    V = deepcopy(units.weight)
    EFO_L2 = np.zeros((units.outdimension, 1))
    EFO_p  = np.zeros((units.outdimension, 1))
    EFO_q = np.zeros((units.outdimension, units.outdimension))
    EFO_r = np.zeros((units.outdimension, units.outdimension))

    #Algorithmus Gleichungn 3-12
    for i in range(0,units.outdimension): #Notiz : wenn units.outdimension = 2 , dann i = 0 & 1

        ''' Hilfsvariablen
            alpha * Eigenwert
            Anderes Alpha als im Hauptalgo. Dieses Alpha läuft gegen 1 während
            EFO_d = np.dot(units.x_c.T,units.x_c)
        else:
            EFO_t = EFO_t + EFO_p[i-1] * EFO_p[i-1]
            das normale alpha gegen 0 läuft. Deshalb hier 1-alpha
        '''
        helperVariable1 = (1 - units.alpha) * units.eigenvalue[i]

        #beta * Output
        #gleicher Verlauf wie Alpha aus Hauptalgorithmus
        helperVariable2 = units.alpha * units.y[i]


        #Init und update von t und d nach Gleichung 5+6
        if i==0:
            EFO_t = 0
            EFO_d = np.dot(units.x_c.T,units.x_c)
        else:
            EFO_t = EFO_t + EFO_p[i-1] * EFO_p[i-1]
            EFO_d = EFO_d - units.y[i-1] * units.y[i-1]
            if EFO_d < 0:
                EFO_d = 0
        #Gleichung 7
        EFO_s = (helperVariable1 + units.alpha * EFO_d) * units.y[i]

        #Gleichung 8
        EFO_L2[i] = helperVariable1 * helperVariable1 + helperVariable2 * (helperVariable1 * units.y[i] + EFO_s)

        #Gleichung 9
        EFO_n2 = EFO_L2[i] - EFO_s * EFO_s * EFO_t

        #ensure that EFO_n2 > 0
        '''Fragen: ist bei matlab nicht 1e-100 nicht schon LÄNGST wie 0?
            wofür Zeile 54/55?
        '''
        if EFO_n2 < 1e-100:
            EFO_n2 = 1e-100
        EFO_n = math.sqrt(EFO_n2)

        #Gleichung 12
        EFO_p[i] = (helperVariable2 - EFO_s * EFO_t) / EFO_n

        #Berechnung vom 2 additiven Termen in Gleichung 4 (siehe IndexBezeichnung)
        #Jede Zeile der Spalte i mit dem gleichen Ergebnis füllen:

        for j in range(len(units.weight[:,0])):
            units.weight[j, i] = EFO_p[i] * units.x_c[j]
        #units.weight[:, i] = EFO_p[i] * units.x_c
        #for j in range(len(units.weight[0])):
         #   units.weight[j, i] = EFO_p[i] * units.x_c

        for i2 in range(0,i+1):#hier im gegensatz zum Matlab-Code noch i+1m weil Python j bis i-1 laufen lässt, bei matlab nicht
                              #evtl. denkfehler
            #Gleichung 10+11
            if i2<i:
                EFO_r[i, i2] = EFO_r[i - 1, i2] + EFO_p[i - 1] * EFO_q[i - 1, i2]
                EFO_q[i, i2] = -(helperVariable2 * units.y[i2] + EFO_s * EFO_r[i, i2]) / EFO_n
            else:
                EFO_r[i, i2] = 0
                EFO_q[i, i2] = helperVariable1 / EFO_n
            #Gleichung 4
            units.weight[..., i] = units.weight[..., i] + (EFO_q[i, i2] * V[..., i2])

    units.eigenvalue = np.sqrt(EFO_L2)
        #hier Matlab-Code etwas verändern
    b= np.isreal(units.eigenvalue)
    real=0    #wenn b complex, dann real = .1 sonst real =0
    for k in range(0, len(b)):
        if b[k] == False:
            real = 1
    if real==1:
        units.eigenvalue = abs(units.eigenvalue)

    return units