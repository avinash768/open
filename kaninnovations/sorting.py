arr = [8,10,9,7,6,5,4,3,2,1,1,0]

 # Implement the bubble sort algorithm
n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
             # Swap the elements if they are in the wrong order
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Print the sorted array
print("Original Array:", arr)