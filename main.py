#import the lib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pickle

#load the data
data = pd.read_csv("heart.csv")
data.drop(["Sex","ChestPainType","RestingECG","FastingBS"], axis="columns", inplace= True)
print(data.head())
max_values = data.max(axis="rows")
min_values = data.min(axis="rows")

#understand the data
res = data.isnull().sum()
print(res)

#features and target
features = data.drop("HeartDisease", axis="columns")
target = data["HeartDisease"]
print(features.head())
print(target.head())

#handle cat data
nfeatures = pd.get_dummies(features, drop_first=True)
print(nfeatures.head())

#feature importance
#mfeatures = data.drop(['Sex','ChestPainType','RestingECG'],axis="columns",inplace=True)
#print(mfeatures)

#train and test 
x_train, x_test, y_train, y_test = train_test_split(nfeatures, target)

#model
model = RandomForestClassifier()
model.fit(nfeatures, target)

#performance
#cr = classification_report(y_test, model.predict(x_test))
#print(cr * 100)

#prediction 
print("__________________________________________________")
data = [[37,130,283,98,0.0,0,0,1]]
data1 = [[49,160,180,156,1.0,0,1,0]]
res = model.predict(data1)
print(res)	

#features importance
#x = nfeatures.columns
#y = model.feature_importances_
#plt.figure(figsize=(12,4))
#plt.bar(x, y)
#plt.show()
#print(y)

#finding maximum and minimum value from the dataset
print(max_values)
print(min_values)
 
#save the model 
with open("heart.model", "wb") as f:
	pickle.dump(model,f)
