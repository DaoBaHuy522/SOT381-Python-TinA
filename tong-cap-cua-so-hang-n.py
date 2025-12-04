#canh tinh tong cap so cong
x=int(input("nhap so bat dau: "))
y=int(input("nhap so lon nhat: "))
z=int(input("nhap so buoc nhay: "))
k=x
while x<y:
       x=x+z
#tong Sn so hang
n=(x-k-z)/z
print(f"tong so hang cua {n} so hang bang: {x-z}")