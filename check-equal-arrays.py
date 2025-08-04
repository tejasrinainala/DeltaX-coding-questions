# Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.
# Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.
# Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

# Example:

# Input: a[] = [1, 2, 5, 4, 0], b[] = [2, 4, 5, 0, 1]
# Output: true
# Explanation: Both the array can be rearranged to [0,1,2,4,5]


# Constraints:
# 1 ≤ a.size(), b.size() ≤ 107
# 0 ≤ a[i], b[i] ≤ 109

class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False

        freqA = {}
        for i in a:
            if i in freqA:
                freqA[i] += 1
            else:
                freqA[i] = 1

        freqB = {}
        for i in b:
            if i in freqB:
                freqB[i] += 1
            else:
                freqB[i] = 1

        return freqA == freqB
