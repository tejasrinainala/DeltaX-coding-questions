n = int(input())
l = []
c = 0
for k in range(n):
    l.append(int(input()))
for i in range(len(l)):
    c = 0
    for j in range(1,l[i]+1):
        if l[i] % j == 0:
            c+=1
    if c % 2!= 0:
        print("YES")
    else:
        print("NO")
                
# A number is called a smart number if it has an odd number of factors. Given some numbers, find whether they are smart numbers or not.
# Debug the given function is_smart_number to correctly check if a given number is a smart number.
# Note: You can modify only one line in the given code and you cannot add or remove any new lines.
# To restore the original code, click on the icon to the right of the language selector.
# Input Format
# The first line of the input contains  t, the number of test cases.
# The next  t  lines contain one integer each.
# Constraints
# 1≤t≤10^3.
# 1≤n sufix i ≤10^4, where n sufix i is the i th integer.
# Output Format
# The output should consist of  t  lines. In the i th  line print YES if the i th integer has an odd number of factors, else print NO.

# Sample Input
# 4
# 1
# 2
# 7
# 169
# Sample Output
# YES
# NO
# NO
# YES
