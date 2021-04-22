from docutils.nodes import paragraph

import Init
import stimulus_activation
import unit_adaption
import numpy as np
import UnitSpecificDimensionLineFitting
import matplotlib.pyplot as plt


def main():
    # 1: PREALLOCATION AND INITIALIZATION
    repetitions = 10
    parameters, units = Init.initialize()

    np.zeros((repetitions, parameters.rows))
    outDimTotal = np.zeros((repetitions, parameters.rows))

    # Main Loop
    for g in range(0, repetitions):
        print("g_loop")
        # reproducibility
        # rng(g); //matlabcode , aber wofür? wird nix mit gemacht und funktoniert genau gleich ohne den code
        # Init Parameters and PCA
        parameters, units = Init.initialize()
        outDim = np.zeros((parameters.T, 1))
        for loop in range(0, parameters.T):
            # 2: Unit STIMULUS AND ACTIVATION
            parameters, units = stimulus_activation.stimulus_activation(parameters, units)
            # 3: UNIT ADAPTATION
            parameters, units = unit_adaption.unit_adaption(parameters, units)
            # 4: ADJUSTING UNIT SPECIFIC DIMENSION

            if units.protect == 0:
                if parameters.criterion == 4:
                    parameters, units = UnitSpecificDimensionLineFitting.UnitSpecificDimensionLineFitting(parameters,
                                                                                                          units)
            else:
                units.protect = units.protect - 1

            # 5 Benchmark
            outDim[loop] = units.outdimension

    print("ende")
    return


main()
