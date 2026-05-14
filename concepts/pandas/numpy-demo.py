import numpy as np

arr1 = np.array([1,2,3,4,5])
print(arr1)

# BAsic operation (Mean, sum, etc.)
print("sum :",np.sum(arr1))
print("multiplication :",np.prod(arr1))
print("Sub :",arr1-1)
print("Divison :",arr1 / 2)

print("Mean:",np.mean(arr1))
print("Min: ",np.min(arr1))
print("Max: ",np.max(arr1))
print("std:",np.std(arr1))


# correct 2D array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

# Matrix Transformations 
transposed = arr2.T
print("\nTransposed Matrix: \n",transposed)

# Dot product of two matrices 
mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[5,6],[7,8]])
dot_product = np.dot(mat1, mat2)
print("\n Dot product: \n", dot_product)


# reshape
arr3 = arr2.reshape(3,2)
print(arr3)
