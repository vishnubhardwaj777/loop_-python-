num = int(input("enter a number -:"))
cnt = 0
while(num > 0):
    rem = num%10
    qu = num//10
    cnt = cnt + 1
    num = qu
print(cnt)    