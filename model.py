import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import openpyxl
from sklearn.ensemble import RandomForestClassifier

data = pd.read_excel('dataGYM.xlsx')

df = data.copy()
del df['BMI']
del df['Prediction']

df["Class"].replace({"EXtremely obese":"Extremely obese", "Healthy\xa0":"Healthy", "Under weight":"Underweight"}, inplace=True)

df["weight"] = df["weight"]*2.2

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)
model_GYM = RandomForestClassifier(n_estimators=20)
model_GYM.fit(x_train, y_train)

def gym_app():
  age = input("Your Age: ")
  height = input("Your height in feet: ")
  weight = input("Your weight in pounds: ")
  input_data = np.asarray([[age, height, weight]])
  prediction = model_GYM.predict(input_data)
  print(f"prediction: {prediction[0]}")

print(gym_app())

import pickle
pickle.dump(model_GYM, open("model_GYM.sav", "wb"))