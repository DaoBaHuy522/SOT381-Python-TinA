#Kiểm tra số x có trong List không, nếu có thì ở vị trí nào
n = int(input("nhập số lượng danh sách n="))
ds = []

for i in range(n):
    d = float(input(f"nhập số con số thứ {i+1} là: "))
    ds.append(d)

#thực hiện chương trình
w = float(input("nhập con số bạn cần tìm: "))
coko = w in ds
print(coko)
if coko == True:
    print(f" có số {w} nằm trong danh sách")
    vi_tri = ds.index(w)
    print(f" nó nằm ở vị trí thứ {vi_tri+1}")
    so_lan=ds.count(w)
    print(f" số lần mà số xuất hiện {w} là: {so_lan}")
else:
    print(f"số {w} nó không nằm trong danh sách")