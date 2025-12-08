#tim so nguyen to
x=int(input("nhap so bat dau: "))
y=int(input("nhap so gioi han: "))
h=0
if x>0 and y>x:
    while h<8:
        h=h+1
        if h==4 or h==6 or h==8:  
            continue
        print(h)
for u in range(x,y):
    if h>=8:
        k=u%2
        p=u%3
        l=u%5
        g=u%7
        if k==0 or p==0 or l==0 or g==0 or u==1:
            continue
        print(u)
        
        


    
    
        
        
        
        
     
    
    
        
        
        
         
               