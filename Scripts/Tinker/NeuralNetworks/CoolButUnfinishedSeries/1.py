brains = [3,2]#2 brains
tools = [0.2,0.1]#1 calculatior with 2 tools for 2 brains
cheese = 3#1 cheese for 1 calculator

n_brains = len(brains)#calcs how many brains there are in the list
ball = 0#creates a list of zeros as placeholders for balls that come out of the calculators

value = 0
for i in range(n_brains):#for each brain do a calculation
    value += brains[i] * tools[i]#brain*tool+cheese = ball

ball = value+cheese
print(ball)#print balls

