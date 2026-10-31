import numpy as np

# a = np.array([1,2,3,4, 5, 6, 7, 8, 9])
# b= np.array([1,2,3,4, 5, 6, 7, 8, 9])
a=np.array([1,2,3])
b=np.array([4,5,6])
def multply_by_number(a,b,n):
    for i in a:
        for l in i:
            b = np.append(b, l * n)
            
    b = np.delete(b, 0)
    b = np.delete(b, 0)
    b = b.reshape(3, 3)
    print(f"old Value: \n{a}")
    print(f"new Value: \n{b}")
# multply_by_number(a,b,10)
def multply_by_list(a,b):
    total = 0
    for n_from_a in a:
        for n_from_b in b:
            total += n_from_a * n_from_b
            
    
    return total
    # print(f"old Value: \n{a}")
    # print(f"new Value: \n{b}")
