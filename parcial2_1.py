import math
def dist(a,b,c,d):
	p=c-a
	q=d-b
	p=p*p
	q=q*q
	r=p+q
	resp= math.sqrt(r)
	return resp

x1= int(input("x1: "))
y1= int(input("y1: "))
x2= int(input("x2: "))
y2= int(input("y2: "))
hyp= dist(x1,y1,x2,y2)
print("Hypotenuse",hyp)
