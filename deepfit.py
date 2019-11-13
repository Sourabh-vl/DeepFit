# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:39:00 2019

@author: sourabhag
"""
import cv2
class Deepfit:
    
    def VideoToFrames(path):
        
            # Path to video file
        vidObj = cv2.VideoCapture(path)

        # Used as counter variable
        count = 0

        # checks whether frames were extracted
        success = 1

        while success:

            # vidObj object calls read
            # function extract frames
            success, image = vidObj.read()

            # Saves the frames with frame-count
            cv2.imwrite("frames/frame%d.jpg" % count, image)

            count += 1
        
        
    
    def tagVideo(data):
        return data
    
    def shapleyVideo(data):
        print("hi")
        return data
    
    def activityPredict(data):
        return data
    
    def recoveryPhase(data):
        return data
    
    def pathtorecover(data):
        return data
        
    def toneAnalyser(data):
        return data
