#!/usr/bin/python3

# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'images')   
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in3f
import time
from PIL import Image
import random

def refreshimage():
    logging.basicConfig(level=logging.DEBUG)

    try:
        logging.info("epd7in3f Demo")

        epd = epd7in3f.EPD()   
        logging.info("init and Clear")
        epd.init()
        epd.Clear()

        # read bmp file 
        # Get a list of all BMP files in the directory
        bmp_files = [file for file in os.listdir(picdir) if file.lower().endswith('.bmp')]

        if not bmp_files:
            print("No BMP files found in the directory.")
            return

        # Choose a random BMP file from the list
        random_bmp_file = random.choice(bmp_files)

        # Open the selected BMP file
        bmp_path = os.path.join(picdir, random_bmp_file)
        image = Image.open(bmp_path)

        # Display the image (assuming you have the appropriate code for this)
        epd.display(epd.getbuffer(image))
        
        time.sleep(3)

        logging.info("Goto Sleep...")
        epd.sleep()
            
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd7in3f.epdconfig.module_exit()
        exit()


refreshimage()