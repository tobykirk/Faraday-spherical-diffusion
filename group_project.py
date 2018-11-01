import numpy as np

def boundary_conditions():
	return

def finite_one_timestep(C_local):
	'''
	Takes in just the radial part and give the radial part of 
	the next time step
	'''
	C_p_add_one=np.ones(r.shape[0])*C_local

	for i in range(r.shape[0]):
		C_p_add_one[i]=C_local[i]+D_s * dt * ( 2.0/r[i]*(C_local[i+1]-C[i])/dr + \
			(C_local[i+1]-2*C_local[i]+C_local[i-1])/dr**2)
	return C_p_add_one

D_s=1e-14
R=1e-5
C_max=12000
J_0=9.5e-6

C_0=9500

dr=0.1
dt=1
# number of points in time 
nT=10

r=np.arange(1,10,dr)
C=np.ones((nT,r.shape[0]))*C_0

for p in range(2,nT):
	C[p+1,:]=finite_one_timestep(C[p,:])


print(C.shape)