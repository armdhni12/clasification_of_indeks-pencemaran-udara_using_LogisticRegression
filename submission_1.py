# -*- coding: utf-8 -*-
"""Submission_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1atclhRONJkEjTE4viPJm_FQyaMyqU7dg

**Nama Kelompok: Jagoan Neon** 🦹🏻‍♂️⚡

**Kelas: MICRODENTIAL-002-UDINUS-04 Associate Data Scientist**

Studi Kasus: **Indeks Standar Pencemaran Udara (ISPU) Bulan Januari - Oktober Tahun 2021**

Metode Klasifikasi: **Logistic Regression**

Sumber: **Open Data Jakarta**

(Url Link: https://data.jakarta.go.id/dataset/indeks-standar-pencemaran-udara-ispu-tahun-2021)

**Import the Libraries**
"""

# for basic mathematics operation 
import os
import statsmodels.api as sm
import pandas as pd
import numpy as np

# for visualizations
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn import linear_model

# to inactivated warnings
import warnings 
warnings.filterwarnings('ignore')

"""**Exploratory Data Analysis and Pre-Processing**

Reading the Dataset
"""

# importing the dataset
df=pd.read_csv("palingbener.csv")
df

# deleting tanggal, max, and critical column
df=df.drop(["tanggal","max","critical"],axis=1)

# showing the dataframe
df

# showing a concise summary of a DataFrame
df.info()

# le = preprocessing.LabelEncoder()
# le.fit(df['categori'])
# df['categori']=le.transform(df['categori'])

# checking if there is any NULL data
df.isna().sum()

#fill NA/NaN values

df[["pm25","pm10","so2","co","o3","no2"]]=df[["pm25","pm10","so2","co","o3","no2"]].fillna(df[["pm25","pm10","so2","co","o3","no2"]].mean())

# checking is NA/NaN values filled already
df.isna().sum()

"""Data Visualization"""

df.hist(bins=20, figsize=(20,15))
plt.show()

# search for correlation
corr_matrix = df.corr()
sns.heatmap(corr_matrix, xticklabels=corr_matrix.columns, yticklabels=corr_matrix.columns)
plt.show()

# visualize the percentage of pollution level categories
plt.figure(figsize=(10,10))
df['categori'].value_counts().plot.pie(shadow=True, explode = [0,0.1, 0.2],autopct='%1.2f%%')
plt.title("Persentase Kategori Level Polusi")
plt.legend()
plt.show()

# visualize pairwise relationships in a dataset
sns.pairplot(df,hue='categori')

# gets rows (and/or columns) at integer locations
X=df[['pm10','pm25','so2','co','o3','no2']]
y=df['categori']
y

"""**Naive Bayes Classification**"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, accuracy_score,precision_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from sklearn.metrics import accuracy_score ,precision_score,recall_score,f1_score
from sklearn.datasets import make_classification

X_train, X_test, y_train, y_test  = train_test_split(X,y,test_size=0.2,random_state=101)

"""Making a confusion matrix"""

from sklearn.linear_model import  LogisticRegression
from sklearn import linear_model

logreg = LogisticRegression(solver= 'lbfgs',max_iter=400)
logreg.fit(X_train, y_train)
Y_pred = logreg.predict(X_test)
accuracy_lr=round(accuracy_score(y_test,Y_pred)* 100, 2)
acc_log = round(logreg.score(X_train, y_train) * 100, 2)

cm = confusion_matrix(y_test, Y_pred)
accuracy = accuracy_score(y_test,Y_pred)
precision =precision_score(y_test, Y_pred,average='micro')
recall =  recall_score(y_test, Y_pred,average='micro')
f1 = f1_score(y_test,Y_pred,average='micro')
print('Confusion matrix for Logistic Regression\n',cm)
print('accuracy_Logistic Regression : %.3f' %accuracy)
print('precision_Logistic Regression : %.3f' %precision)
print('recall_Logistic Regression: %.3f' %recall)
print('f1-score_Logistic Regression : %.3f' %f1)







# calculate the classification report
print(classification_report(y_test, Y_pred))

# Commented out IPython magic to ensure Python compatibility.
# calculate the mislabeled points out
print("Number of mislabeled points out of a total %d points : %d"
#       % (X_test.shape[0], (y_test != Y_pred).sum()))

import pickle

#save the model as pickle
with open('logreg.pkl','wb') as f:
    pickle.dump(logreg,f)

#load model
with open('logreg.pkl','rb') as f:
    clf_loaded=pickle.load(f)

#  #checking the model
model=pickle.load(open('logreg.pkl','rb'))
print(model.predict([[27,46,27,7,47,7]]))



