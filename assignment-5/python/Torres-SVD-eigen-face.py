#!/usr/bin/env python3
"""========================================================================
Purpose:
    The purpose of this script is to perform the eigen face problem for
    assignment #5.

Author:
    Emilio Torres
========================================================================"""
#=========================================================================#
# Preamble                                                                #
#=========================================================================#
#-------------------------------------------------------------------------#
# python packages                                                         #
#-------------------------------------------------------------------------#
import os
import sys
from subprocess import call
import matplotlib.pyplot as plt
import scipy.io
from numpy import *
from matplotlib import image
from PIL import Image
import matplotlib.image as mpimg
#-------------------------------------------------------------------------#
# Plot settings                                                           #
#-------------------------------------------------------------------------#
plt.rcParams['figure.figsize'] = [10, 10]
plt.rcParams.update({'font.size': 18})
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
    media_path  = pwd +'%c..%cmedia%c'              %(sep, sep, sep)
    #---------------------------------------------------------------------#
    # Making media path                                                   #
    #---------------------------------------------------------------------#
    if os.path.exists(media_path) is False:
        os.mkdir(media_path)
    #---------------------------------------------------------------------#
    # Loading face data                                                   #
    #---------------------------------------------------------------------#
    face_data   = scipy.io.loadmat('Faces.mat')
    faces       = face_data['faces']
    m           = int(face_data['m'])
    n           = int(face_data['n'])
    nfaces      = ndarray.flatten(face_data['nfaces'])
    print('nfaces --->')
    print(nfaces)
    #---------------------------------------------------------------------#
    # Plotting all the faces                                              #
    #---------------------------------------------------------------------#
    allPersons  = zeros((n*6,m*6))
    count       = 0
    for j in range(6):
        for k in range(6):
            allPersons[j*n:(j+1)*n, k*m:(k+1)*m] =\
                        reshape(faces[:,sum(nfaces[:count])],(m,n)).T
            count += 1
            print(count)
    #---------------------------------------------------------------------#
    # Plotting all the faces                                              #
    #---------------------------------------------------------------------#
    img = plt.imshow(allPersons)
    img.set_cmap('gray')
    plt.axis('off')
    plt.savefig(media_path + 'all-faces.png')
    plt.close()
    #---------------------------------------------------------------------#
    # Plotting all the faces                                              #
    #---------------------------------------------------------------------#
    for person in range(len(nfaces)):
        subset      = faces[:,sum(nfaces[:person]):sum(nfaces[:(person+1)])]
        allFaces    = zeros((n*8,m*8))
        count       = 0
        for j in range(8):
            for k in range(8):
                if count < nfaces[person]:
                    allFaces[j*n:(j+1)*n,k*m:(k+1)*m] = \
                            reshape(subset[:,count],(m,n)).T
                    count += 1
        #-----------------------------------------------------------------#
        # Plotting all the faces individually                             #
        #-----------------------------------------------------------------#
        img = plt.imshow(allFaces)
        img.set_cmap('gray')
        plt.axis('off')
        plt.savefig(media_path + 'face-%i.png'                   %(person))
        plt.close()
        print('face --> %i'                         %(person))
    #---------------------------------------------------------------------#
    # Training points using the first 36 faces                            #
    #---------------------------------------------------------------------#
    **** Perform the training points here ****
    #---------------------------------------------------------------------#
    # Computing the SVD                                                   #
    #---------------------------------------------------------------------#
    **** Computre the SVD here ****
    #---------------------------------------------------------------------#
    # Plotting the average face                                           #
    #---------------------------------------------------------------------#
    **** Plot the average face here ****
    #---------------------------------------------------------------------#
    # Plotting different modes  here                                      #
    #---------------------------------------------------------------------#
    **** Plot different modes here ****
    #---------------------------------------------------------------------#
    # Test face                                                           #
    #---------------------------------------------------------------------#
    **** Plolt test face here ****
    #---------------------------------------------------------------------#
    # Different modes                                                     #
    #---------------------------------------------------------------------#
    **** Apply different modes here for face 37 ****
