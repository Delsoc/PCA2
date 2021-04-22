import random
from copy import deepcopy
import numpy as np
import numpy.matlib


# rand=round(random.uniform(0.1, 1.0),4)
class units():
    def __init__(self, pm):
        # Protecs a Unit for n Iterations after the Dimension changed
        self.protect = 100

        # Unit specific Output Dimension
        self.outdimension = pm.StartDim
        self.suggestedOutdimension = pm.StartDim
        self.realDim = pm.StartDim

        # init centers by choosing N data points at random
        tempDataVec = deepcopy(pm.shape[0])  ##immer die erste Zeile, soll das random sein oder geht das so?
        for i in range(0, len(tempDataVec)):  ##im matlabcode wird zu jedem datensatz jeweils der gleiche center-vector erstellt
            tempDataVec[i] = tempDataVec[i] * round(random.uniform(0.1, 1.0), 4)
        centerHelp = np.array([tempDataVec])
        self.center = centerHelp.T

        ''' first m principal axes (weights)
            orhonormal (as needed by distance measure) '''
        self.weight, s, vh = np.linalg.svd(np.random.rand(pm.columns, self.outdimension), full_matrices=False)

        # first m eigenvalues
        self.eigenvalue = np.matlib.repmat(pm.lambda_init, self.outdimension, 1)

        # residual variance in the minor (d - m) eigendirections
        self.sigma = pm.lambda_init

        # deviation between input and center
        self.x_c = np.zeros((pm.columns, 1))

        # unit output (activation) for input x_c
        self.y = np.zeros((self.outdimension, 1))

        # unit matching measure
        self.mt = np.zeros((self.outdimension, 1))

        # unit summarized matching measure
        self.Dt = 1.0

        # Unit variance
        self.variance = 0

        # Unit total variance
        self.totalVariance = 0

        # global learning rate
        self.alpha = pm.epsilon_init

        # wird in UnitSpecificDimensionLineFitting benutzt
        self.gy = np.zeros((self.outdimension, 1))
