import numpy as np

class Neural:
    def __init__(self,layerID, nBrainPerBatch, nOfFutureCalculators):
        self.tools = np.random.rand(nBrainPerBatch, nOfFutureCalculators) * 0.1
        self.cheese = np.zeros(nOfFutureCalculators)
        self.values = None
        self.layerID = layerID

    def __str__(self):
        return f"LayerID ({self.layerID}):\n"+str(self.values)+"\n \n"
    def __repr__(self):
        return f"LayerID ({self.layerID}):\n"+str(self.values)+"\n \n"

    def forward(self,_brains):
        self.values =np.dot(_brains,self.tools)+self.cheese
        return self.values

    def forwardButFlatAtMius(self,_brains):
        forward = self.forward(_brains)
        self.values = np.maximum(0,forward)
        return self.values

    def softmax(self,_brains):
        forward = self.forward(_brains)

        allMaximums = np.amax(forward, axis=1,keepdims=True)
        forward-=allMaximums#minus maximum to make sure that the values stay small

        forward = np.exp(forward) # make it e^x so there is no 0 or smaller

        allSums = np.sum(forward,axis=1,keepdims=True)
        forward /=allSums#normalize values to get percent value between 0 and 1
        self.values = forward
        return self.values

    def categoricalCrossEtropy(self,y_pred,y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred,1e-7,1-1e-7)
        correct_confidences = y_pred_clipped[range(samples),y_true]

        loss = -np.log(correct_confidences)
        print(loss)
        self.values = loss
        return self.values

def forwardAll(layers,startInput):
    step = []
    step.append(layers[0].forwardButFlatAtMius(startInput))
    for i in range(len(layers)-1,1):
        step.append(layers[i].forwardButFlatAtMius(step[i-1]))
        
    step.append(layers[-1].categoricalCrossEtropy(step[-1],[1,1,1,1,1]))

    for s in step:
        print()
        print()
        print(s)
        print()
        print()


def allLayers(startInput,calculatorPerLayer,nLayers):
    nBrainsPerBatch = startInput.shape[1]
    firstLayer = Neural(1,nBrainsPerBatch,calculatorPerLayer)

    layers = []
    print("Input: \n",startInput)
    layers.append(firstLayer)
    for n in range(nLayers):
        layers.append(Neural(n+2,calculatorPerLayer,calculatorPerLayer))

    lastLayer = Neural("LAST",calculatorPerLayer, startInput.shape[0])
    layers.append(lastLayer)

    forwardAll(layers,startInput)

#(5,2)x(2,3) = (5,3)  5 batches and 3 calculators


while True:
    brains = [[-0.2,1.2],[1.2,-5.4],[11.52,-19.72],[0.82,4.92],[-0.11,1.44]]#shape = (5,2)
    brains = np.array(brains)
    allLayers(brains,6,4)
    input("waiting")


#The Output Shape will allways start with the starting batch size z.B. starBatch = 2 then size = (2,?)