#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 11:09:11 2023

@author: thomasstinglhamber
"""
import os
import cv2
import time

def create_film(folder_path, frame_duration):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)
    #print(sorted(file_list))
    file_list.sort(key=lambda x: int(''.join(filter(str.isdigit, x))) if ''.join(filter(str.isdigit, x)).isdigit() else float('inf'))
    print(file_list)
    
    # Initialize a video writer
    video_writer = cv2.VideoWriter('/Users/thomasstinglhamber/Desktop/Energy_x.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (640, 480))
    # Loop through each file in the folder
    for file_name in file_list:
        
        if file_name.endswith('.jpg') or file_name.endswith('.png'):
            # Read the image file
            #print((file_name[:2]))
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)

            # Display the image for the specified duration
            for _ in range(int(frame_duration * 30)):  # Assuming 30 frames per second
                video_writer.write(image)

            # Display the image for a brief transition period
            transition_duration = 0.3  # Adjust this parameter as needed
            transition_frames = int(transition_duration * 30)
            for _ in range(transition_frames):
                video_writer.write(image)

    # Release the video writer
    video_writer.release()

# Specify the folder path where the images are located
folder_path = '/Users/thomasstinglhamber/Desktop/PHYS22M/Mémoire/film/NEW2/Energy_X'

# Specify the frame duration in seconds
frame_duration = 0.2  # Adjust this parameter as needed

# Call the function to create the film
create_film(folder_path, frame_duration)
