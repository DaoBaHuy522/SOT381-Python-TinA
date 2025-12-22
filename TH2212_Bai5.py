n=int(input("nhap tong lan thu n="))
def tu_mau():
    v=0
    for i in range(1,n+1):
        v=v+i
    m=0
    for i in range(2,n+1,2):
        m=m+i
    s=v/m
    return round(s,4)
print(f"ham tinh gia tri cua s={tu_mau()}")
    