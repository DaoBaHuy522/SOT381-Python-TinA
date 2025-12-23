n=int(input("nhapp so luong bai hat n="))
ds=[]
for i in range(1,n+1):
    bai=input(f"bai thu {i} la: ")
    ds.append(bai)
#chu viet thuong
print("Danh sach vua nhap la:")
for h in range(n):
    print(ds[h])
#chu viet hoa
print("Danh sach cac bai ở dạng viết hoa:")
for k in range(n):
    DS=ds[k].upper()
    print(DS)

print("tìm ra bài trong danh sách có chữ yêu")
for l in range(n):
    hat=ds[l]
    if hat.find("yêu") != -1:
        print(hat)
        
print("tìm tư dai nhất")
baii=ds[0]
so_tuu=len(baii.split())
for f in range(1,n):
    bai=ds[f]
    so_tu= len(bai.split())
    if so_tu>so_tuu:
        so_tuu=so_tu
        baii=bai
print(so_tuu,baii)
    
