x=int(input("nhap so tu nhien n="))
k=x%2
h=x%3
if h==0 and k==0:
    print(f"{x} chia het cho 2 va 3")
elif k==0:
    print(f"{x} chi chia het cho 2")
elif h==0:
    print(f"{x} chi chia het cho 3")