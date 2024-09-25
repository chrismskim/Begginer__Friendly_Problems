# Initialize global variable to store the position of the found element
pos = -1

# Function to search for a value in the array
def search(arr, n):
    i = 0
    while i < len(arr):
        if arr[i] == n:
            globals()['pos'] = i  # Update global variable 'pos' with the index of the found element
            print("Found here")
            return True
        i = i + 1
    return False

# Import array module
from array import *

# Create an empty integer array
arr = array('i', [])

# Input: Length of the array
n = int(input("Enter the length of the array: "))

# Input: Elements of the array
print("Enter the elements:")
for i in range(n):
    x = int(input())
    arr.append(x)

# Input: Value to be searched
s = int(input("Enter the value to be searched: "))

# Search for the value in the array
if search(arr, s):
    print(f"Found at position {pos}")
else:
    print("Not found")

