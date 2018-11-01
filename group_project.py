import numpy as np
import matplotlib.pyplot as plt


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
			(C_local[i+1]-2*C_local[i]+C_local[i-1])/dr**2)
	return C_next_T_step_local

D_s=1e-14
R=1e-5
C_max=12000.0
tol=C_max/100.00
J_0=9.5e-6

C_0=9500.0

dr=1e-7
dt=0.01
# number of points in time 
nT=100000

j=np.ones(nT)*J_0

r=np.arange(0,R,dr)

C_prev_T_step=np.ones(r.shape[0])*C_0
C_next_T_step=np.zeros(r.shape[0])
C_t=np.ones((nT,r.shape[0]))*C_0

for p in range(1,nT-1):
	C_next_T_step=finite_one_timestep(C_prev_T_step)
	C_next_T_step=boundary_conditions(C_next_T_step,j[p])

	if C_next_T_step.any()> C_max-tol:
		j=0

	C_t[p+1,:]=C_next_T_step[:]



plt.plot(r,C_next_T_step,'g^')
plt.show()

