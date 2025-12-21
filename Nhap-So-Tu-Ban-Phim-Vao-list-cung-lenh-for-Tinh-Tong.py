#tính tổng 5 số nhập từ banf phím list cùng với lệnh for
x=int(input("nhap so phan tu la: "))
ds=[]
for i in range(x):
    a=int(input(f"nhap so thu {i} la: "))
    ds.append(a)
o=sum(ds)
print(f"tong so {x} phan tu la: {o}")