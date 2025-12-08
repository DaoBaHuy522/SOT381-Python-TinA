#viet nhap 1 so nguyen cho biet co cho het dong thoi 3 va 5 hay ko
a=int(input(f"nhap so a "))
h=a%3
k=a%5
if h==0 or k==0:
    print("ca 3 va 5 deu chia het")
else:
    if h==0:
       print("chia het cho3")
    if k==0:
       print(" chia het cho5")
