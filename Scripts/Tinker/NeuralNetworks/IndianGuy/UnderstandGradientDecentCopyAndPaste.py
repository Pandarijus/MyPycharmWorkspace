import numpy as np

def myReLU(X):
    return np.maximum(0, X)

def gradient_descent(x1, x2, solution, repeats):
    print("\n \n")
    # ----------Start DATA----------#
    w1 = np.random.rand()
    w2 = np.random.rand()
    bias = np.random.rand()
    rate = 0.5
    n = len(x1)
    # ----------Start DATA----------#

    for i in range(repeats):


        value = w1 * x1 + w2 * x2 + bias
        print("Value:",value)
        output = myReLU(value)
        print("Output:",output )
        roundedOutput = [round(o,4) for o in output]
        print("roundedOutput:", roundedOutput)
        print("solution:", solution)
        print()


        diffOutputMinusSolution = (output - solution)

        print("diffOutputMinusSolution:", diffOutputMinusSolution)
        print()

        w1d = (1 / n) * np.dot(np.transpose(x1), diffOutputMinusSolution)
        print("x1:", x1)
        print("np.transpose(x1):", np.transpose(x1))
        print("divided by:",n)


        print("w1d:",w1d )
        w2d = (1 / n) * np.dot(np.transpose(x2), diffOutputMinusSolution)
        print("w2d:", w2d)

        bias_d = np.mean(diffOutputMinusSolution)# mean = sum/count
        print("bias_d:", bias_d)
        w1 -=(rate * w1d)
        print("w1:", w1)
        w2 -= (rate * w2d)
        print("w2:", w2)
        bias -= (rate * bias_d)
        print("bias:", bias)
        print("\n \n")




#----------INPUT DATA----------#

input1 = [0, 1, 0, 1]
input2 = [0, 0, 1, 1]
solution = [0, 0, 0, 1]

input1 = np.array(input1)
input2 = np.array(input2)
solution = np.array(solution)

gradient_descent(input1, input2, solution, 100)


#----------INPUT DATA----------#
