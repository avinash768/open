import numpy as np

# Define the size of the square matrix (n x n)
n = 5

# Create a random integer array of shape (n, n)
random_array = np.random.randint(1, 10, size=(n, n))

# Calculate the mean of the entire array
mean_value = random_array.mean()

# Replace the values in the right diagonal with the mean
for i in range(n):
    random_array[i, n - i - 1] = mean_value

# Print the original array and the modified array
print("Original Array:")
print(random_array)
