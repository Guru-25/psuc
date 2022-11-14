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
    
'''
2. Assume that a person bought a cylinder shaped container full of milk. He took a small cone shape of a container and pour milk from the cylinder container. 
a) Get the cylinder and cone measurements from user
b) Find the total volume of both the containers in liters. (use formula)
c) Find the remaining milk after pouring. 
d) check the cylinder measurements are greater than the cone measurements
'''

rCy=int(input())
hCy=int(input())
rCo=int(input())
hCo=int(input())
volCy=3.14*rCy**2*hCy
volCo=(1/3)*3.14*rCo**2*hCo
volume=volCy+volCo
print(volume)
remVolume=volCy-volCo
print(remVolume)
if rCy and hCy > rCo and hCo:
    print("True")
else:
    print("False")

