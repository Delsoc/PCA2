from copy import deepcopy

from setuptools.command.easy_install import easy_install

import eforrlsa
import numpy as np


def unit_adaption(parameter, units):
    units.alpha = (parameter.epsilon_init - parameter.epsilon_final) * units.Dt ** parameter.phi + parameter.epsilon_final

    # Update the center of a unit, Eq. (3.8) Schenck dissertation (Neural Gas Step)
    units.center = units.center + units.alpha * units.x_c

    units= eforrlsa.eforrlsa(units)
    # sortEigenvalues
    # (getestet, sortiert absteigend)
    units.eigenvalue[:] = units.eigenvalue[::-1]

    units.variance = sum(units.eigenvalue)

    if (parameter.columns != units.outdimension):
        units.sigma = units.sigma + units.alpha * (
                    np.dot(units.x_c.T, units.x_c) - np.dot(units.y.T, units.y) - units.sigma)
        if (units.sigma < 0):
            units.sigma = parameter.logArgMinLimit
        units.totalVariance = units.variance + units.sigma
    else:
        units.totalVariance = units.variance

    # update internal unit state for adaptive learning rate control
    units.Dt = 0.0
    a_lowpass = parameter.mu
    for i in range(0, units.outdimension):  # Notiz : wenn units.outdimension = 2 , dann i = 0 & 1
        units.mt[i] = units.mt[i] * (1 - a_lowpass) + units.y[i] * units.y[i] / units.eigenvalue[i] * a_lowpass
        if (units.mt[i] > parameter.logArgMinLimit):
            amin = np.amin(abs(np.log(units.mt[i]) / parameter.log_precomp))
            if amin > 1:  # gleiche Funktionalität wie in matlab min(A,1.0) -> falls A größer als 1, dann return 1.0
                amin = 1.0
            units.Dt = units.Dt + amin
        else:
            units.Dt = units.Dt + 1.0
    units.Dt = units.Dt / units.outdimension

    return (parameter, units)
