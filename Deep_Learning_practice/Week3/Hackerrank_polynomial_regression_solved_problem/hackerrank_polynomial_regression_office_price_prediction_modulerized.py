# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def read_dataset(n_samples):
    
    data_matrix = []
    for i in range(n_samples):
        row = list(map(float, input().split()))
        data_matrix .append(row)
        
    data_matrix  = np.array(data_matrix)
    return data_matrix 

def read_test_features():
    X_test = []
    test_samples = int(input().strip())
    for i in range(test_samples):
        row = list(map(float, input().split()))
        X_test.append(row)
    
    X_test = np.array(X_test)
    return X_test

def extract_train_features_and_labels(data_matrix):
     # print(data_matrix[:,-1])
    # print(data_matrix[:, :-1])
    
    X_train = data_matrix[:, :-1]
    y_train = data_matrix[:,-1]
    
    return X_train , y_train 
    
if __name__ == "__main__":
    
    n_features , train_sample_cnt  = map(int , input().split())
    # print(n_samples , n_features)
    
    train_data = read_dataset(train_sample_cnt)
    X_train , y_train = extract_train_features_and_labels(train_data)
    
    # print("dimension of X_train :", X_train.shape)
    # print("dimension of y_train :", y_train.shape)
    # print(type(y_train))
    
    test_sample_cnt = int(input().strip())
    X_test = read_dataset(test_sample_cnt)
    # print(X_test.shape)
    
    # Constructing the polynomials of our Independent features 
    # poly_reg = PolynomialFeatures(degree = 3)
    # X_p = poly_reg.fit_transform(X_train)
    # print("dimension of X_p : ", X_p.shape)
    
    degree = 3
    poly_reg=make_pipeline(PolynomialFeatures(degree),LinearRegression())
    
    
    # Fitting Simple Linear Regression to the Training set
    # regressor = LinearRegression()
    # regressor.fit(X_p, y_train)
    poly_reg.fit(X_train, y_train)
    
    y_test = poly_reg.predict(X_test)
    # print("dimension of y_test : ", y_test.shape)
    # print(y_test)
    
    for value in y_test:
        print(round(value,2))
    
    # 1.0 2.0
    # 3.0 4.0
    # 5.0 6.0
