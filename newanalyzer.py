
#######collect Data
import pandas as pd
df_siti = pd.read_csv('result_aau/EH.csv')
#df_siti = pd.read_csv('result_aau/siti.csv')
#print(df_siti.head())
X = df_siti.drop('Name', axis=1)
#print(X.head())
df_size = pd.read_csv('size.txt')
X['Size'] = df_size['Size']

df_responsTime = pd.read_csv('result_aau/x265_time_medium_c5_2xlarge.csv')
#print(df_responsTime.head())
Y = df_responsTime['time_QP27']

#######split Data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
############## ml alg
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

linear_reg = LinearRegression()
ridge_reg = Ridge()
lasso_reg = Lasso()
decision_tree_reg = DecisionTreeRegressor()
random_forest_reg = RandomForestRegressor()
gradient_boosting_reg = GradientBoostingRegressor()
svr_reg = SVR()

models = [
    ('Linear Regression', linear_reg),
    ('Ridge Regression', ridge_reg),
    ('Lasso Regression', lasso_reg),
    ('Decision Tree Regression', decision_tree_reg),
    ('Random Forest Regression', random_forest_reg),
    ('Gradient Boosting Regression', gradient_boosting_reg),
    ('Support Vector Regression', svr_reg)
]

for model_name, model in models:
    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate Mean Absolute Error (MAE)
    mae = mean_absolute_error(y_test, y_pred)

    # Calculate Mean Squared Error (MSE)
    mse = mean_squared_error(y_test, y_pred)



    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

        
    # Calculate Mean Percentage Error (MSE)
    percentage_error = (mae / y_test.mean()) * 100

    

    print("Model:", model_name)
    print("Mean Absolute Error (MAE:",mae)
    print("Mean Squared Error (MSE):",mse)
    print("Root Mean Squared Error (RMSE):", rmse)
    print("R-squared (R2):", r2)
    print("percentage_error:",percentage_error)
    print()