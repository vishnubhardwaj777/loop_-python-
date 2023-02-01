num = int(input("enter a start number -:"))
ans = 0
for i in range(num):
    ans = ans + (i*i*i)
ans = ans + (num*num*num)    
print(ans)