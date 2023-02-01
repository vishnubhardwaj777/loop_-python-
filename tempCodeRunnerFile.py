num = int(input("enter a start number -:"))
ans = 0
for i in range(num):
    if(i%2 != 0):
        ans = ans + i
if(num%2 != 0):
        ans = ans + num
        print(ans)
print(ans)   