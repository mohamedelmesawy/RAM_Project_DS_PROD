# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# https://drive.google.com/file/d/1KnyWpHrRpDHvffW0Ysh209HZYe_US3hZ/view?usp=sharing
FILE_PATH = './data/Mall_Customers.csv'


def preprocessing():
    df = pd.read_csv(FILE_PATH)
    le = LabelEncoder()
    df['Genre'] = le.fit_transform(df['Genre'].values)
    df['Age_<=_40'] = np.where(df['Age'] <= 40, True, False)
    df = (df - df.mean()) / df.std()

    # add ones column
    df.insert(0, 'Ones', 1)

    # set X (training data) and y (target variable)
    cols = df.drop(columns=['CustomerID', 'Age']).shape[1]
    X = df.drop(columns=['CustomerID', 'Age']).iloc[:, 0:cols-1]
    y = df.drop(columns=['CustomerID', 'Age']).iloc[:, cols-1:cols]

    # convert to matrices and initialize theta
    X = X.values
    y = y.values

    return X, y


def fit_model(X, y, normalize=False):
    model = LinearRegression(normalize=normalize)
    model.fit(X, y)
    return model


# Predict
def evaluate(model, X, y):
    y_pred = model.predict(X)
    score = r2_score(y, y_pred)
    return score


#  MAIN
def train_and_evaluate(normalize=False):
    print('I am in Train_and_evaluate Function.')
    X, y = preprocessing()
    model = fit_model(X, y, normalize)
    score = evaluate(model, X, y)
    return score, model

# Testing
# input_to_predict = np.array([1, 1, 44, 0])
# mr_predected_spending_score = model.predict(
#     input_to_predict.reshape([1, 4]))
# print(mr_predected_spending_score[0][0])
