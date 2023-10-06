from VCA_data_frame import X,Y
#find best feture
best_result=[]
X2=X
min_errorr = 100
best_model=''
all_feature = ['SI', 'TI', 'E', 'h', 'max_E', 'min_E', 'max_h', 'min_h', 'max_SI', 'min_SI', 'max_TI', 'min_TI', 'Size']
n = len(all_feature)
for i in range(2**n):
    subset = []
    X=X2
    for j in range(n):
        if (i >> j) & 1:
            subset.append(all_feature[j])
    print(subset)
    if n != len(subset):
        for feature in subset:
            X = X.drop(feature, axis=1)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    ############## ml alg
    from sklearn.linear_model import LinearRegression, Ridge, Lasso
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
    from sklearn.svm import SVR
    from sklearn.metrics import mean_absolute_error, mean_squared_error
    from sklearn.preprocessing import MinMaxScaler


    linear_reg = LinearRegression()
    ridge_reg = Ridge()
    lasso_reg = Lasso()
    decision_tree_reg = DecisionTreeRegressor()
    random_forest_reg = RandomForestRegressor()
    gradient_boosting_reg = GradientBoostingRegressor()
    svr_reg = SVR()

    models = [
        ('Linear Regression', linear_reg,'normalizeNeeded'),
        ('Ridge Regression', ridge_reg,'normalizeNeeded'),
        ('Lasso Regression', lasso_reg,'normalizeNeeded'),
        ('Decision Tree Regression', decision_tree_reg,'Non'),
        ('Random Forest Regression', random_forest_reg,'Non'),
        ('Gradient Boosting Regression', gradient_boosting_reg,'Non'),
        ('Support Vector Regression', svr_reg,'normalizeNeeded')
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

            # Calculate Mean Absolute Error (MAE)
            mae = mean_absolute_error(y_test, y_pred)

            # Calculate Mean Squared Error (MSE)
            mse = mean_squared_error(y_test, y_pred)
                
            # Calculate Mean Percentage Error (MSE)
            percentage_error = (mae / y_test.mean()) * 100
            if min_errorr > percentage_error:
                min_errorr = percentage_error
                best_result= subset
                best_model= model_name
            # print("Model:", model_name)
            # print("Mean Absolute Error (MAE:",mae)
            # print("Mean Squared Error (MSE):",mse)
            # print("percentage_error:",percentage_error)
            # print()
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
            if min_errorr > percentage_error:
                min_errorr = percentage_error
                best_result= subset
                best_model= model_name

            # print("Model:", model_name)
            # print("Mean Absolute Error (MAE:",mae)
            # print("Mean Squared Error (MSE):",mse)
            # print("percentage_error:",percentage_error)
            # print()
print("Best Model:", best_model)
print("Best percentage_error:", min_errorr)
for f in best_result:
    all_feature.remove(f)
print("Best feature selection:", all_feature)