import numpy as np
from group_project import *

cmax = 12000
c0 = 9500
j0 = 9.5e-6
R = 1e-5
dr = 1e-7
Nr = R/dr

[cs,complete,errorflag] = spherical-diffusion(j0,c0,R,dr)

def completed():
    """
    Tests whether the simulation was completed with no fatal errors.
    The test passes if the simulation reached the final time step and no error flags were triggered.
    """
    assert complete == 1
    assert errorflag == 0

def inrange():
    """
    Tests whether the concentration profile is in the allowed range.
    The allowed range is defined as being between 0 and cmax.
    The test passes if the final concentration is in this range for all r and t.
    """
    assert cs.any > 0
    assert cs.any < cmax

def continuity():
    """
    Tests whether or not the concentration profile has any discontinuities.
    A discontinuity is defined here as a finite difference being greater than cmax.
    The test passes if no such discontinuities are detected.
    """
    dc = cs[:,0:Nr-1]-cs[:,1:Nr]
    assert dc.any < cmax
