#!/usr/bin/env python3
"""========================================================================
Purpose:
    The purpose pf this script is to build subroutines to perform the
    following:
        1. LU factorization
        2. Matrix inverse

    **** Note:
            This is pseudo code to help with Assignment 1

Author:
    Emilio Torres
========================================================================"""
#=========================================================================#
# Preamble                                                                #
#=========================================================================#
#-------------------------------------------------------------------------#
# Python packages                                                         #
#-------------------------------------------------------------------------#
import sys                                      # helpful for de-bugging (e.g., sys.exit(1))
from subprocess import call                     # may not use
import time                                     # for timing code
from numpy import copy, identity, random, zeros # useful math packages
import scipy.linalg as la                       # linear algebra package
import matplotlib.pyplot as plt                 # plotting packages
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
    out = ''                # initialize string
    for I in range(0, mat.shape[0]):
        for J in range(0, mat.shape[1]):
            out += '%12.5f'          %(mat[I,J])
        out += '\n'
    print(var_str)
    print(out)
#-------------------------------------------------------------------------#
# Plotting settings                                                       #
#-------------------------------------------------------------------------#
def plot_setting():

    """ Useful plotting settings """
    #---------------------------------------------------------------------#
    # Plotting settings                                                   #
    #---------------------------------------------------------------------#
    plt.rc('text', usetex=True)                     # text style
    plt.rc('font', family='serif')                  # text font
    SMALL_SIZE = 14                                 # small font size
    MEDIUM_SIZE = 18                                # medium font size
    BIGGER_SIZE = 20                                # large font size
    plt.rc('font',      size=SMALL_SIZE)            # controls default text sizes
    plt.rc('axes',      titlesize=SMALL_SIZE)       # fontsize of the axes title
    plt.rc('axes',      labelsize=MEDIUM_SIZE)      # fontsize of the x and y labels
    plt.rc('xtick',     labelsize=SMALL_SIZE)       # fontsize of the tick labels
    plt.rc('ytick',     labelsize=SMALL_SIZE)       # fontsize of the tick labels
    plt.rc('legend',    fontsize=SMALL_SIZE)        # legend fontsize
    plt.rc('figure',    titlesize=BIGGER_SIZE)      # fontsize of the figure title
#-------------------------------------------------------------------------#
# LU factorization                                                        #
#-------------------------------------------------------------------------#
def LU_factorization(
        mat):                  # inpuit matrix

    """ Calculating the LU factorization of the input vector """
    #---------------------------------------------------------------------#
    # Preallocating matrices                                              #
    #---------------------------------------------------------------------#
    M   = mat.shape[0]            # matrix size
    U   = copy(mat)               # make sure you copy matrix  (No!!! U = mat )
    L   = identity(M)           # Initialize L with the identity matrix
    #---------------------------------------------------------------------#
    # Cheking it is error matrix                                          #
    #---------------------------------------------------------------------#
    if not mat.shape[0] ==  mat.shape[1]:
        print('Input matrix must be square')
        print('Input --> [%i, %i]'          %(mat.shape[0], mat.shape[1]))
        sys.exit(8)
    #---------------------------------------------------------------------#
    # Calculating both L and U                                            #
    #---------------------------------------------------------------------#
    for K in range(0, M-1):
        for J in range(K+1, M):
            L[J,K]      = U[J,K]/U[K,K]
            U[J,K:]     = U[J,K:]-L[J,K]*U[K,K:]
            U[J,K]      = 0.0

    return L, U
#=========================================================================#
# Main                                                                    #
#=========================================================================#
if __name__ == '__main__':
    #---------------------------------------------------------------------#
    # Main preamble                                                       #
    #---------------------------------------------------------------------#
    call(['clear'])
    #---------------------------------------------------------------------#
    # Testing LU                                                          #
    #---------------------------------------------------------------------#
    A               = random.rand(3,3)
    (Lower,Upper)   = LU_factorization(A)
    print_matrix(Lower, 'L')
    print_matrix(Upper, 'U')
    print_matrix(A - (Lower@Upper), 'A-LU')
    #---------------------------------------------------------------------#
    # Time study                                                          #
    #---------------------------------------------------------------------#
    N       = [100, 200, 300, 400, 500, 1000, 2000]
    times   = zeros(len(N))
    times2  = zeros(len(N))
    for k, i in enumerate(N):
        A               = random.rand(i,i)          # random matrix
        tic             = time.time()               # start time
        (Lower,Upper)   = LU_factorization(A)       # LU
        toc             = time.time()               # end time
        times[k]        = toc-tic                   # time elapsed
        tic             = time.time()
        (p, l, u)       = la.lu(A)
        toc             = time.time()
        times2[k]       = toc-tic
    #---------------------------------------------------------------------#
    # Plotting the solutions                                              #
    #---------------------------------------------------------------------#
    plot_setting()                                              # plot settings
    plt.plot(times, N, 'ro--', lw=1.5, label='Custom LU')       # custom plot
    plt.plot(times2, N, 'bo--', lw=1.5, label='Scipy LU')       # builtin plot
    plt.ylabel('Matrix size')                                   # y-label
    plt.xlabel('time')                                          # x-label
    plt.grid(True)                                              # grid on
    plt.legend(loc=0)                                           # legend on
    plt.savefig('LU-study.png')                                 # storing plot
    plt.show()                                                  # plot show on
