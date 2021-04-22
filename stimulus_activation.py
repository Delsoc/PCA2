from copy import deepcopy
import math
import random
import numpy as np
def stimulus_activation(parameter,units):

    parameter.xvalue = math.ceil((parameter.rows-1) * random.uniform(0.1, 1.0))#hier p.rows-1 ,bei matlab nicht
    Shape =parameter.shape.astype(np.float)
    parameter.x = Shape[parameter.xvalue, :].T
    X = np.zeros((len(Shape[0]), 1))

    for i in range(len(Shape[0])):
        X[i] = Shape[parameter.xvalue, i]

    #calculate neuron input and output (activation)
    units.x_c = np.subtract(X, units.center)
    units.y = np.dot(units.weight.T, units.x_c)

    return (parameter,units)