import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load your data and split it into training and testing sets as you did before...
df_EH = pd.read_csv('result_aau/EH.csv')
df_siti = pd.read_csv('result_aau/siti.csv')
#print(df_siti.head())
X = df_siti.drop('Name', axis=1)
X['E'] = df_EH['E']
X['h'] = df_EH['h']
#print(X.head())
df_size = pd.read_csv('size.txt')
X['Size'] = df_size['Size']

df_responsTime = pd.read_csv('result_aau/x265_time_medium_c5_2xlarge.csv')
#print(df_responsTime.head())
Y = df_responsTime['time_QP27']

#######split Data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
# Create an empty DataFrame to store the results
results_df = pd.DataFrame(columns=['Model', 'MAE', 'MSE', 'Percentage Error'])

models = [
    ('Linear Regression', LinearRegression(), 'normalizeNeeded'),
    ('Ridge Regression', Ridge(), 'normalizeNeeded'),
    ('Lasso Regression', Lasso(), 'normalizeNeeded'),
    ('Decision Tree Regression', DecisionTreeRegressor(), 'Non'),
    ('Random Forest Regression', RandomForestRegressor(), 'Non'),
    ('Gradient Boosting Regression', GradientBoostingRegressor(), 'Non'),
    ('Support Vector Regression', SVR(), 'normalizeNeeded')
]

for model_name, model, normalize in models:
    # Train the model
    if normalize == 'normalizeNeeded':
        scaler = MinMaxScaler()

        # Fit and transform the scaler on your training data
        X_train_scaled = scaler.fit_transform(X_train)

        # Use the same scaler to transform your test data
        X_test_scaled = scaler.transform(X_test)
        model.fit(X_train_scaled, y_train)

        # Make predictions
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

    # Calculate Mean Absolute Error (MAE)
    mae = mean_absolute_error(y_test, y_pred)

    # Calculate Mean Squared Error (MSE)
    mse = mean_squared_error(y_test, y_pred)

    # Calculate Mean Percentage Error (MSE)
    percentage_error = (mae / y_test.mean()) * 100

    # Add the results to the DataFrame
    results_df = results_df.append({'Model': model_name, 'MAE': mae, 'MSE': mse, 'Percentage Error': percentage_error}, ignore_index=True)

plt.figure(figsize=(12, 6))
plt.subplot(131)
bars = plt.barh(results_df['Model'], results_df['MAE'], color='skyblue')
plt.xlabel('MAE')
plt.title('Mean Absolute Error (MAE)')
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, round(bar.get_width(), 2), ha='center', va='center')

plt.subplot(132)
bars = plt.barh(results_df['Model'], results_df['MSE'], color='lightcoral')
plt.xlabel('MSE')
plt.title('Mean Squared Error (MSE)')
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, round(bar.get_width(), 2), ha='center', va='center')

plt.subplot(133)
bars = plt.barh(results_df['Model'], results_df['Percentage Error'], color='lightgreen')
plt.xlabel('Percentage Error (%)')
plt.title('Mean Percentage Error')
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, round(bar.get_width(), 2), ha='center', va='center')

plt.tight_layout()
plt.show()