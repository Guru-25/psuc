# Fibonacci series of n numbers

n=int(input())
x=0
y=1
fib=[]
if n==0:
    print("no elements")
elif n==1:
    print("0")
else:
    fib.append(x)
    fib.append(y)
    for i in range(n-2):
        z=x+y
        fib.append(z)
        x=y
        y=z
    print(*fib)
