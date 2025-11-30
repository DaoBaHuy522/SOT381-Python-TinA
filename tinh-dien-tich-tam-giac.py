x1=int(input("nhap x1= "))
y1=int(input("nhap y1= "))
print("toa do A( ",x1," ; ",y1," )")
x2=int(input("nhap x2= "))
y2=int(input("nhap y2= "))
print("toa do B( ",x2," ; ",y2," )")
x3=int(input("nhap x3= "))
y3=int(input("nhap y3="))
print("toa do C( ",x3," ; ",y3," )")
a=x1-x2
b=y1-y2
print("vecto AB =( ",a," ; ",b," )")
c=x2-x3
d=y2-y3
print("vecto BC =( ",c," ; ",d," )")
e=x3-x1
f=y3-y1
print("vecto CA =( ",e," ; ",f," )")
import math
AB=math.sqrt(a**2+b**2)
print("do dai AB= ",AB)
BC=math.sqrt(c**2+d**2)
print("do dai BC= ",BC)
CA=math.sqrt(e**2+f**2)
print("do dai AC= ",CA)
if a/c!=b/d and c/e!=d/f and e/a!=f/b:
    if a*c+b*d==0:
        print("tam giac vuong tai B")
        S=AB*BC/2
        print("dien tich tam giac vuong S= ",S)
    else:
        if c*e+d*f==0:
            print("tam giac vuong tai C")
            S=BC*CA/2
            print("dien tich tam giac vuong S= ",S)
        else:
                if a*e+b*f==0:
                    print("tam giac vuong tai A")
                    S=CA*AB/2
                    print("dien tich tam giac vuong S= ",S)
                else:
                        if AB==BC and BC==CA and CA==AB:
                            print("tam giac deu")
                            import math
                            S=AC**2*(math.sqrt(3)/4)
                            print("dien tich tam giac dieu S= ",S)
                        else:
                                p=(AB+BC+CA)/2
                                SS=p*(p-AB)*(p-BC)*(p-CA)
                                import math
                                S=math.sqrt(SS)
                                print("dien tich tam giac S= ",S)
else:
    print(" 3 diem khong tao ra tam giac, vi toa do 3 diem nam cung tren 1 duong thang")