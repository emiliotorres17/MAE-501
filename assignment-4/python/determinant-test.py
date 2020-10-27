#!/usr/bin/env python3
"""========================================================================
Purpose:
    The purpose of this script is to plot the average kinetic energy for
    the different CDS values.

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
    data_path   = pwd + '%c..%cdata%c'          %(sep, sep, sep)
    media_path  = pwd + '%c..%cmedia%c'         %(sep, sep, sep)
    #---------------------------------------------------------------------#
    # Preallocating variables                                             #
    #---------------------------------------------------------------------#
    a11     = [1,-1]
    a12     = [1,-1]
    a13     = [1,-1]
    a21     = [1,-1]
    a22     = [1,-1]
    a23     = [1,-1]
    a31     = [1,-1]
    a32     = [1,-1]
    a33     = [1,-1]
    det     = []
    count   = []
    counter = 0
    #---------------------------------------------------------------------#
    # Looping over the variables                                          #
    #---------------------------------------------------------------------#
    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0,2):
                for m in range(0,2):
                    for n in range(0,2): 
                        for p in range(0,2):
                            for q in range(0,2):
                                for l in range(0,2):
                                    for o in range(0,2):
                                        counter += 1
                                        A = array([[a11[o], a12[l], a13[q]],\
                                                [a21[p], a22[n], a23[m]],
                                                [a31[k], a32[j], a33[i]]])
                                        det.append(linalg.det(A))
                                        count.append(counter)
                                        print(counter)
    #---------------------------------------------------------------------#
    # Looping over the variables                                          #
    #---------------------------------------------------------------------#
    plot_setting()
    plt.plot(count, det, 'ro')
    plt.xlabel('Permutation number')
    plt.ylabel('Determinant value')
    plt.grid(True)
    plt.savefig(media_path + 'determinant-study.png')
    plt.show()

    print('**** Successful run ****')
    sys.exit(0)
