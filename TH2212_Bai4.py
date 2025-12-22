def tim_so(a,b,c):
    Max=a
    if b>Max:
        Max=b
    if Max<c:
        Max=c
    Min=a
    if Min>b:
        Min=b
    if Min>c:
        Min=c
    return Max,Min
Max,Min=tim_so(2,8,5)
print(f"gia tri lon nhat la: {Max}")
print(f"gia tri nho nhat la: {Min}")

