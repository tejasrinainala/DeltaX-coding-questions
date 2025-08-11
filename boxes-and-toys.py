# Boxes and Toys

# Tina and Rahul have 1 toy each. They are entering into an amusement park but it is not allowed to take the toys inside, so they have to keep it in the boxes provided by the park management. They want to keep the toys together in one box. There are N boxes in total, at this moment there are ti toys present in ithℎ box and the maximum capacity of the box is denoted by ci. Rahul and Tina want to know in how many boxes can they keep their toys such that both the toys are in the same box.

# Input format

# The first line of the input contains integer N, denoting the count of boxes. Each of the next N lines contains two integers ti and ci denoting the number of toys present in the ithℎ box and the maximum capacity of that box.

# Output format

# Print the maximum number of boxes that fulfill the conditions.

# Constraints
# 1<=N<= 100 and 1<=ti,ci<=1000
# Time Limit : 1 second

# Example

# Input

# 4
# 1 2
# 2 4
# 5 6
# 6 10

# Output
# 2
# Sample test case explanation
# It is only possible to keep both the toys in box2 and box4.


n = int(input())
p = []
c  = 0
for i in range(n):
    a,b = map(int,input().split())
    p.append((a,b))
for i in range(len(p)):
    if abs(p[i][0]-p[i][1]) >= 2:
        c+=1
print(c)
        
