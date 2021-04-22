from copy import deepcopy
import math
import numpy as np
from scipy.linalg import orth
from tables import parameters


def Find(liste, units, p):
    for i in range(len(liste)):
        if (liste[i] > units.totalVariance * p.dimThreshold):
            return i
    return 0


def UnitSpecificDimensionLineFitting(parameter, units):
    if (units.variance < units.totalVariance * parameter.dimThreshold):
        # Add n Dimensions
        # Transform eigenvalues into log scale
        logEigenvalues = np.log(units.eigenvalue)


        x = np.zeros((units.outdimension, 1))
        for i in range(0, units.outdimension):
            x[i] = i+1

        x=x.flatten()
        logEigenvalues1D=logEigenvalues.flatten()


        pp = np.polyfit(x, logEigenvalues1D, 1)
        p = np.poly1d(pp)
        x1 = np.arange(max(x)+1, parameter.columns + 1).T
        approximatedEigenvaluesLog = p(1) * x1 + p(2)

        # Transform back into normal scale
        approximatedEigenvalues = np.zeros((len(approximatedEigenvaluesLog), 1))
        #approximatedEigenvalues = math.exp(approximatedEigenvaluesLog)
        for i in range(len(approximatedEigenvaluesLog)):
            approximatedEigenvalues[i] = math.exp(approximatedEigenvaluesLog[i])

        addedDim = Find(np.cumsum(abs(approximatedEigenvalues)) + units.variance, units, parameter)
        # Zeile 23/24 vom matlab code nicht nötig, weil ich in function Find index auf den ersten Index (bei Python aber 0) gesetzt habe
        if units.variance + sum(abs(approximatedEigenvalues)) < units.totalVariance * parameter.dimThreshold:
            addedDim = 1  # HIER im ggs zu Matlab gleich 0 und nicht 1, aber kann sein dass 1 bei 1 anfangen sollte und dann -1 immer gemacht wird wegen überlauf
        if addedDim + units.outdimension > parameter.columns:
            addedDim = parameter.columns - units.outdimension

        #hilfsvariablen
        #test2 = np.random.rand(parameter.columns, 1) #hier eig nicht 1 , sondern addedDim
        #test3 = orth(np.random.rand(parameter.columns, addedDim))
        if addedDim == 0:
            randOrth = np.random.rand(parameter.columns, 1)
        else:
            randOrth = orth(np.random.rand(parameter.columns, addedDim))

        units.weight = np.hstack((units.weight, randOrth))


        #units.eigenvalue = (units.eigenvalue).append(approximatedEigenvalues[addedDim])
        if addedDim == 0:
            appendApproximatedEigenvalues = approximatedEigenvalues[addedDim]
        else:
            appendApproximatedEigenvalues = np.zeros((addedDim, 1))
            for i in range(0,addedDim+1):
                appendApproximatedEigenvalues = np.append(appendApproximatedEigenvalues, approximatedEigenvalues[i])

        units.eigenvalue = np.append(units.eigenvalue, appendApproximatedEigenvalues)
        size = len(units.eigenvalue)
        units.eigenvalue = np.reshape(units.eigenvalue, (size, 1))

        units.outdimension = units.outdimension + addedDim #addedDim nochmal genauer angucken
        units.realDim = units.outdimension
        units.y = np.zeros((units.outdimension, 1))
        ZeroElement = np.array([0])
        for i in range(addedDim+2): #addedDim wahrscheinlich überarbeiten
            units.mt = np.append(units.mt, ZeroElement)
        units.gy = np.zeros((units.outdimension, 1))
        units.protect = 10
        print('%s %d' % ("Dimension: ", units.outdimension))
    else:
        if sum(units.eigenvalue[:len(units.eigenvalue) - 1]) > (units.totalVariance * parameter.dimThreshold):
            # Remove 1 Dimension
            if units.outdimension > 2:
                units.outdimension = units.outdimension - 1
                units.weight = np.delete(units.weight, len(units.weight), 1)
                units.eigenvalue = units.eigenvalue[:-1]
                units.y = units.y[:-1]
                units.mt = units.mt[:-1]
                units.gt = units.gt[:-1]
                units.protect = 10
                print('%s %d' % ("Dimension: ", units.outdimension))
        # else:
        # Do Nothing
        # In thise case the recent amount of Dimensions is above the Threshold
        # but removing the last Dimension would cause a drop below the Threshold again!
    if units.realDim == 1:
        units.suggestedOutdimension = 1
    else:
        units.suggestedOutdimension = units.outdimension
    return (parameter, units)
