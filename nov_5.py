# 1. Find the last digit of the number entered

n=int(input())
last_digit=n%10
print(last_digit)

# 2. Find the area of circle for the given valid radius

r=int(input())
area=3.14*r**2
print(area)

# 3. Find the quadrant value of the given month. (ex. March - Quadrant 1, May - Quadrant 2)

month=input()
if month=="January" or month=="February" or month=="March" or month=="April":
    print("Quadrant 1")
elif month=="May" or month=="June" or month=="July" or month=="August":
    print("Quadrant 2")
elif month=="September" or month=="October" or month=="November" or month=="December":
    print("Quadrant 3")
else:
    print("Please enter a valid Month")
    
# 4. Print all the two digit numbers that are ends with 2 or 4. 

for i in range(10,99,10):
    a=i+2
    b=i+4
    print(a)
    print(b)
    
# 5. Print the first 10 numbers that are divisible by both 3 and 4

for i in range(12,132):
    if i%12==0:
        print(i)
