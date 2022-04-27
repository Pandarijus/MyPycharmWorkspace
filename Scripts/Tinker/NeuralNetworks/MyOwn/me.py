from Bigbrain import *
def mySigmoid(value):
    return 1/1+np.exp(value)

def neural(inputs,solutions,repeats):
    weights = np.random.uniform(-0.2, 0.2, [2])
    b = 0
    for r in range(repeats):
        outputs = np.dot(inputs, weights) + b
        #outputs = mySigmoid(outputs)
        learning_rate = 0.5
        loss = np.mean(abs(solutions - outputs))
        l = solutions - outputs
        weights +=np.sum( learning_rate* np.dot(l,inputs)/4 ,0)

        b +=  learning_rate*np.mean(l)
        print(weights, b, outputs, solutions, loss)

    while True:
        x1 = input("x1:")
        x2 = input("x2:")
        print(weights[0]*int(x1)+weights[1]*int(x1)+b)




i = [[0,0],[0,1],[1,0],[1,1]]
so = [0,1,1,1]
neural(i,so,1000)



