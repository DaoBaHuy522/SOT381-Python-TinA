#lọc số chẵn số lẻ
a=int(input("nhap so bat dau ")) 
b=int(input("nhap so ket thuc: "))
ds=[]
for i in range(a,b+1):
    ds.append(i)
chan=0
le=0
for so in ds:
    if so%2==0:
        chan+=1
    else:
        le+=1
print(f"co {chan} so chan")
print(f"co {le} so le")