import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc
import numpy as np
from pylab import *
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.ticker as ticker
import matplotlib.colors as color

class Page_Slider(matplotlib.widgets.Slider):

    def __init__(self, ax, variable, label, var_init,val_fmt):

        self.variable = variable
        super(Page_Slider,self).__init__(ax, label, 1, variable, valinit=var_init, valfmt=val_fmt)


def boundary_conditions(C_bc,j):
	C_bc[0]=C_bc[1]
	C_bc[-1]=C_bc[-2]+dr/D_s*j
	return C_bc

def finite_one_timestep(C_local):
	'''
	Takes in just the radial part and give the radial part of 
	the next time step
	'''
	C_next_T_step_local=C_local
	for i in range(1,r.shape[0]-1):
		C_next_T_step_local[i]=C_local[i]+D_s * dt * (2.0/r[i]*(C_local[i+1]-C_local[i])/dr + \
			(C_local[i+1]-2.0*C_local[i]+C_local[i-1])/dr**2)
	return C_next_T_step_local

D_s=1e-14
R=1e-5
C_max=12000.0
tol=C_max/10.00
J_0=9.5e-6

C_0=9500.0

dr=1e-6
dt=0.01
# number of points in time 
nT=180000
print(nT*dt)
j=np.ones(nT)*J_0

r=np.arange(0,R,dr)

C_prev_T_step=np.ones(r.shape[0])*C_0
C_next_T_step=np.zeros(r.shape[0])
C_t=np.ones((nT,r.shape[0]))*C_0

for p in range(1,nT-1):

	if (np.any(C_next_T_step > C_max-tol)):
		print('Turned j off')
		j[:]=0
	C_next_T_step=finite_one_timestep(C_prev_T_step)
	C_next_T_step=boundary_conditions(C_next_T_step,j[p])


	C_t[p+1,:]=C_next_T_step[:]

'''
plt.plot(r,C_next_T_step)
plt.show()
'''


fig=plt.figure()
# information about the slider
ax1=fig.add_subplot(111)
cut=1
axcolor = 'lightgoldenrodyellow'
xaxis  = axes([0.2, 0.02, 0.55, 0.02], facecolor=axcolor)
cut_slider = Page_Slider(xaxis, C_t.shape[0] , 'x-Grid', cut, '%i')

ax1.plot(r,C_t[cut,:],'g^')
ax1.set_xlabel(r'$r$',fontsize=18)
ax1.set_ylabel(r'$C$',fontsize=18)

def update_2by2(val):
	cut_val = int(cut_slider.val)
	ax1.clear()
	ax1.plot(r,C_t[cut_val,:],'g^')

	ax1.set_xlabel(r'$r$',fontsize=18)
	ax1.set_ylabel(r'$C$',fontsize=18)

cut_slider.on_changed(update_2by2)

plt.show()
