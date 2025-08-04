# Given an array arr[] of positive integers and an integer k, Your task is to return k largest elements in decreasing order. 

# Example:

# Input: arr[] = [12, 5, 787, 1, 23], k = 2
# Output: [787, 23]
# Explanation: 1st largest element in the array is 787 and second largest is 23.

# Constraints:
# 1 ≤ k ≤ arr.size() ≤ 106
# 1 ≤ arr[i] ≤ 106


class Solution:
	def kLargest(self, arr, k):
	    arr.sort(reverse=True)
	    c=0
	    res = []
	    for i in range(0,k):
	        res.append(arr[i])
	    return res
	        
	        
