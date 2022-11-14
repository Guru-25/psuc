'''
Generate the Fibonacci sequence based on the given first number x and second number y. Each number thereafter is the sum of the two preceding numbers. Ask the user how many Fibonacci numbers to generate. From the generated numbers, print the numbers that are divisible either by 5 or 7. If no such elements, print "no element". Also print the sum of all the numbers.

Example: x=4, y=5, count=4, Fibonacci sequence: 4 5 9 14 Output: divisible by 5 or 7: 5 14 sum: 32

https://www.hackerrank.com/contests/psuc-ch2/challenges/python-lab1-ch2/problem
'''

x=int(input()) 
y=int(input()) 
count=int(input())
if count==0:
    print("no element")
    print("0")
elif count==1:
    if x%5==0 or y%7==0:
        print(x)
    else:
        print("no element")
    print(x)
else:
    def fib(x,y,count): 
        l=[] 
        l.append(x) 
        l.append(y) 
        for i in range(count-2):
            total=x+y 
            x=y
            y=total
            l.append(total)
        return l
    ok=0
    ll=[]
    z=fib(x,y,count)
    for i in z:
        if i%5==0 or i%7==0:
            ok=1
            ll.append(i)
    if ok==0:
        print("no element")
    else:
        print(*ll)
    print(sum(z))
