import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

# Load your data
df_EH = pd.read_csv('result_aau/EH.csv')
df_siti = pd.read_csv('result_aau/siti.csv')
X = df_siti.drop('Name', axis=1)
X['E'] = df_EH['E']
X['h'] = df_EH['h']
df_size = pd.read_csv('size.txt')
X['Size'] = df_size['Size']
df_responsTime = pd.read_csv('result_aau/x265_time_medium_c5_2xlarge.csv')
Y = df_responsTime['time_QP27']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Define machine learning models
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

# Initialize lists to store evaluation results
model_names = []
mae_scores = []
mse_scores = []
mpe_scores = []

# Evaluate each model
for model_name, model in models:
    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate Mean Absolute Error (MAE)
    mae = mean_absolute_error(y_test, y_pred)
    mae_scores.append(mae)

    # Calculate Mean Squared Error (MSE)
    mse = mean_squared_error(y_test, y_pred)
    mse_scores.append(mse)

    # Calculate Mean Percentage Error (MPE)
    percentage_error = (mae / y_test.mean()) * 100
    mpe_scores.append(percentage_error)

    model_names.append(model_name)

# Create a bar chart to visualize the metrics for each model
plt.figure(figsize=(12, 6))
bar_width = 0.25
index = range(len(model_names))
plt.bar(index, mae_scores, label='MAE', color='skyblue', width=bar_width)
plt.bar(index, mse_scores, label='MSE', color='lightcoral', alpha=0.6, width=bar_width, align='edge')
plt.bar(index, mpe_scores, label='MPE', color='lightgreen', alpha=0.6, width=bar_width, align='edge')
plt.xlabel('Models')
plt.ylabel('Error')
plt.title('Model Comparison: MAE, MSE, and MPE')
plt.legend()
plt.xticks(index, model_names, rotation=45)
plt.tight_layout()

# Annotate bars with numeric values
for i, mae in enumerate(mae_scores):
    plt.text(i, mae, f'{mae:.2f}', ha='center', va='bottom', fontsize=10)
for i, mse in enumerate(mse_scores):
    plt.text(i + bar_width, mse, f'{mse:.2f}', ha='center', va='bottom', fontsize=10)
for i, mpe in enumerate(mpe_scores):
    plt.text(i + bar_width, mpe, f'{mpe:.2f}', ha='center', va='top', fontsize=10)

# Show the plot
plt.show()
