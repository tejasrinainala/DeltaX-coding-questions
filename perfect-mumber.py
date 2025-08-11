# Perfect Number and Divisors

# Have you heard of Perfect numbers? If not
# let me tell you what is it, Perfect Numbers are integers that are equal to the
# sum of all its divisors except that number itself.


# Now, given an integer  N ,write a program to print true


# if it is a perfect number or false if it
# is not a


# perfect number.

# Input format

# The first line contains the number of
# test cases T.

# Each test case contains an integer N is provided.


# Output format

# For each test case on a new line, print
# true or false depending on N.

# Constraints

# 1<=T<=10

# 1<=N<=100

# Time Limit : 1  second

# Example

# Input

# 2

# 28

# 96

# Output
# true
# false


n = int(input())
arr = []
s = 0
for i in range(n):
    arr.append(int(input()))
for i in range(len(arr)):
    s = 0
    for j in range(1,arr[i]):
        if arr[i] % j == 0:
            s+=j
    if s == arr[i]:
        print(True)
    else:
        print(False)
            
