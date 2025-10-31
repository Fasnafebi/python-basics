def stars(n,i=1):
    if i>n:
        return
    print("*"*i)
    stars(n,i+1)
try:
    rows=int(input("enter the number of rows:"))
    if rows<=0:
        print("error!")
    else:
        stars(rows)
except ValueError:
    print("error!")