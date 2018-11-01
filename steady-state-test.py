import numpy as np
from spherical-diffusion import *

cmax = 12000
c0 = 9500
j0 = 0
R = 1e-5
dr = 1e-7
Nr = R/dr

[cs,complete,errorflag] = spherical-diffusion(j0,c0,R,dr)

def completed():
    """
    Tests whether or not the simulation was completed with no fatal errors.
    The test passes if the simulation reached the final time step with no error flags triggered.
    """
    assert complete == 1
    assert errorflag == 0

def steadystate():
    """
    Tests whether the simulation gives the correct answer for the trivial case of zero flux.
    The test passes if the concentration is equal to c0 everywhere.
    """
    assert cs.any == c0