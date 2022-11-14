'''
A cone and sphere having the same radious are melted and recast into a cylinder. The radious and height of the cone are R and H. If the radious of the cylinder so formed is 2cm, find the height of the cylinder (CH).

https://www.hackerrank.com/contests/psuc-ch1/challenges/python-lab1-ch1/problem
'''

r=int(input())
h=int(input())
rCy=2
vCy=(1/3)*3.14*r**2*h
vSp=3.14*r**3*(4/3)
hCy=(vCy+vSp)/(3.14*rCy**2)
print(round(hCy,2))
