num = int(input("enter a start number -:"))
ans = 0
for i in range(num):
    ans = ans + (i*i)
ans = ans + (num*num)    
print(ans)