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
# User defined functions                                                  #
#=========================================================================#
#-------------------------------------------------------------------------#
# Converting to grey scale                                                #
#-------------------------------------------------------------------------#
def rgb2gray(rgb):
    return dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
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
    # Loading face data                                                   #
    #---------------------------------------------------------------------#
    face_data   = scipy.io.loadmat(data_path + 'Faces.mat')
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
    trainingFaces   = faces[:,:sum(nfaces[:36])]
    avgFace         = mean(trainingFaces, axis=1)
    print('finished line avgFace')
    #---------------------------------------------------------------------#
    # Computing the SVD                                                   #
    #---------------------------------------------------------------------#
    X           = trainingFaces - tile(avgFace,(trainingFaces.shape[1],1)).T
    U, S, VT    = linalg.svd(X,full_matrices=0)
    print('finished SVD')
    #---------------------------------------------------------------------#
    # Plotting the average face                                           #
    #---------------------------------------------------------------------#
    fig1    = plt.figure()
    img_avg = plt.imshow(reshape(avgFace,(m,n)).T)
    img_avg.set_cmap('gray')
    plt.axis('off')
    plt.savefig(media_path + 'average-face.png')
    plt.show()
    plt.close()
    #---------------------------------------------------------------------#
    # Plotting the average face                                           #
    #---------------------------------------------------------------------#
    img_u1  = plt.imshow(reshape(U[:,0],(m,n)).T)
    img_u1.set_cmap('gray')
    plt.axis('off')
    plt.savefig(media_path + 'mode-1.png')
    plt.show()
    plt.close()
    #---------------------------------------------------------------------#
    # Test face                                                           #
    #---------------------------------------------------------------------#
    testFace = faces[:,sum(nfaces[:36])]
    print(type(testFace))
    print(testFace.shape)
    plt.imshow(reshape(testFace,(m,n)).T)
    plt.set_cmap('gray')
    plt.title('Original Image')
    plt.axis('off')
    plt.savefig(media_path + 'original-image-1.png') 
    plt.close()
    #---------------------------------------------------------------------#
    # Test face                                                           #
    #---------------------------------------------------------------------#
    testFaceMS  = testFace - avgFace
    r_list      = [25, 50, 100, 200, 400, 800, 1600]
    #---------------------------------------------------------------------#
    # Different modes                                                     #
    #---------------------------------------------------------------------#
    for r in r_list:
        reconFace   = avgFace + U[:,:r]  @ (U[:,:r].T @ testFaceMS)
        img         = plt.imshow(reshape(reconFace,(m,n)).T)
        img.set_cmap('gray')
        plt.title('r = ' + str(r))
        plt.axis('off')
        plt.savefig(media_path + 'r-%i-1.png'              %(r))
        plt.close()
    #---------------------------------------------------------------------#
    # Test face                                                           #
    #---------------------------------------------------------------------#
    testFace = faces[:,sum(nfaces[:37])]
    print(type(testFace))
    print(testFace.shape)
    plt.imshow(reshape(testFace,(m,n)).T)
    plt.set_cmap('gray')
    plt.title('Original Image')
    plt.axis('off')
    plt.savefig(media_path + 'original-image-2.png') 
    plt.close()
    #---------------------------------------------------------------------#
    # Test face                                                           #
    #---------------------------------------------------------------------#
    testFaceMS  = testFace - avgFace
    r_list      = [25, 50, 100, 200, 400, 800, 1600]
    #---------------------------------------------------------------------#
    # Different modes                                                     #
    #---------------------------------------------------------------------#
    for r in r_list:
        reconFace   = avgFace + U[:,:r]  @ (U[:,:r].T @ testFaceMS)
        img         = plt.imshow(reshape(reconFace,(m,n)).T)
        img.set_cmap('gray')
        plt.title('r = ' + str(r))
        plt.axis('off')
        plt.savefig(media_path + 'r-%i-2.png'              %(r))
        plt.close()
