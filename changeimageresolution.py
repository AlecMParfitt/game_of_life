#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 17:10:56 2021

@author: jonathansleppy
"""
"""This function takes a 3d image matrix of arbitrary resolution and resamples it
to a specified output resolution. 'interpstyle' is a string with options:
    
    'linear', 'cubic', 'quintic'. They are listed in order of best computational
    speed, but that is inversly related to output quality. (ex. linear will run
    the fastest but won't look the best. 
    
    'outputresolution' is a vector of 2 elements specifying the desired horizontal 
    resolution and vertical resolution,respectively."""


import numpy as np
import scipy as sp
import scipy.interpolate

def changeimagesamplingresolution(imagematrix,outputresolution,interpstyle):
    "find the resolution of the input"
    a,b,c = imagematrix.shape
    
    "generate dummy space vectors for interpolation"
    x = np.linspace(0,1,num=a)
    y = np.linspace(0,1,num=b)
    
    "generate vectors for the querry points"
    aprime = outputresolution[0]
    bprime = outputresolution[1]
    xprime = np.linspace(0,1,num=aprime)
    yprime = np.linspace(0,1,num=bprime)
    
    "preallocate the output matrix"
    outputimage = np.zeros(aprime,bprime)
    
    "loop of color indicies"
    for i in range(c):
        "calculate the interpolant"
        print(x.size,y.size)
        f = sp.interpolate.interp2d(x,y,imagematrix[:,:,i],kind=interpstyle)
        
        "compute the new values at querry points"
        outputimage[:,:,i] = f(xprime,yprime)
        
        
    return outputimage
        
        
    