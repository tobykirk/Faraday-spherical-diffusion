from spherical-diffusion import *

cmax = 12000
c0 = 9500
j0 = 0
R = 1e-5
dr = 1e-7
Nr = R/dr

[cs,complete,errorflag] = spherical-diffusion(j0,c0,R,dr)

def completed():
    assert complete == 1
    assert errorflag == 0

def steadystate():
    assert cs[-1,:] == c0