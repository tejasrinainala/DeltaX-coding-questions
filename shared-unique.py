# Shared & Unique

# Description:
# Write a python program that takes two string values as input and returns a list of three elements, in the following order:
# a)Shared letters between two words.
# b)Letters unique to word 1
# c)Letters unique to word 2

# Constraints:
# • String values will be considered in lowercase.
# • If an element contains no alphabets, return an empty string
# • Even with multiple matching character there should be only 1 exist in the unique group
# • Each element should be alphabetically sorted and placed within the list

# Sample Input:
# sharp
# soap
# Sample Output:
# ['aps', 'hr', 'o']
# Explanation:
# String1 = sharp
# String2 = soap
# common letters = 'aps'
# unique letters in string1 = 'hr'
# unique letters in string2 = 'o'
# Hence the output = ['aps', 'hr', 'o']

a = input()
b = input()
repeated = ''
sr = ''
a_unique = ''
b_unique = ''
for i in a + b:
    if (i in a) and (i in b) and (i not in repeated):
        repeated += i
    elif (i in a) and (i not in b) and (i not in a_unique):
        a_unique += i
    elif (i not in a) and (i in b) and (i not in b_unique):
        b_unique += i
repeated = "".join(sorted(repeated))
a_unique = "".join(sorted(a_unique))
b_unique = "".join(sorted(b_unique))
print([repeated,a_unique,b_unique])
