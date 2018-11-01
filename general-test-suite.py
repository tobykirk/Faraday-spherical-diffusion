from spherical-diffusion import *

cmax = 12000
c0 = 9500
j0 = 9.5e-6
R = 1e-5
dr = 1e-7
Nr = R/dr

[cs,complete,errorflag] = spherical-diffusion(j0,c0,R,dr)

def completed():
    assert complete == 1
    assert errorflag == 0

def inrange():
    assert cs[-1,:] > 0
    assert cs[-1,:] < cmax

def continuity():
    dc = cs[-1,0:Nr-1]-cs[-1,1:Nr]
    assert dc[:] < cmax