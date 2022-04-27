import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression,RidgeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pickle

fileName = "abend.csv"

df = pd.read_csv(fileName,header=None)
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
    model = pip.fit(xTrain,yTrain)
    models[index] = model

for index,model in models.items():
    yAi = model.predict(xTest)
    print(index,accuracy_score(yTest,yAi))

pick = input("which model do you like best?")
if pick not in models:
    pick = 'rf'

with open(fileName[:-4]+'.pkl','wb') as file:
    pickle.dump(models[pick],file)
