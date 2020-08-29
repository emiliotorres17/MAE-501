#!/usr/bin/env python3

import os
import sys
from subprocess import call
from numpy import *

if __name__ == '__main__':

    call(['clear'])
    b           = array([[5],[6],[3]])
    A           = array([[1,3,1],[4,0,2],[1,3,4]])
    A1          = array([[1,3,1],[4,0,2],[1,3,4]])
    I           = identity(3)
    #step 2
    A1[1,:]     = 4*A1[0,:]-A1[1,:]
    I[1,:]      = 4*I[0,:]-I[1,:]
    print(A1)
    print('\n')
    print(I)
    #step 2
    A1[2,:]     = A1[0,:]-A1[2,:]
    I[2,:]      = I[0,:]-I[2,:]
    print('\n\n\n')
    print(A1)
    print('\n')
    print(I)
    #step 3
    A1[1,:]     = -2/3*A1[2,:]-A1[1,:]
    I[1,:]     = -2/3*I[2,:]-I[1,:]
    print('\n\n\n')
    print(A1)
    print('\n')
    print(I)
    #step 4
    A1[0,:]    = -1/3*A1[2,:]-A1[0,:]
    I[0,:]    = -1/3*I[2,:]-I[0,:]
    print('\n\n\n')
    print(A1)
    print('\n')
    print(I)
    #step 4
    A1[0,:]     = 1/4*A1[1,:]-A1[0,:]
    I[0,:]      = 1/4*I[1,:]-I[0,:]
    I[1,:]      = I[1,:]/A1[1,1]   
    I[2,:]      = I[2,:]/A1[2,2]   
    print('\n\n\n')
    print(A1)
    print('\n')
    print(I)
    #print('\n\n\n')
    #print(I-linalg.inv(A))
    print('\n\n\n')
    print(linalg.inv(A)@b)
    print(44/24)
    print(23/18)
    
    #print(linalg.inv(A))
