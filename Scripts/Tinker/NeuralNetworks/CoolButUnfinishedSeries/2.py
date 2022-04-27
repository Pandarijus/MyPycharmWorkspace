def calcNextLayer(prevBrains, currentTools, currentCheese):#brains,tools,cheeses
    n_brains = len(prevBrains)#calculate how many brains there are

    value = 0
    for brainIndex in range(n_brains):#goes through every brain
        brain = prevBrains[brainIndex]
        for tool in currentTools:
            value += brain*tool#brain mush

    return [value +currentCheese]# every brain mush + cheese = ball


brains = [3,2]#brains
ball1Tools = [0.2,0.1]#first ball has 2 tools for 2 brains
ball2Tools = [0.12]#second ball has 2 tools for 2 brains

ball1Cheese = 3#first cheese
ball2Cheese = -1#second cheese


ball1 = calcNextLayer(brains,ball1Tools,ball1Cheese)#i have to add them togeher right?
print(ball1)
ball2 = calcNextLayer(ball1,ball2Tools,ball2Cheese)
print(ball2)
