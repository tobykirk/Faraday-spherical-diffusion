import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

'''
This program solves a 2D heat conduction problem 


Written by : Marjan and Simon and Nina
31/10/2018
'''

def FDE_interior(interior1_local,interior2_local,Temp):
	Temp2=Temp
	for i in interior1_local :
		for j in interior2_local :
			Temp2[i,j]=alpha * dt /dx **2 * (Temp[i+1,j]+Temp[i-1,j]+Temp[i,j+1]+Temp[i,j-1]) + \
				(1-4*alpha * dt /dx**2) * Temp[i,j]
			# activating this line shows you the area you are covering for the interior
			#Temp2[i,j]=200
	return Temp2

def FDE_edge(edge1_local,edge2_local,Temp,edge):
	Temp2=Temp
	if edge == 'T':
		for i in edge1_local:
			for j in edge2_local:
				Temp2[i,j]=alpha * dt /dx **2 * (2 * Temp[i-1,j]+Temp[i,j+1]+Temp[i,j-1]+2* T_f *(h * dx /k)) \
					+ (1-4 *alpha * dt /dx**2 -  2* alpha * h * dt /(k * dx) ) * Temp[i,j] 
				#Temp2[i,j]=200
	elif edge == 'L':
		for i in edge1_local:
			for j in edge2_local:
				Temp2[i,j]=alpha * dt /dx **2 * (2 * Temp[i-1,j]+Temp[i+1,j]+Temp[i,j-1]+2* T_f *(h * dx /k)) \
					+ (1-4 *alpha * dt /dx**2 -  2* alpha * h * dt /(k * dx) ) * Temp[i,j] 
	elif edge == 'R':
		for i in edge1_local:
			for j in edge2_local:
				Temp2[i,j]=alpha * dt /dx **2 * (2 * Temp[i-1,j]+Temp[i+1,j]+Temp[i,j+1]+2* T_f *(h * dx /k)) \
					+ (1-4 *alpha * dt /dx**2 -  2* alpha * h * dt /(k * dx) ) * Temp[i,j] 
	elif edge == 'B':
		for i in edge1_local:
			for j in edge2_local:
				Temp2[i,j]=alpha * dt /dx **2 * (2 * Temp[i+1,j]+Temp[i,j+1]+Temp[i,j-1]+2* T_f *(h * dx /k)) \
					+ (1-4 *alpha * dt /dx**2 -  2* alpha * h * dt /(k * dx) ) * Temp[i,j] 
	return Temp2 

def FDE_corner(c1_local,c2_local,Temp,corner):
	Temp2=Temp
	if corner=='BR':
		Temp2[c1_local,c2_local]=2 * alpha * dt /dx **2 * (Temp[c1_local+1,c2_local]+Temp[c1_local,c2_local+1]+ 2* T_f *(h*dx/k)) \
			+ (1-4 *alpha * dt /dx**2 -  4* alpha * h * dt /(k * dx)) * Temp[c1_local,c2_local]
	elif corner=='BL':
		Temp2[c1_local,c2_local]=2 * alpha * dt /dx **2 * (Temp[c1_local+1,c2_local]+Temp[c1_local,c2_local-1]+ 2* T_f *(h*dx/k)) \
			+ (1-4 *alpha * dt /dx**2 -  4* alpha * h * dt /(k * dx)) * Temp[c1_local,c2_local]
	elif corner=='TL':
		Temp2[c1_local,c2_local]=2 * alpha * dt /dx **2 * (Temp[c1_local-1,c2_local]+Temp[c1_local,c2_local-1]+ 2* T_f *(h*dx/k)) \
			+ (1-4 *alpha * dt /dx**2 -  4* alpha * h * dt /(k * dx)) * Temp[c1_local,c2_local]
	elif corner=='TR':
		Temp2[c1_local,c2_local]=2 * alpha * dt /dx **2 * (Temp[c1_local-1,c2_local]+Temp[c1_local,c2_local+1]+ 2* T_f *(h*dx/k)) \
			+ (1-4 *alpha * dt /dx**2 -  4* alpha * h * dt /(k * dx)) * Temp[c1_local,c2_local]
	return Temp2

nT=1000
h=10
alpha=1.4* 10e-7
k=40
rho=1110
T_f=180
dx=0.4/21.0
dt=0.01

n_spacing=11

Temp=np.zeros((n_spacing,n_spacing))

# First layer is the oven wall temperature
Temp[0,:]=T_f
Temp[:,0]=T_f
Temp[n_spacing-1,:]=T_f
Temp[:,n_spacing-1]=T_f

# in the middle it is at room temperature
Temp[1:n_spacing-1,1:n_spacing-1]=25

# one single cell represents the potato chip, we can make the chip bigger by changing this section
Temp[(n_spacing-1)/2,(n_spacing-1)/2]=-15

# saving this array in initial_oven_condition for plotting later
initial_oven_condition = Temp.copy()

edge1=np.arange(2,n_spacing-2,dtype=np.int)
edge2=np.ones(n_spacing-2,dtype=np.int)
edge3=np.ones(n_spacing-2,dtype=np.int)*(n_spacing-2)


interior2=np.arange(2,n_spacing-2,dtype=np.int)
interior1=interior2

# Loop over the number time
for p in range(nT):
#	corners	
	Temp=FDE_corner(1,1,Temp,'TL')
	Temp=FDE_corner(1,n_spacing-2,Temp,'TR')
	Temp=FDE_corner(n_spacing-2,1,Temp,'BL')
	Temp=FDE_corner(n_spacing-2,n_spacing-2,Temp,'BR')
#	edge
	'''
	# top
	Temp=FDE_edge(edge2,edge1,Temp,'T')
	#left
	Temp=FDE_edge(edge1,edge2,Temp,'L')
	# right
	Temp=FDE_edge(edge1,edge3,Temp,'R')
	# bottom
	Temp=FDE_edge(edge3,edge1,Temp,'B')
#	interior
	Temp=FDE_interior(interior1,interior2,Temp)
	'''

fig=plt.figure()

ax1=fig.add_subplot(121)
ax1.imshow(initial_oven_condition)
fig.colorbar(ax1.imshow(initial_oven_condition), orientation='vertical')
ax1.set_title('Initial condition of the oven',fontsize=10)

ax2=fig.add_subplot(122)
ax2.imshow(Temp)
fig.colorbar(ax2.imshow(Temp), orientation='vertical')
ax2.set_title('condition after '+str(nT)+' seconds',fontsize=10)

plt.show()


#print(Temp)
