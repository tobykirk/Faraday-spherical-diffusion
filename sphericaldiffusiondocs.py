def boundary_conditions():
    '''
    the boundary conditions
    :return:
    '''
	return

def finite_one_timestep(C_local):
	'''
	Takes in just the radial part and give the radial part of
	the next time step
	'''

	C_p_add_one=np.ones(r.shape[0])*C_local
    '''
    
    '''

D_s=1e-14
    """
    diffusion coefficient - input parameter
    """
R=1e-5
    """
    the total spherical radius, i.e. maximum value of r
    """
C_max=12000
    """
    maximum allowable concentration of particle
    """
J_0=9.5e-6
    """
    constant flux value at time=0
    """
C_0=9500
    """
    uniform concentration of particle at time=0
    """
dr=0.1
    """
    increment in radius vector r
    """
dt=1
    """
    size of time step
    """
nT=10
    """
    number of time steps
    """
r=np.arange(1,10,dr)
    """
    where np.arange([start time,]stop time,[step size])
    returns evenly spaced values within the interval bounded by start (inclusive) and stop (exclusive) times
    with step size dr
    """

C=np.ones((nT,r.shape[0]))*C_0

def squared(x):
    """
    Returns the square if the input x

    Longer description - the square is found by multiplying x by x.

    :param x:
        base number
    :return: x*x
        base number raised to power 2

    Examples

    >>> squared(2)
    4

    >>> squared(-1)
    1
    """
    return x*x
