#!/usr/bin/env python3
"""========================================================================
Purpose:
    The purpose of this script is to perform the QR factorization.

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
import time
#-------------------------------------------------------------------------#
# User packages                                                           #
#-------------------------------------------------------------------------#
from ales_post.plot_settings        import plot_setting
from linear_algebra                 import print_matrix
from linear_algebra                 import LU_factorization
#=========================================================================#
# User defined functions                                                  #
#=========================================================================#
#-------------------------------------------------------------------------#
# QR factorization                                                        #
#-------------------------------------------------------------------------#
def QR_factor(
        mat):

    """ QR factorization subroutine """
    #---------------------------------------------------------------------#
    # Preallocating variables                                             #
    #---------------------------------------------------------------------#
    N       = mat.shape[0]
    Q1      = zeros((N,N))
    #---------------------------------------------------------------------#
    # Calculating QR                                                      #
    #---------------------------------------------------------------------#
    for j in range(0, N):
        q   = mat[:,j]
        #-----------------------------------------------------------------#
        # direction vectors                                               #
        #-----------------------------------------------------------------#
        for i in range(0,j):
            num     = transpose(Q1[:,i])@q
            den     = transpose(Q1[:,i])@Q1[:,i]
            q       = q-(num/den)*Q1[:,i]
        #-----------------------------------------------------------------#
        # Normalizing Q matrix                                            #
        #-----------------------------------------------------------------#
        Q1[:,j]  = q
    for i in range(0, N):
        Q1[:,i] = 1.0/sqrt(sum(Q1[:,i]**2.0))*Q1[:,i]
    #---------------------------------------------------------------------#
    # Calculating R                                                       #
    #---------------------------------------------------------------------#
    R1   = transpose(Q1)@mat 

    return Q1, R1
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
    # Verification case                                                   #
    #---------------------------------------------------------------------#
    A       = array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
    [Q, R]  = QR_factor(A)
    print_matrix(Q, 'Q =')
    print_matrix(R, 'R =')
    print_matrix(A-Q@R, 'A-QR =')
    #---------------------------------------------------------------------#
    # LU factorization                                                    #
    #---------------------------------------------------------------------#
    A       = array([[1, 2, 3], [2, 2, 3], [3, 3, 3]])
    [L, U]  = LU_factorization(A)
    print_matrix(U, 'U =')
    print_matrix(L, 'L =')
    print_matrix(A-L@U, 'A-LU =')
    sys.exit(8)
    #---------------------------------------------------------------------#
    # Time study                                                          #
    #---------------------------------------------------------------------#
    M       = [10, 100, 200, 500, 1000, 2000]
    timeQR  = zeros(len(M))
    timeLU  = zeros(len(M))
    ratio   = zeros(len(M))
    for k, m in enumerate(M):
        A           = random.rand(m,m)
        #-----------------------------------------------------------------#
        # QR factorization                                                #
        #-----------------------------------------------------------------#
        tic         = time.time() 
        [Q, R]      = QR_factor(A)
        toc         = time.time()
        timeQR[k]   = toc-tic
        #-----------------------------------------------------------------#
        # LU factorization                                                #
        #-----------------------------------------------------------------#
        tic         = time.time() 
        [L, U]      = LU_factorization(A)
        toc         = time.time()
        timeLU[k]   = toc-tic
        #-----------------------------------------------------------------#
        # Ratio of time between the factors                               #
        #-----------------------------------------------------------------#
        ratio[k]    = timeQR[k]/timeLU[k]
        #-----------------------------------------------------------------#
        # Print statement                                                 #
        #-----------------------------------------------------------------#
        print('M --> %8i\ttime QR --> %4.2e\ttime LU --> %4.2e'\
                        %(m, timeQR[k], timeLU[k]))
    #---------------------------------------------------------------------#
    # Plotting time                                                       #
    #---------------------------------------------------------------------#
    plot_setting()
    plt.plot(timeQR, M, 'ro--', label='$QR$ Factorization') 
    plt.plot(timeLU, M, 'bo--', label='$LU$ Factorization') 
    plt.grid(True)
    plt.legend(loc=0)
    plt.ylabel('Matrix size')
    plt.xlabel('Time [sec]')
    plt.savefig(media_path + 'QR-LU.png')
    plt.show()
    #---------------------------------------------------------------------#
    # Plotting ratio                                                      #
    #---------------------------------------------------------------------#
    plot_setting()
    plt.plot(M, ratio, 'ro--') 
    plt.plot([M[0], M[-1]], [1,1], 'b--')
    plt.grid(True)
    plt.ylim([0, 30])
    plt.ylabel('$t_{QR}/t_{LU}$')
    plt.xlabel('Matrix size')
    plt.savefig(media_path + 'QR-LU-ratio.png')
    plt.show()

    print('**** Successful run ****')
    sys.exit(0)