a=int(input("nhap gia tri a"))
b=int(input("nhap gia tri b"))
c=int(input("nhap gia tri c"))
Max=a
Min=a
if b>Max:
    Max=b
if Max<c:
    Max=c
if Min>b:
    Min=b
if Min>c:
    Min=c
print(f"gia tri lon nhat la: {Max}")
print(f"gia tri nho nhat la: {Min}")
