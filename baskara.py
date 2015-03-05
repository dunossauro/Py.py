import math

def baskara(a,b,c):

	delta = (b**2)-((4*a)*c)

	
	if delta < 0:
		print("Delta menor que 0")
		exit()

	d = math.sqrt(delta)
	

	print(-b+d/(2*a))

	print(-b-d/(2*a))

a = float(input("digite o valor de a:	"))
b = float(input("digite o valor de b:	"))
c = float(input("digite o valor de c: 	"))

baskara(a,b,c)
