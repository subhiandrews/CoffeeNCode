#!/usr/bin/python3
# Let's say you have 2 equal length list of integers and you want to find the difference between the two lists
# difference calculated by subtracting the element at index i of list 2 from that of list1
#  
import time
arr1 = [5, 6, 7, 8, 9, 10, 11, 12]
arr2 = [3, 4, 5, 6, 7, 8, 9, 10]

#result of this should be [2, 2, 2]

result = [0] * len(arr1)

start = time.time() * 1000000
for i in range(len(arr1)):
    result[i] = arr1[i] - arr2[i]
stop = time.time() * 1000000

print("Difference: {}".format(result))
print("Time taken by For Loop: {}".format(stop - start))

start = time.time() * 1000000
result = [ arr1[i] - arr2[i] for i in range(len(arr1)) ]
stop = time.time() * 1000000

print("Difference: {}".format(result))
print("Time taken by List Comprehension: {}".format(stop - start))


