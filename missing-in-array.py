# You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

# Examples:

# Input: arr[] = [1, 2, 3, 5]
# Output: 4
# Explanation: All the numbers from 1 to 5 are present except 4.

# Constraints:
# 1 ≤ arr.size() ≤ 106
# 1 ≤ arr[i] ≤ arr.size() + 1



class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1  
        total = n * (n + 1) // 2
        actual = sum(arr)
        return total - actual

            
            
