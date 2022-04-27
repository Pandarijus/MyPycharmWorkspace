import numpy as np

def sigmoid_numpy(X):
   return 1/(1+np.exp(-X))

def log_loss(y_true, y_predicted):#doesn't matter for back propagation
    epsilon = 1e-15
    y_predicted_new = [max(i,epsilon) for i in y_predicted]
    y_predicted_new = [min(i,1-epsilon) for i in y_predicted_new]
    y_predicted_new = np.array(y_predicted_new)
    return -np.mean(y_true*np.log(y_predicted_new)+(1-y_true)*np.log(1-y_predicted_new))


def gradient_descent(age, affordability, y_true, epochs):#loss_thresold
    w1 = np.random.rand()
    w2 = np.random.rand()
    bias = np.random.rand()
    rate = 0.5
    n = len(age)
    for i in range(epochs):
        weighted_sum = w1 * age + w2 * affordability + bias
        y_predicted = sigmoid_numpy(weighted_sum)
        #print(y_predicted)
        loss = log_loss(y_true, y_predicted)

        w1d = (1/n)*np.dot(np.transpose(age),(y_predicted-y_true))
        w2d = (1/n)*np.dot(np.transpose(affordability),(y_predicted-y_true))

        bias_d = np.mean(y_predicted-y_true)
        w1 = w1 - rate * w1d
        w2 = w2 - rate * w2d
        bias = bias - rate * bias_d

        #print (f'Epoch:{i}, w1:{w1}, w2:{w2}, bias:{bias}, loss:{loss}')
        #print (f"diff:{abs(y_true-y_predicted)}")
        print(f'Epoch:{i}, Output:{y_predicted}, Solution:{solution} loss:{loss}')
        #if loss<=loss_thresold:
         #   break

    print()
    print(f"{w1},{w2},{bias}")
    return w1, w2, bias



def sigmoid(x):
    import math
    return 1 / (1 + math.exp(-x))

def prediction_function(x1, x2,w1,w2,bias):
    weighted_sum = w1*x1 + w2*x2 + bias
    return sigmoid(weighted_sum)

input1   = [0,1,0,1]
input2   = [0,0,1,1]
solution = [0,1,1,1]


input1 = np.array(input1)
input2 = np.array(input2)
solution = np.array(solution)


babyBrain = (input("1==Learn  2==Test\n") == '1') #"test"
if babyBrain:
    gradient_descent(input1,input2,solution,1000)
else:

    while True:
        x1 = float(input("x1:"))
        x2 = float(input("x2:"))
        p = prediction_function(
        x1,x2,
        #paste neutal values down here:
        7.262377984308832,7.2618751499762775,-3.1586301678851507
        )
        print(p)





