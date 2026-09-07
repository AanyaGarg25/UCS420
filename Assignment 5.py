import numpy as np

# Q1

arr = np.array([1, 2, 3, 4, 5])

print("Original array:", arr)
print("Addition in array:", arr + 2)
print("Multiplication in array:", arr * 3)
print("Division in array:", arr / 2)


# Q2(a)

arr = np.array([1, 2, 3, 6, 4, 5])

print("\nReversed array:", arr[::-1])


# Q2(b)(i)

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])

values, counts = np.unique(x, return_counts=True)
most_frequent = values[np.argmax(counts)]
indices = np.where(x == most_frequent)[0]

print("\nArray x:", x)
print("Most frequent value in x:", most_frequent)
print("Indices in x:", indices)


# Q2(b)(ii)

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

values, counts = np.unique(y, return_counts=True)
most_frequent = values[np.argmax(counts)]
indices = np.where(y == most_frequent)[0]

print("\nArray y:", y)
print("Most frequent value in y:", most_frequent)
print("Indices in y:", indices)


# Q3

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2-D Array:")
print(arr)

print("1st row, 2nd column:", arr[0, 1])
print("3rd row, 1st column:", arr[2, 0])


# Q4

Aanya = np.linspace(10, 100, 25)

print("\nArray Aanya:")
print(Aanya)

print("Dimensions:", Aanya.ndim)
print("Shape:", Aanya.shape)
print("Total elements:", Aanya.size)
print("Data type:", Aanya.dtype)
print("Total bytes:", Aanya.nbytes)

transpose_array = Aanya.reshape(25, 1)

print("Transpose using reshape:")
print(transpose_array)

transpose_T = Aanya.reshape(25, 1).T

print("Transpose using T:")
print(transpose_T)


# Q5

ucs420_Aanya = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 15, 20, 35]
])

print("\nOriginal Array:")
print(ucs420_Aanya)

print("Mean:", np.mean(ucs420_Aanya))
print("Median:", np.median(ucs420_Aanya))
print("Maximum:", np.max(ucs420_Aanya))
print("Minimum:", np.min(ucs420_Aanya))
print("Unique Elements:", np.unique(ucs420_Aanya))

reshaped_ucs420_Aanya = ucs420_Aanya.reshape(4, 3)

print("Reshaped Array:")
print(reshaped_ucs420_Aanya)

resized_ucs420_Aanya = np.resize(ucs420_Aanya, (2, 3))

print("Resized Array:")
print(resized_ucs420_Aanya)