x=int(input("nhap do dai = "))
y=int(input("nhap do rong ="))
if x==y:
    print("hinh vuong")
else:
    print("hinh chu nhat")
    k=2*x+2*y
    h=x**2+y**2
    print(f"dien tich hinh chu nhat la = {h}")
    print(f"chu vi hinh chu nhat la = {k}")