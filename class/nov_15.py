# summation of n numbers

n=int(input())
sum1=0
for i in range(n+1):
    sum1=sum1+i
print(sum1)

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
    
# check perfect number or not

n=int(input())
sum1=0
for i in range(1,n):
    if n%i==0:
        sum1=sum1+i
if sum1==n:
    print("perfect number")
else:
    print("not a perfect number")
    
# check whether prime number or not

n=int(input())
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not a prime number")
            break
    else:
        print("prime number")
else:
    print("not a prime number")
    
    
