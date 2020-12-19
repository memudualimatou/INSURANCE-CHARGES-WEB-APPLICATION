import warnings

warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_score
from sklearn.preprocessing import LabelEncoder
from math import sqrt
import pickle

data = pd.read_csv('insurance.csv')

print("train shape {} rows, {} columns".format(*data.shape))

cat_var = data.select_dtypes(include=['object']).columns
print(cat_var)

previous_data = data.copy()
data = data[data.charges < 50000]
data.reset_index(drop=True, inplace=True)

#
labelencoder_X = LabelEncoder()
data['sex'] = labelencoder_X.fit_transform(data['sex'])
data['smoker'] = labelencoder_X.fit_transform(data['smoker'])
data['region'] = labelencoder_X.fit_transform(data['region'])

# In[28]:
print(data)

# # MODEL


# Spliting the datasewt
X = data[data.columns.drop('charges')]
y = data['charges']

# splitting the dataset into training and test set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# lookin for the best parameters

regressor = RandomForestRegressor(random_state=42)
param_grid = {'bootstrap': [True, False],
              'max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, None],
              'max_features': ['auto', 'sqrt'],
              'min_samples_leaf': [1, 2, 4],
              'min_samples_split': [2, 5, 10],
              'n_estimators': [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
              }
CV_rfc = RandomizedSearchCV(estimator=regressor, param_distributions=param_grid, n_iter=100, cv=3, verbose=2,
                            random_state=42, n_jobs=-1)
CV_rfc.fit(X_train, y_train)

# In[34]:


params = CV_rfc.best_params_

print(params)

# Fitting Random Forest Regression to the dataset

regressor = RandomForestRegressor(**params)
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Predicting the training set result
y_train_pred = regressor.predict(X_train)

# In[36]:


print("R2 score on the test set:", r2_score(y_test, y_pred) * 100)
print("R2 score on the training set:", r2_score(y_train, y_train_pred) * 100)

# In[37]:


print("RMSE score on the test set:", sqrt(mean_squared_error(y_test, y_pred)))
print("RMSE score on the training set:", sqrt(mean_squared_error(y_train, y_train_pred)))

# In[38]:


accuracies = cross_val_score(estimator=regressor, X=X_train, y=y_train, cv=10)
print(accuracies.mean(), accuracies.std())

# In[39]:


# # visualizing between the actual and the predicted charges on the test set
plt.scatter(y_test, y_pred)
plt.xlabel('actual charges')
plt.ylabel('predicted charges')
plt.title('Real charges vs actual charges')
plt.show()

# # MODEL TESTING

# In[40]:


# To save the sterialized model
pickle.dump(regressor, open('model.pkl', 'wb'))

# In[41]:


# load/deserialized model to make future prediction
model = pickle.load(open("model.pkl", 'rb'))
print(model.predict([[19, 0, 28, 0, 1, 1]]))
