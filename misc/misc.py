# def smallestDifferenceTriplet(arr1, arr2, arr3, n):
#     arr1.sort()
#     arr2.sort()
#     arr3.sort()

#     res_min, res_max, res_mid = 0, 0, 0
#     i, j, k = 0, 0, 0
#     diff = float('inf')

#     while i < n and j < n and k < n:
#         s = arr1[i] + arr2[j] + arr3[k]
#         max_val = max(arr1[i], arr2[j], arr3[k])
#         min_val = min(arr1[i], arr2[j], arr3[k])

#         if min_val == arr1[i]:
#             i += 1
#         elif min_val == arr2[j]:
#             j += 1
#         else:
#             k += 1

#         if diff > (max_val - min_val):
#             diff = max_val - min_val
#             res_max = max_val
#             res_mid = s - (max_val + min_val)
#             res_min = min_val

#     return [res_max, res_mid, res_min]

# # Example usage:
# arr1 = [1, 2, 3]
# arr2 = [4, 5, 6]
# arr3 = [7, 8, 9]
# n = len(arr1)  # Assuming all arrays have the same length

# print(smallestDifferenceTriplet(arr1, arr2, arr3, n))  # Output will be the smallest difference triplet


# def reverseWord(str: str) -> str:
#     l = len(str)
#     # print(l)
#     str_list = list(str)
#     # print(str_list)
#     start = 0
#     end = l-1
    
#     while end - start >= 1:
#         temp = str_list[start]
#         str_list[start] = str_list[end]
#         str_list[end] = temp
        
#         start += 1
#         end -= 1
    
#     word =''
#     for letter in str_list:
#         word += letter
#     return word

# print(reverseWord('hruday'))

# def binarySearch(target, left_index, right_index, arr):
#     if left_index <= right_index:
#         mid = (left_index + right_index) // 2
#         print(left_index, mid, right_index)

#         if target == arr[mid]:
#             return mid
#         elif target < arr[mid]:
#             return binarySearch(target, left_index, mid - 1, arr)
#         else:
#             return binarySearch(target, mid + 1, right_index, arr)

#     return -1

# print(binarySearch(12, 0, 5, [1, 5, 9, 10, 11, 12]))

# #using loops
# def subArray(array):
#     subArrays = []
#     length = len(array)
#     for l in range(1, length+1):
#         for arr in range(length-l+1):
#             subArrays.append(array[arr:arr+l])

#     return subArrays

# print(subArray([1,2,3,4]))

# #using recursion
# subArrays = []
# def subArrayRec(array):
#     l = len(array)
#     if l >= 2:
#         subArrays.append(array)
#         subArrayRec(array[0:l-1])
#         subArrayRec(array[1:l])
#     return subArrays

# print(subArrayRec([1,2,3]))

# #Input : [1, 2, 3]
# #Output : [1], [1, 2], [2], [1, 2, 3], [2, 3], [3]


# def printSubArrays(arr, start, end):
     
#     # Stop if we have reached the end of the array    
#     if end == len(arr):
#         return
     
#     # Increment the end point and start from 0
#     elif start > end:
#         return printSubArrays(arr, 0, end + 1)
         
#     # Print the subarray and increment the starting
#     # point
#     else:
#         print(arr[start:end + 1])
#         return printSubArrays(arr, start + 1, end)
         
# # Driver code
# arr = [1, 2, 3]
# printSubArrays(arr, 0, 0)






