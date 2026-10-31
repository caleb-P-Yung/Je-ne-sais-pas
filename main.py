import tensorflow as tf
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# # a = np.array([1,2,3,4, 5, 6, 7, 8, 9])
# # b= np.array([1,2,3,4, 5, 6, 7, 8, 9])
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# def multply_by_number(a,b,n):
#     for i in a:
#         for l in i:
#             b = np.append(b, l * n)
            
#     b = np.delete(b, 0)
#     b = np.delete(b, 0)
#     b = b.reshape(3, 3)
#     print(f"old Value: \n{a}")
#     print(f"new Value: \n{b}")
# # multply_by_number(a,b,10)
# def multply_by_list(a,b):
#     total = 0
#     for n_from_a in a:
#         for n_from_b in b:
#             total += n_from_a * n_from_b
            
    
#     return total
#     # print(f"old Value: \n{a}")
#     # print(f"new Value: \n{b}")

# import the data
data_test = pd.read_csv("data/test.csv")

data_train = pd.read_csv("data/train.csv")


# make data points
x_test = data_test["x"].tolist()
y_test = data_test["y"].tolist()

x_train=data_train["x"].tolist()
y_train=data_train["y"].tolist()


# Create the plot
plt.scatter(x_test, y_test, color='blue', s=50, marker='o')
plt.scatter(x_train, y_train, color='black', s=50, marker='o')
# Customize and show
plt.title("AI Plot")
plt.grid(True)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()