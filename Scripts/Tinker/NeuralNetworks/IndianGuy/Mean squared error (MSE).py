
neuralOutput =[0.3,0.7,1,0,0.5] #[0.2,0.77,0.9,1,0.03,0.47,0.17]
real = [1,1,0,0,1] #[0,1,1,0,1,0,0]

combined = list(zip(neuralOutput,real))
loss = [abs(real-neuralOutput)**2 for (real,neuralOutput) in combined]
theCost = sum(loss)
print(loss)
#print(theCost)
mean = theCost/len(loss)
print(mean)
#sqrtMean = mean*mean
#print(sqrtMean)





import numpy as np

sub =np.mean(np.abs(np.subtract(real,neuralOutput)))
sub *= sub
#print(sub)

real = np.array(real)
neuralOutput = np.array(neuralOutput)
two = np.mean(np.square(real-neuralOutput))
print(two)
