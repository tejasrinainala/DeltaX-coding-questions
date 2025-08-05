# Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

# Examples:

# Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
# Output: a[] = [2, 2, 3, 4], b[] = [7, 10]
# Explanation: After merging the two non-decreasing arrays, we get, 

# Constraints:
# 1 ≤ a.size(), b.size() ≤ 105
# 0 ≤ a[i], b[i] ≤ 107



class Solution:
    def mergeArrays(self, a, b):
        merged = a + b  # Combine both
        merged.sort()   # Sort the combined array
        for i in range(len(a)):
            a[i] = merged[i]  # First n elements into a
        for j in range(len(b)):
            b[j] = merged[len(a) + j]  # Remaining m elements into b
        return a,b

