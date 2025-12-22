#tinh dien tich vs chu vi tam giac
a=int(input("nhap canh thu nhat a= "))
b=int(input("nhap canh thu hai b= "))
c=int(input("nhap canh thu ba c= "))
cv=a+b+c
print(f"chu vi tam giac la: {cv:.2f}")
r=cv/2
import math
s=math.sqrt(r*(r-a)*(r-b)*(r-c))
print(f"dien tich hinh vuong la: {s:.2f}")
