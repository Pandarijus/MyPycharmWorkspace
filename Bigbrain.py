import numpy as np
import os

e =2.7182818284590452

def checkIfSringsAreEqual(str1,str2):
    return str1.lower() == str2.lower()
def getRandomInt(_min,_max):
    np.random.randint(_min,_max)
def getRandom(_min,_max):
    return np.random.uniform(_min,_max)

def calcIndexThatHasNotBeenUsed():
  print(os.listdir('Images'))
  listdirr = [int(l) for l in os.listdir('Images')]
  print(listdirr)
  maxNamedDir = max(listdirr)
  return maxNamedDir+1
def calcIndexOfDir(directory,fileName =""):

    listdirr = [str(l) for l in os.listdir(directory) if fileName in str(l) or not fileName]
    numbsOfDir = [0]
    for lis in listdirr:
        lis = lis[:-3]
        numbsOfDir.append(int(''.join([s for s in lis if s.isdigit()])))
    #print(numbsOfDir)
    maxNamedDir = max(numbsOfDir)
    return maxNamedDir+1



