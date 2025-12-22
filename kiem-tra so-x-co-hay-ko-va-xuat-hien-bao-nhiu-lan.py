#LIST kiểm tra số x có hay ko va xuất hiện bao nhiu lần
n=int(input("nhap so lan danh sach: "))
ds=[]
for i in range(n):
    x=int(input(f"nhap du lieu vao danh sach lan thu {i+1}: "))
    ds.append(x)
print(f"ds={ds}")
g=int(input("kiem tra so do co ton tai hay khong"))
h=int(input("ban can tim vi tri: "))
k=int(input("muon biet no xuat hien bao nhiu lan: "))
ton_tai=g in ds
if ton_tai==True:
    print(f"so {g} co ton tai")
else:
    print(f"so {g} khong ton tai")
dem_so=ds.count(k)
vi_tri=ds.index(h)
print(f"so lan lap cua {k} la {dem_so} lan")
print(f"vi tri cua {h} la {vi_tri}")