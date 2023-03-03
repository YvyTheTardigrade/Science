import matplotlib.pyplot as plt
import numpy as np
from sympy import *

#you can write below the x and y coordinates of your points 

coordx=[]
coordy=[]


def p(x):
	y=0
	title=0
	for i in range(len(coordx)):
		p=1
		for j in range(len(coordx)):
			if j!= i:
			
				p=p*(x-coordx[j])/(coordx[i]-coordx[j])
		y += coordy[i]*p
	return y


def title():
	x= symbols("x")
	y=0
	title=0
	for i in range(len(coordx)):
		p=1
		for j in range(len(coordx)):
			if j!= i:
				p=p*(x-coordx[j])/(coordx[i]-coordx[j])
		y += coordy[i]*p
	return simplify(y)
	

x= np.linspace(-2*np.abs(min(coordx)),np.abs(max(coordx))*2, 150)
y= p(x)
plt.plot(x,y,"b")
plt.axvline(x=min(coordx),color='red',linestyle='--')
plt.axvline(x=max(coordx),color='red',linestyle='--')

plt.title(title())
plt.xlabel('x')
plt.ylabel('y')

plt.ylim(min(coordy)-10,max(coordy)+10)
plt.grid()

plt.show()
	
