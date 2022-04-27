#how and why do batches work?????  because it minimizes the difference between inputs. minimizing too mutch hurts you?

import numpy as np

brains = [3,2]
toolsLayer1 =  [[0.2,0.1],
                [3.1,3.4],
                [4.22,1.2]]


toolsLayer2 =      [[0.12,1.22,1.22],
                    [3.1, 2.1,1.22],
                    [0.64, 1.9,1.22]]


biasesLayer1 = [3,-2,7]
biasesLayer2 = [-1,5,0.2]



layer1 = np.dot(toolsLayer1,brains)+biasesLayer1
print(layer1)

layer2 = np.dot(toolsLayer2,layer1)+biasesLayer2
print(layer2)



# class Layer:
#     def createLayer(self):
#
#
# def calcNextLayer(prevLayer, thesesWeightss, theseBiass):
#     n_BallsPerLayerer = len(thesesWeightss)
#
#
#
# inputLayer = [[3,2]]
# allFirstWeights =  [[0.2,0.1],
#                     [3.1,3.4],
#                     [4.22,1.2]]
#
#
# allSecondWeights = [[0.12,1.22],
#                     [3.1, 2.1],
#                     [0.64, 1.9]]
#
#
# firstBiass = [3,-2,7]
# secondBiass = [-1,5,0.2]
