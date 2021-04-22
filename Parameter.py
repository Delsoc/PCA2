import scipy.io as sio
import math

'''Datasets:
    0. cameraman
    1. circles
    2. PHM
    3. careercon
    4. waveData
    5. waveDataNoNoise
'''
Datasets = ["cameraman.mat", "circles.mat", "PHM.mat", "careercon.mat", "waveData.mat", "waveDataNoNoise.mat"]
'''criterion:
    0. Eigenvalue-Ooe
    1. Eigenvalue-average
    2. Percentage of total variance
    3. Cumulative percentage of total variance
    4. Kirsch et al. approach
'''
class Parameter():
    def __init__(self):

        self.x = 0 #erstmal einfach irgendein Wert, damit es erstellt ist, um es in stimulus_activation ändern zu können

        self.Dataset = 3   #0-5 #oben beschrieben
        self.criterion = 4 #noch useless #oben beschrieben

        self.temp = sio.loadmat(Datasets[self.Dataset])
        self.shape = self.temp['data']

        self.StartDim = 2

        self.tau = 0
        self.sigmaMean = 0

        self.dimThreshold = 0.90

        #learningrate
        self.epsilon_init  = 0.5
        self.epsilon_final = 0.001

        #Neighborhood range
        self.rho_init = 2
        self.rho_final = 0.01

        #initial variance
        self.lambda_init = 1000.0

        #number of data points and input dimension
        self.columns = len(self.shape[0])
        self.rows = len(self.shape)

        #number of total iterations
        self.T = self.rows

        self.helper = 0

        #Adaptive Lernratensteuerung fur Neural Gas Principal Component Analysis.
        self.mu = 0.005
        self.xvalue =0
        self.logArgMinLimit = 1e-323
        self.phi = 2.0
        self.udmLogBase = 10.0
        self.log_precomp = math.log(self.udmLogBase).__round__(4)