import  numpy as np
import matplotlib.pyplot as plt
def myfunc(x):
	f=-(x-2)**2 + 4 
	return f

def mytrapz(a,b):
	dx=(b-a)/100.0
	integral=0
	for i in range(100):
		x=a+i*dx
		print(dx,x,i,myfunc(x))
		integral=myfunc(x)*dx+integral
	return integral



x=np.arange(0,4,0.1)

pythonanswer=np.trapz(myfunc(x),x)
print(mytrapz(0,4),pythonanswer)


plt.plot(x,myfunc(x))
plt.show()