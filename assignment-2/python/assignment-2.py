#!/usr/bin/env python3
"""========================================================================
Purpose:
    Solve a 1-D heat transfer problem.

Author:
    Emilio Torres
========================================================================"""
#=========================================================================#
# Preamble                                                                # 
#=========================================================================#
#-------------------------------------------------------------------------#
# Python packages                                                         # 
#-------------------------------------------------------------------------#
import os
import sys
from subprocess import call
from numpy import *
import scipy.linalg as la
import matplotlib.pyplot as plt
import time
#-------------------------------------------------------------------------#
# User packages                                                           # 
#-------------------------------------------------------------------------#
from ales_post.plot_settings import plot_setting
#=========================================================================#
# User defined functions                                                  # 
#=========================================================================#
#-------------------------------------------------------------------------#
# Pretty print matrix                                                     #
#-------------------------------------------------------------------------#
def print_matrix(
        mat,                  # input matrix
        var_str):

    """ Pretty printing a matrix """
    #---------------------------------------------------------------------#
    # Looping over columns and rows                                       #
    #---------------------------------------------------------------------#
    if mat.shape[1] is not False:
        out = ''                # initialize string
        for I in range(0, mat.shape[0]):
            for J in range(0, mat.shape[1]):
                out += '%12.5f'          %(mat[I,J])
            out += '\n'
    if mat.shape[1] is False:
        for I in range(0, mat.shape[0]):
            out += '%12.5f'          %(mat[I])
            out += '\n'
    print(var_str)
    print(out)
#-------------------------------------------------------------------------#
# Tri-diagonal                                                            # 
#-------------------------------------------------------------------------#
def tri_solver(
        A,
        B,
        C,
        D):

    """ Solving A tri-diagonal system """

    #---------------------------------------------------------------------#
    # Preallocating variables                                             # 
    #---------------------------------------------------------------------#
    N   = len(D)            # number of equations
    Ain = copy(A)
    Bin = copy(B) 
    Cin = copy(C) 
    Din = copy(D)
    #---------------------------------------------------------------------#
    # Looping over the domain                                             # 
    #---------------------------------------------------------------------#
    for I in range(1, N):
        mult    = Ain[I-1]/Bin[I-1]
        Bin[I]  = Bin[I] - mult*Cin[I-1] 
        Din[I]  = Din[I] - mult*Din[I-1]
    #---------------------------------------------------------------------#
    # Preallocation solutions                                             # 
    #---------------------------------------------------------------------#
    D[-1]     = Din[-1]/Bin[-1]
    #---------------------------------------------------------------------#
    # Interior solutions                                                  # 
    #---------------------------------------------------------------------#
    for I in range(N-2, -1, -1):
        D[I] = (Din[I]-Cin[I]*d[I+1])/Bin[I]

    return D
#=========================================================================#
# Main                                                                    # 
#=========================================================================#
if __name__ == '__main__':
    #---------------------------------------------------------------------#
    # Main preamble                                                       #
    #---------------------------------------------------------------------#
    call(['clear'])
    sep         = os.sep
    pwd         = os.getcwd()
    media_path  = pwd + '%c..%cmedia%c'             %(sep, sep, sep)
    #---------------------------------------------------------------------#
    # Domain variables                                                    #
    #---------------------------------------------------------------------#
    num     = [10, 100, 1000, 2000, 5000, 10000]
    time1   = zeros(len(num))
    time2   = zeros(len(num))
    for n in range(0, len(num)):
        print(num[n])
        M       = num[n]
        L       = 1.0
        dx      = L/float(M)
        alpha   = 1.0
        x       = linspace(0.0, 1.0, M+1)
        xc      = linspace(0.0, 1.0, 1000)
        Te      = 50.0/(4.0*pi**2.0)*sin(2.*pi*xc) +3.*xc
        #-----------------------------------------------------------------#
        # Preallocating variables                                         #
        #-----------------------------------------------------------------#
        T       = zeros(len(x))
        a       = ones(len(x)-3)
        b       = -2.0*ones(len(x)-2)
        c       = ones(len(x)-3)
        d       = -50.*sin(2.*pi*x[1:M])
        d       = dx**2.0*d
        d[-1]   = d[-1]-3.0
        #-----------------------------------------------------------------#
        # Solving system                                                  #
        #-----------------------------------------------------------------#
        tic     = time.time()
        T[1:M]  = tri_solver(a,b,c,d)
        T[0]    = 0.0
        T[M]    = 3.0 
        toc     = time.time()
        #-----------------------------------------------------------------#
        # Time elapsed                                                    #
        #-----------------------------------------------------------------#
        time1[n]= toc-tic
        #-----------------------------------------------------------------#
        # Full matrix approach                                            #
        #-----------------------------------------------------------------#
        A               = zeros((M-1,M-1))
        Tmat            = zeros(M+1)
        rhs             = zeros(M-1)
        A[0,0]          = -2.
        A[0,1]          = 1.
        A[M-2,M-2]      = -2.
        A[M-2,M-3]      = 1.
        for i in range(1,M-2):
            A[i,i]      = -2.
            A[i,i-1]    = 1.
            A[i,i+1]    = 1.
        rhs             = -50.*sin(2.*pi*x[1:M])
        rhs             = dx**2.0*rhs
        rhs[-1]         = rhs[-1]-3.
        tic             = time.time()    
        Tmat[1:M]       = linalg.inv(A)@rhs
        Tmat[0]         = 0.
        Tmat[-1]        = 3.
        toc             = time.time()    
        time2[n]        = toc-tic
    #---------------------------------------------------------------------#
    # Plotting solution                                                   #
    #---------------------------------------------------------------------#
    plot_setting()
    plt.plot(time1, num, 'ro--', lw=1.5, label='Tri-diagonal')
    plt.plot(time2, num, 'bo--', lw=1.5, label='Inverse matrix')
    plt.grid(True)
    plt.legend(loc=0)
    plt.savefig(media_path + 'time-comparison.png')
    plt.close()
    #---------------------------------------------------------------------#
    # Plotting time for tri-solver                                        #
    #---------------------------------------------------------------------#
    plt.plot(time1, num, 'ro--', lw=1.5, label='Tri-diagonal')
    plt.grid(True)
    plt.legend(loc=0)
    plt.savefig(media_path + 'tri-solve.png')
    plt.close()
    #---------------------------------------------------------------------#
    # Plotting time ratio                                                 #
    #---------------------------------------------------------------------#
    plt.plot(time2/time1, num, 'ro--', lw=1.5)
    plt.grid(True)
    plt.legend(loc=0)
    plt.savefig(media_path + 'time-ratio-solve.png')
    plt.show()
    plt.close()
