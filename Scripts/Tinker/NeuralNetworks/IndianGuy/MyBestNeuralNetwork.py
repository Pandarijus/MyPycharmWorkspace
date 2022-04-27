import numpy as np

def myCalcFunction(X):
    return myReLU(X)#myReLU(X)

def myReLU(X):
   return np.maximum(0,X)

def mySigmoid(X):
    return 1/(1+np.exp(-X))

def getLoss(y_true, y_predicted):#doesn't matter for back propagation
    return sum(abs(y_true-y_predicted))


def gradient_descent(x1, x2, solution, repeats):
    w1 = np.random.rand()
    w2 = np.random.rand()
    bias = np.random.rand()
    rate = 0.5
    n = len(x1)

    for i in range(repeats):
        weighted_sum = w1 * x1 + w2 * x2 + bias
        output =myCalcFunction(weighted_sum)#mySigmoid(weighted_sum)# myReLU(weighted_sum)
        #print(output)
        loss = getLoss(solution, output)

        w1d = (1/n)*np.dot(np.transpose(x1), (output - solution))#I DIDN'T WRITE THIS
        w2d = (1/n)*np.dot(np.transpose(x2), (output - solution))#I DIDN'T WRITE THIS

        bias_d = np.mean(output - solution)#I DIDN'T WRITE THIS
        w1 = w1 - rate * w1d#I DIDN'T WRITE THIS
        w2 = w2 - rate * w2d#I DIDN'T WRITE THIS
        bias = bias - rate * bias_d#I DIDN'T WRITE THIS


        print(f'Epoch:{i}, Output:{output}, Solution:{solution} loss:{loss}')
        if loss<= 0.0001:# stop at 99.99% acuracy
            break

    print("Rounded values:")
    
    print(f"{round(w1,4)},{round(w2,4)},{round(bias,4)}")

    with open("saveNeuralOutput.txt",'w+') as textFile:
        textFile.write(f"{round(w1,4)},{round(w2,4)},{round(bias,4)}")

    print("Normal values:")
    print(f"{w1},{w2},{bias}")
    return w1, w2, bias


def getValue(x1, x2, w1, w2, bias):
    value = w1*x1 + w2*x2 + bias
    return myCalcFunction(value)#mySigmoid(value)#myReLU(value)


#babyBrain = (input("Do you want to train the Neural Network first? [y]es [n]o  \n") != 'n')

module = input("What Model do you want? ([AND]  [OR]  [XOR])\n")
if module == "AND":
    input1   = [0,1,0,1]
    input2   = [0,0,1,1]
    solution = [0,0,0,1]
elif module == "OR":
    input1   = [0,1,0,1]
    input2   = [0,0,1,1]
    solution = [0,1,1,1]
else:
    module = "XOR"
    input1   = [0,1,0,1]
    input2   = [0,0,1,1]
    solution = [1,0,0,1]

input1 = np.array(input1)
input2 = np.array(input2)
solution = np.array(solution)




#if babyBrain:
gradient_descent(input1,input2,solution,1000)
print("\n \n")# \n \n \n \n \n \n \n \n \n \n \n \n \n")


with open("saveNeuralOutput.txt") as file:
    saved = file.readline()
    saved = saved.split(',')
    saved = [float(s) for s in saved]


print("Module: "+module)
while True:
    x1 = float(input("x1:"))
    x2 = float(input("x2:"))
    p = getValue(x1,x2,saved[0],saved[1],saved[2])
    print("Real Output:",p)
    print("Rounded:",round(p))