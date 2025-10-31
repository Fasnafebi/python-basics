def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
try:
    num=int(input("enter a number:"))
    if num<=0:
        print("pls enter a positive number!")
    else:
        result=sum(num)
        print(f"sum from 1 to {num}is :{result}")
except ValueError:
    print("error!")
