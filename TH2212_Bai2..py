def tim_soLN(a,b,c):
    Max=a
    if b>Max:
        Max=b
    if Max<c:
        Max=c
    return Max
v=tim_soLN(3,6,7)
print(f"gia tri lon nhat la: {v}")
def tim_soNN(d,e,f):
    Min=d
    if Min>e:
        Min=e
    if Min>f:
        Min=f
    return Min
n=tim_soNN(4,9,5)
print(f"gia tri nho nhat la: {n}")


