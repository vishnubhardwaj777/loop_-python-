num = int(input("enter a number -:"))
ans = 1
for i in range(num):
    ans = num * ans
    num = num - 1
#ans = ans * num
print(ans)    
