# import tensorflow as tf
import numpy as np
import pandas as pd
a = np.array([[1,2,3],[4, 5, 6], [7, 8, 9]])
b= np.array([[1,2,3],[4, 5, 6], [7, 8, 9]])
def multply_by_number(a,b,n):
    for i in a:
        for l in i:
            b = np.append(b, l * n)
            print(b)
    b = np.delete(b, 0)
    b = np.delete(b, 0)
    b = b.reshape(3, 3)
    print(f"old Value: \n{a}")
    print(f"new Value: \n{b}")
# multply_by_number(a,b,10)
def multply_by_list(a,b):
    for i in a:
        for I in b:
            b = np.append(b, i * I)
            print(b)
    b = np.delete(b, 0)
    b = np.delete(b, 0)

    # print(f"old Value: \n{a}")
    # print(f"new Value: \n{b}")
multply_by_list(a,b)
# data = pd.read_csv("data/test.csv")
# print(data.iloc[9])