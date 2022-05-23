import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression,RidgeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pickle

fileEnding ="csv"
fileName = "HandRightSigns"
path = f"Saves/Model/{fileName}.{fileEnding}"
pickSpecificPipeline = False#'rf'

df = pd.read_csv(path,header=None)
x = df.drop(columns=df.columns[0],axis=1)
y = df.iloc[:, 0]

xTrain,xTest,yTrain,yTest = train_test_split(x, y, test_size=0.3,random_state=1234)
pipes = {
    'lr':make_pipeline(StandardScaler(),LogisticRegression()),
    'rc':make_pipeline(StandardScaler(),RidgeClassifier()),
    'rf':make_pipeline(StandardScaler(),RandomForestClassifier()),
    'gb':make_pipeline(StandardScaler(),GradientBoostingClassifier())
}
#print(pipes.keys())
models = {}

for index,pip in pipes.items():
    print("Starting Training:",index)
    model = pip.fit(xTrain,yTrain)
    models[index] = model

if pickSpecificPipeline:
    pick = pickSpecificPipeline
else:
    highestScore = 0
    highestPipe = 0
    for modelName, model in models.items():
        yAi = model.predict(xTest)
        accuracy = accuracy_score(yTest, yAi)
        print(modelName, accuracy * 100, "%")
        if accuracy > highestScore:
            highestScore = accuracy
            highestModel = modelName
    pick = highestModel
print("The best Model: [",pick,"]")

# pick = input("which model do you like best?")
# if pick not in models:
#     pick = 'rf'

with open(path[:-4]+'.pkl','wb') as file:
    pickle.dump(models[pick],file)
    print("Saved [", pick, "]")
