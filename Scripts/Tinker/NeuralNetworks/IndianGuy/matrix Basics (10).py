import numpy as np

indianProfitTable = [[200,220,250],[68,79,105],[110,140,180],[80,85,90]]

indianProfitMatrix = np.mat(indianProfitTable)


print(indianProfitMatrix)

convertedIndianProfitMatrix = indianProfitMatrix*75
print(convertedIndianProfitMatrix)





unitsSoldTable = [[50,60,25],[10,13,5],[40,70,52]]
pricePerUnit = [20,30,15]

moneyMadeEachYear = np.dot(unitsSoldTable,pricePerUnit)
print(moneyMadeEachYear)