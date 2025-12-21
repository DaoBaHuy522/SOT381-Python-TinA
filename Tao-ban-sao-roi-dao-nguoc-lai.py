#LIST//tao ban sao dao nguoc cua mot list
ds=[]
for i in range(1,10):
    ds.append(i)
print(f"thu tu ban dau {ds}")
ban_sao=ds.copy()
print(f"dao nguoc lai {ban_sao[::-1]}")