#!/usr/bin/env python3
"""========================================================================
Purpose:
    the purpose of this script is complete the assignment 3 solution.

Author:
    Emilio Torres
========================================================================"""
#=========================================================================#
# Purpose                                                                 #
#=========================================================================#
#-------------------------------------------------------------------------#
# Python packages                                                         #
#-------------------------------------------------------------------------#
import os
import sys
from subprocess import call
from numpy import *
import matplotlib.pyplot as plt
#-------------------------------------------------------------------------#
# User packages                                                           #
#-------------------------------------------------------------------------#
from ales_post.plot_settings        import plot_setting
#=========================================================================#
# User defined functions                                                  #
#=========================================================================#
#-------------------------------------------------------------------------#
# Matrix print                                                            #
#-------------------------------------------------------------------------#
def print_matrix(
        mat,                  # input matrix
        var_str):

    """ Pretty printing a matrix """
    #---------------------------------------------------------------------#
    # Looping over columns and rows                                       #
    #---------------------------------------------------------------------#
    out = ''                # initialize string
    for I in range(0, mat.shape[0]):
        for J in range(0, mat.shape[1]):
            out += '%12.5f'          %(mat[I,J])
        out += '\n'
    print(var_str)
    print(out)
#=========================================================================#
# Main                                                                    #
#=========================================================================#
if __name__ == '__main__':
    #---------------------------------------------------------------------#
    # Main preamble                                                       #
    #---------------------------------------------------------------------#
    call(['clear'])
    sep     = os.sep
    pwd     = os.getcwd()
    #---------------------------------------------------------------------#
    # Loading data                                                        #
    #---------------------------------------------------------------------#
    data    = loadtxt('data.dat', skiprows=1) 
    time    = data[:,0]
    u       = data[:,1]
    #---------------------------------------------------------------------#
    # Constructing A quadratic matrix                                     #
    #---------------------------------------------------------------------#
    A       = zeros((len(time), 3))
    for i in range(0, len(time)):
        A[i,0]  = time[i]**2.0
        A[i,1]  = time[i]
        A[i,2]  = 1.0
    print_matrix(A, 'A=')
    x   = linalg.inv(transpose(A)@A)@(transpose(A)@u)
    print(x)
    uquad = x[0]*time**2.0 + time*x[1] + x[2] 
    #---------------------------------------------------------------------#
    # Constructing B linear  matrix                                       #
    #---------------------------------------------------------------------#
    B       = zeros((len(time), 2))
    for i in range(0, len(time)):
        B[i,0]  = time[i]
        B[i,1]  = 1.0
    print_matrix(B, 'B=')
    xb      = linalg.inv(transpose(B)@B)@(transpose(B)@u)
    print(x)
    ulinear = xb[0]*time + xb[1] 
    #---------------------------------------------------------------------#
    # Plotting data                                                       #
    #---------------------------------------------------------------------#
    plot_setting()
    plt.plot(time, u, 'ro', lw=1.5)
    plt.plot(time, ulinear, 'g--', lw=1.5, \
                label='$u=%3.2ft + %3.2f$' %(xb[0], xb[1])  )
    plt.plot(time, uquad, 'k--', lw=1.5,\
            label='$u=%3.2f t^{2}+%3.2f t+%3.2f$'  %(x[0], x[1], x[2]))
    plt.grid(True)
    plt.legend(loc=0)
    plt.xlabel('time')
    plt.ylabel('Velocity')
    plt.show()

    print('**** Successful run ****')
    sys.exit(0)
