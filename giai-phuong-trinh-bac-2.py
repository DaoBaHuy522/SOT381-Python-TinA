#viết chương trình bậc 2 hoàn chỉnh
print("a**2*x+b*x+c=0 ,(a!=0)")
a=int(input("nhap a"))
b=int(input("nhap b"))
c=int(input("nhap c"))
print(a,"**2*x+",b,"*x",c)
if a!=0:
    delta=a**2+4*a*c
    import math
    dellta=math.sqrt(delta)
    if delta>0:
        print("phuong trinh co 2 nghiem")
        x1=(-b-dellta)/2*a
        x2=(-b+dellta)/2*a
        print("x1= ",x1)
        print("x2= ",x2)
    else:
        if delta==0:
            print("phuong trinh co nghiem kep")
            x=-b/(2*a)
            print("x= ")
        else:
             print("phuong trinh vo nghiem")
else:                   
    print("khong phai phuong trinh bac 2")
        