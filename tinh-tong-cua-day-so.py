x=int(input("U1= "))
n=int(input("n= "))
d=int(input("d= "))
if d!=0:  
    S=x*n+(n-1)*d/2
    print("tong cua day so S= ",S)
else:
    Un=int(input("Un= "))
    S=n*(x+Un)/2
    print("tong cua day so S= ",S)