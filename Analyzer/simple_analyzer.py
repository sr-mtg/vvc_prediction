from VCA_data_frame import X,Y

#######split Data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


#######ML algorithm  --> RandomForestRegressor
# from sklearn.ensemble import RandomForestRegressor
# model = RandomForestRegressor(random_state=42)
# model.fit(X_train, y_train)
#######ML algorithm  --> LinearRegression
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X_train, y_train)
#######ML algorithm  --> LinearRegression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

############Evaluate Model
from sklearn.metrics import mean_absolute_error,mean_squared_error
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
percentage_error = (mae / y_test.mean()) * 100

print('Mean Absolute Error: ',mae)
print('Mean Squared Error (MSE):', mse)
print("Percentage Error:",percentage_error)

