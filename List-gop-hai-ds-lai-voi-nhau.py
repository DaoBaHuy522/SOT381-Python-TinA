#Gộp hai List số nguyên thành một List mới
x=int(input("ban muon ds1 cua ban co bao nhiu so luong: "))
ds1=[]
for i in range(x):
    dl_ds1=int(input(f"nhap du lieu cua ds1 lan{i+1}: "))
    ds1.append(dl_ds1)
y=int(input("ban muon ds2 cua ban co bao nhiu so luong: "))
ds2=[]
for l in range(x):
    dl_ds2=int(input(f"nhap du lieu cua ds2 lan{l+1}: "))
    ds2.append(dl_ds2)
print(f"du lieu cua ds1 va ds2 khi gop lai la")
print(f"DS={ds1+ds2}")