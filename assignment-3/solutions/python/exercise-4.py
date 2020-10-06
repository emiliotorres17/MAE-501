#!/usr/bin/env python3
"""========================================================================
Purpose:
    The purpose of this script is to calculate the solution to exercise-4.

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
# Main                                                                    #
#=========================================================================#
if __name__ == '__main__':
    #---------------------------------------------------------------------#
    # Main preamble                                                       #
    #---------------------------------------------------------------------#
    call(['clear'])
    sep         = os.sep
    pwd         = os.getcwd()
    data_path   = pwd + '%c..%cdata%c'              %(sep, sep, sep)
    media_path  = pwd + '%c..%cmedia%c'             %(sep, sep, sep)
    #---------------------------------------------------------------------#
    # Loading data                                                        #
    #---------------------------------------------------------------------#
    data        = loadtxt(data_path + 'data.dat', skiprows=1)
    time        = data[:,0]
    u           = data[:,1]
    #---------------------------------------------------------------------#
    # Linear fit                                                          #
    #---------------------------------------------------------------------#
    N           = len(time)
    A           = zeros((N,2))
    A[:,0]      = time 
    A[:,1]      = 1.0 
    coefsL      = linalg.inv(transpose(A)@A)@(transpose(A)@u)
    ulinear     = time*coefsL[0] + coefsL[1]
    err         = u - A@coefsL
    E           = sqrt(sum(err**2.0))
    print(E)
    print(err)
    #---------------------------------------------------------------------#
    # Parabola fit                                                        #
    #---------------------------------------------------------------------#
    N           = len(time)
    A           = zeros((N,3))
    A[:,0]      = time**2.0 
    A[:,1]      = time 
    A[:,2]      = 1.0 
    coefs       = linalg.inv(transpose(A)@A)@(transpose(A)@u)
    upar        = time**2.0*coefs[0] + time*coefs[1]+ coefs[2]
    err         = u - A@coefs
    E           = sqrt(sum(err**2.0))
    print(E)
    print(err)
    #---------------------------------------------------------------------#
    # Scatter plot                                                        #
    #---------------------------------------------------------------------#
    plot_setting()
    plt.plot(time, u, 'ro')
    plt.grid(True)
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.savefig(media_path + 'scatter.png')
    plt.show()
    #---------------------------------------------------------------------#
    # Plotting linear fit                                                 #
    #---------------------------------------------------------------------#
    plt.plot(time, u, 'ro')
    plt.plot(time, ulinear, 'g',\
                label='$u(t)=%2.1ft %2.1f$'      %(coefsL[0], coefsL[1]))
    plt.grid(True)
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.legend(loc=0)
    plt.savefig(media_path + 'linear.png')
    plt.show()
    #---------------------------------------------------------------------#
    # Plotting parabolic fit                                              #
    #---------------------------------------------------------------------#
    plt.plot(time, u, 'ro')
    plt.plot(time, upar, 'm',\
                label='$u(t)=%2.1ft^{2} + %2.1ft + %2.1f$'\
                        %(coefs[0], coefs[1], coefs[2]))
    plt.grid(True)
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.legend(loc=0)
    plt.savefig(media_path + 'parabolic.png')
    plt.show()

    print('**** Successful run ****')
    sys.exit(0)
