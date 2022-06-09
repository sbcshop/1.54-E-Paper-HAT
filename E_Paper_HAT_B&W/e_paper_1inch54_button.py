#!/usr/bin/python
# -*- coding:utf-8 -*-
import lib_1nch54_e_paper
import time
from PIL import Image,ImageDraw,ImageFont
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

KEY1_PIN       = 5
KEY2_PIN       = 6
KEY3_PIN       = 13
KEY4_PIN       = 19
KEY5_PIN       = 26

but0 = 21
but1 = 20
but2 = 16
but3 = 12




GPIO.setmode(GPIO.BCM) 
GPIO.setup(KEY1_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY2_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY3_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY4_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)# Input with pull-up
GPIO.setup(KEY5_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)# Input with pull-up


GPIO.setup(but0,GPIO.IN, pull_up_down=GPIO.PUD_UP)# Input with pull-up
GPIO.setup(but1,GPIO.IN, pull_up_down=GPIO.PUD_UP)# Input with pull-up
GPIO.setup(but2,GPIO.IN, pull_up_down=GPIO.PUD_UP)# Input with pull-up
GPIO.setup(but3,GPIO.IN, pull_up_down=GPIO.PUD_UP)# Input with pull-up



while 1:
    
        e_paper = lib_1nch54_e_paper.epaper()
        e_paper.init()
        #e_paper.Clear_screen
        font24 = ImageFont.truetype(('images/Font.ttc'), 24)
        font18 = ImageFont.truetype(('images/Font.ttc'), 18)
        font30 = ImageFont.truetype(('images/Font.ttc'), 30)
        font40 = ImageFont.truetype(('images/Font.ttc'), 40)
        #image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 255: clear the frame
        #draw = ImageDraw.Draw(image)
        #draw.text((10, 20), 'KEY 45', font = font30)
        #e_paper.display_image(e_paper.buffer(image.rotate(90)))

        if GPIO.input(KEY1_PIN) == GPIO.LOW: # button is released
            print("KEY1")
            image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 255: clear the frame
            draw = ImageDraw.Draw(image)
            draw.text((10, 20), 'KEY 1', font = font30)
            e_paper.display_image(e_paper.buffer(image.rotate(90)))
            
            
        
        if GPIO.input(KEY2_PIN) == GPIO.LOW: # button is released
            print("KEY2")
            image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 255: clear the frame
            draw = ImageDraw.Draw(image)
            draw.text((10, 20), 'KEY 2', font = font30)
            e_paper.display_image(e_paper.buffer(image.rotate(90)))
            
        
        # Drawing on the Vertical image
        if GPIO.input(KEY3_PIN) == GPIO.LOW: # button is released
            print("KEY3")
            image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 255: clear the frame
            draw = ImageDraw.Draw(image)
            draw.text((10, 20), 'KEY 3', font = font30)
            e_paper.display_image(e_paper.buffer(image.rotate(90)))
            
            
        if GPIO.input(KEY4_PIN) == GPIO.LOW: # button is released
            print("KEY4")
            image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 255: clear the frame
            draw = ImageDraw.Draw(image)
            draw.text((10, 20), 'KEY 4', font = font30)
            e_paper.display_image(e_paper.buffer(image.rotate(90)))

        if GPIO.input(KEY5_PIN) == GPIO.LOW: # button is released
            print("KEY5")
            image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 255: clear the frame
            draw = ImageDraw.Draw(image)
            draw.text((10, 20), 'KEY 5', font = font30)
            e_paper.display_image(e_paper.buffer(image.rotate(90)))


        if GPIO.input(but0) == GPIO.LOW: # button is released
            print("buto")
            image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 255: clear the frame
            draw = ImageDraw.Draw(image)
            draw.text((10, 20), 'button 0', font = font30)
            e_paper.display_image(e_paper.buffer(image.rotate(90)))
            

        if GPIO.input(but1) == GPIO.LOW: # button is released
            print("but1")
            image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 255: clear the frame
            draw = ImageDraw.Draw(image)
            draw.text((10, 20), 'button 1', font = font30)
            e_paper.display_image(e_paper.buffer(image.rotate(90)))
            

        if GPIO.input(but2) == GPIO.LOW: # button is released
            print("but2")
            image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 255: clear the frame
            draw = ImageDraw.Draw(image)
            draw.text((10, 20), 'button 2', font = font30)
            e_paper.display_image(e_paper.buffer(image.rotate(90)))
            


        if GPIO.input(but3) == GPIO.LOW: # button is released
            print("but3") 
            image = Image.new('1', (e_paper.width, e_paper.height), 255)  # 255: clear the frame
            draw = ImageDraw.Draw(image)
            draw.text((10, 20), 'button 3', font = font30)
            e_paper.display_image(e_paper.buffer(image.rotate(90)))

            

