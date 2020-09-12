#!/usr/bin/env python3
"""========================================================================
Purpose:
    The purpose pf this script is to build subroutines to perform the
    following:
        1. Matrix inverse
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
import time                                     
from numpy import copy, identity, random, zeros, array 
import scipy.linalg as la                       
import matplotlib.pyplot as plt                 
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
            out += '%25.5f'          %(mat[I,J])
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
    plt.rc('text', usetex=True)                 
    plt.rc('font', family='serif')              
    SMALL_SIZE = 14                             
    MEDIUM_SIZE = 18                            
    BIGGER_SIZE = 20                            
    plt.rc('font',      size=SMALL_SIZE)        
    plt.rc('axes',      titlesize=SMALL_SIZE)   
    plt.rc('axes',      labelsize=MEDIUM_SIZE)  
    plt.rc('xtick',     labelsize=SMALL_SIZE)   
    plt.rc('ytick',     labelsize=SMALL_SIZE)   
    plt.rc('legend',    fontsize=SMALL_SIZE)    
    plt.rc('figure',    titlesize=BIGGER_SIZE)  
#-------------------------------------------------------------------------#
# LU factorization                                                        #
#-------------------------------------------------------------------------#
def LU_factorization(
        mat):               # inpuit matrix

    """ Calculating the LU factorization of the input vector """
    #---------------------------------------------------------------------#
    # Preallocating matrices                                              #
    #---------------------------------------------------------------------#
    M   = mat.shape[0]      # matrix size
    U   = copy(mat)         # make sure you copy matrix  (No!!! U = mat )
    L   = identity(M)       # Initialize L with the identity matrix
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
#-------------------------------------------------------------------------#
# Diagonal inverse tool                                                   #
#-------------------------------------------------------------------------#
def diagonal_inverse(
        mat):

    """ Subroutine to calculate the inverse of a diagonal matrix """
    #---------------------------------------------------------------------#
    # Domain variables                                                    #
    #---------------------------------------------------------------------#
    M   = mat.shape[0]
    out = idnetity(M)
    #---------------------------------------------------------------------#
    # Diagonal inverse                                                   #
    #---------------------------------------------------------------------#
    for i in range(0,M):
        out[i,i]    = 1/mat[i,i]

    return out
#-------------------------------------------------------------------------#
# Upper matrix inverse                                                    #
#-------------------------------------------------------------------------#
def upper_inverse(
        mat):

    """ Subroutine to calculate the inverse of an upper diagonal matrix """
    #---------------------------------------------------------------------#
    # Domain variables                                                    #
    #---------------------------------------------------------------------#
    M   = mat.shape[0]
    out = identity(M)
    #---------------------------------------------------------------------#
    # Upper inverse                                                       #
    #---------------------------------------------------------------------#
    for j in range(M-1, -1, -1): 
        for i in range(j-1, -1, -1):
            c           = mat[i,j]/mat[j,j]
            out[i,:]    =  out[i,:]-c*out[j,:]
        out[j,:] = out[j,:]/mat[j,j]
    return out
#-------------------------------------------------------------------------#
# Upper matrix inverse                                                    #
#-------------------------------------------------------------------------#
def lower_inverse(
        mat):

    """ Subroutine to calculate the inverse of a lower diagonal matrix """
    #---------------------------------------------------------------------#
    # Domain variables                                                    #
    #---------------------------------------------------------------------#
    M   = mat.shape[0]
    out = identity(M)
    #---------------------------------------------------------------------#
    # Lower inverse                                                       #
    #---------------------------------------------------------------------#
    for j in range(0, M-1): 
        for i in range(j,M-1):
            c           = mat[i+1,j]
            out[i+1,:]  = out[i+1,:]-c*out[j,:]

    return out
#-------------------------------------------------------------------------#
# Inverse tool                                                            #
#-------------------------------------------------------------------------#
def mat_inverse(
        mat):
    """ Subroutine to determine a matrix inverse """
    #---------------------------------------------------------------------#
    # Calculating the inverse using LU factors                            #
    #---------------------------------------------------------------------#
    N       = mat.shape[0]
    [L,U]   = LU_factorization(mat)
    #---------------------------------------------------------------------#
    # Calculating the inverse                                             #
    #---------------------------------------------------------------------#
    Linv    = lower_inverse(L)
    Uinv    = upper_inverse(U)
    inv     = Uinv@Linv
    
    return inv
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
    media_path  = pwd  + '%c..%cmedia%c'            %(sep, sep, sep)
    #---------------------------------------------------------------------#
    # Testing LU                                                          #
    #---------------------------------------------------------------------#
    N                   = 5
    A                   = random.rand(N,N)
    Ainv                = mat_inverse(A) 
    I                   = identity(N)
    print_matrix(A, 'A')
    print_matrix(Ainv, 'A^{-1}')
    print_matrix(I-A@Ainv, 'I-AxA^{-1}')
    #---------------------------------------------------------------------#
    # Time study                                                          #
    #---------------------------------------------------------------------#
    N       = [10, 100, 200, 300, 400, 500, 1000, 2000]
    times   = zeros(len(N))
    times2  = zeros(len(N))
    for k, i in enumerate(N):
        print(i)
        A               = random.rand(i,i)          # random matrix
        tic             = time.time()               # start time
        Ainv            = mat_inverse(A)            # inv(A)
        toc             = time.time()               # end time
        times[k]        = toc-tic                   # time elapsed
        tic             = time.time()
        ainv            = la.inv(A)
        toc             = time.time()
        times2[k]       = toc-tic
    #---------------------------------------------------------------------#
    # Plotting the solutions                                              #
    #---------------------------------------------------------------------#
    plot_setting()
    plt.plot(times, N, 'ro--', lw=1.5, label='Custom $A^{-1}$')
    plt.plot(times2, N, 'bo--', lw=1.5, label='Scipy $A^{-1}$')
    #---------------------------------------------------------------------#
    # Plot settings                                                       #
    #---------------------------------------------------------------------#
    plt.ylabel('Matrix size')
    plt.xlabel('time')
    plt.grid(True)
    plt.legend(loc=0)
    plt.savefig(media_path + 'exercise-8.png')
    plt.close()

    print('**** Successful run ****')
    sys.exit(0)
