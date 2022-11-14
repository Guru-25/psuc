'''
2. Design a simple EB bill calculator. Get the number of units consumed from the user. Based on the following units price tariff, calculate the bill. 
<=200 units - Rs.1.5/unit
<=500 units - Rs.2.5/unit
<=1000 units - Rs.5/unit
>1000 units - Rs.7/unit
(Example: For 700 units, cost is 200x1.5 + 300x2.5 + 200x5)
'''

x=int(input())
if 0<x<=200:
    ok=(x-0)*1.5
    print(ok)
elif 200<x<=500:
    ok1=200*1.5+(x-200)*2.5
    print(ok1)
elif 500<x<=1000:
    ok2=200*1.5+300*2.5+(x-500)*5
    print(ok2)
elif x>1000:
    ok3=200*1.5+300*2.5+500*5+(x-1000)*7
    print(ok3)
else:
    print("Please enter a valid input")
