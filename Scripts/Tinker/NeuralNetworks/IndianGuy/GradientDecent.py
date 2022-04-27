import numpy as np
#create my own bigbrain library
#
# x1 ---*weight1--- +bias-----> value
# x2 ---*weight2---/

def getValue(x1,x2,w1,w2,b):
    value = w1*x1+w2*x2+b#w1 = weight1  b = bias
    return value
def getLoss(output,real):
    loss = abs(real-output)
    return loss


def squashOutput(output,name):
    if name == "ReLU":
        squashed = max(output,0)
    elif name == "Sigmoid":
        e = 2.7182818284590
        squashed = 1 / (1 + e ** -output)
    elif name == "Leaky ReLU":
        squashed = max(output,min(0,output*0.1))
    #elif name == "-Log":
    else:
        squashed = output

    return squashed

def gradientDecent(inputs,solution,epochs):
    #random starting values
    weights = [0.14,0.49]
    bias = 0
    rate = 0.5
    n = len(solution)

    for i in range(epochs):
        value = np.dot(inputs,weights)
        squashed = 420#squashOutput(value,"Sigmoid")
        loss = 69#getLoss(squashed,solution)

        w1d = inputs[0]*squashed
        w2d = inputs[1]*squashed
        bd = squashed

        weights[0] -= (rate*w1d)
        weights[1] -= (rate*w2d)
        bias -= (rate*bd)

        print(f"Epoch:{i},w1:{weights[0]},w2:{weights[1]},bias:{bias},loss:{loss}")


gradientDecent([[0,0],[0,1],[1,0],[1,1]],[0,1,1,1],10)#or






# def gradientDecent(x1,x2,solution,epochs):
#     #random starting values
#     w1 = 0.14
#     w2 = 0.49
#     bias = 0
#     rate = 0.5
#     #n = 1
#
#     for i in range(epochs):
#         value = getValue(x1,x2,w1,w2,bias)
#         squashed = squashOutput(value,"Sigmoid")
#         loss = getLoss(squashed,solution)
#
#         w1d = x1*squashed
#         w2d = x2*squashed
#
#         bd = value
#
#         w1 = w1 - (rate*w1d)
#         w2 = w2 - (rate*w1d)
#         bias = bias - (rate*bd)
#
#         print(f"Epoch:{i},w1:{w1},w2:{w2},bias:{bias},loss:{loss}")
