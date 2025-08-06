# Description:
# Write a Python program that takes a string and replaces each letter with its appropriate position in the alphabet.
# a=1, b=2, c=3, …. y=25,z=26

# Constraint:
# •⁠  ⁠If any of the character given in the string is not a  letter, ignore it.
# •⁠  ⁠Treat the string in lowercase.

# Sample Input:
# code
# Sample Output:
# 3 15 4 5
# Explanation:
# Alphabet positions:
# a=1, b=2, c=3, …. y=25,z=26
# Our String is Code
# Alphabet’s positions –
# c=3
# o=15
# d=4
# e=5
# Hence the output: 3 15 4 5

# Input:
# code hash
# Output:
# 3 15 4 5 8 1 19 8

res = ''
s = input()
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in s:
    if i in a:
        res+=str(a.index(i)+1)
        res+=' '
print(res)

        
