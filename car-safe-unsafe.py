x , y = map(int,input().split())
position = input().upper()
flag = False
if x <= 1 and y <= 1:
    print("Unsafe")
else:
    for i in range(1,x+1):
        for j in range(1,y+1):
            n = i
            m = j
            for k in position:
                if k == 'L':
                    m-=1
                elif k == 'R':
                    m+=1
                elif k == 'F':
                    n-=1
                elif k == 'B':
                    n+=1
                if n > x and m > y or n <= 0 or m <= 0:
                    break
            if n <= x and m <= y or n > 0 or m > 0:
                    flag = True
if flag:
    print("Safe")

            
            
            
