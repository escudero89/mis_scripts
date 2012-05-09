#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2012 Cristian Gabriel Escudero escudero89@gmail.com
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

# @TODO:
# * Add a button to "Pause" and "Reanude" of the app.
# * Allow the program to close when a notification appears.
# * Make documentation.
# * Make preferences that really works, and you can edit.
# * Make translations to other languages possible.
# * Improve design.
# * Keep it simple.

import pynotify
import gtk
import os
import time
import random

from ureyes_lib.helpers import get_media_file

class eyehealth:
    wich_tip = 0
    wich_call = ""
    
    long_break = 60 # in minutes
    short_break = 10
    
    short_break_length = 10 # in seconds
    long_break_length = 300 
    previous_long_break = 30

    check_every = short_break * 60000 # check every 10 minutes = 600000 milliseconds  
            
    def get_tip(self):
        minutes = ( self.wich_tip + 1) * self.short_break # in minutes
 
        if (minutes == self.long_break): 
            self.run_notification("pseudo_break_time")
            self.run_notification("break_time")           
            self.wich_tip = -1 # Restart counter    
        
        if (minutes % 20 == 0): # every 20 minutes
            self.run_notification("202020_rule")
        
        elif (minutes % self.short_break == 0): # every 10 minutes
            while True:
                call_to = random.choice(["shake_eyes", "move_up_down", 
                "move_left_right", "blink", "close_eyes"])
                if ( call_to != self.wich_call ):
                    break;
            self.run_notification(call_to)                
            self.wich_call = call_to            
        
        
        self.wich_tip += 1
        return True            
    
    def run_notification(self, tip):

        health_tips = {
            "202020_rule" : {
                "title" : "20-20-20 Rule: Look for objects far away!",
                "secs" : 20
            }, 
            "shake_eyes" : {
                "title" : "Shake Shake Shake! Move your eyes like clocks!"
            }, 
            "move_up_down" : {
                "title" : "Move your eyes up and down!"
            }, 
            "move_left_right" : {
                "title" : "Move your left and right!"
            }, 
            "blink" : {
                "title" : "Blink! Blink! Time To Blink Very Fast!",
            }, 
            "close_eyes" : {
                "title" : "Close your eyes... Use your hands to create a better dark.",
            }, 
            "pseudo_break_time" : {
                "title" : "Brace yourself, long break is coming.",
                "secs" : self.previous_long_break
            },     
            "break_time" : {
                "title" : "Get off your lazy ass from the computer!",
                "secs" : self.long_break_length
            }            
        }
        
        if not pynotify.init("icon-summary-body"):
            sys.exit(1)
        
        try:
            secs = health_tips[tip]["secs"]
        except:
            secs = self.short_break_length
        
        if (tip not in ["break_time", "pseudo_break_time"]):
            secs_random = round(1.2 - random.random() * 0.7, 2) # 80 ~ 120 %
            secs = int(secs * secs_random) # A number +- 20% of seconds
        
        temp_counter = ["Duration: ", " seconds."]
        temp_counter_temp = temp_counter[0] + str(secs) + temp_counter[1]     
        
        n = pynotify.Notification(
            health_tips[tip]["title"],
            temp_counter_temp,
            get_media_file("ureyes.svg"))
        
        n.set_timeout(secs * 100)
        n.show()       
        
        old_secs = secs + 1
        
        for i in range(old_secs - 1):
            n.update(
                health_tips[tip]["title"],
                temp_counter_temp,
                get_media_file("ureyes.svg"))
                
            n.show()
            secs -= 1
            temp_counter_temp = temp_counter[0] + str(secs) + temp_counter[1]
            time.sleep(1)	   
        
        if (tip != "pseudo_break_time"):   
            n.update("Well Done!", 
                "Go back to work ;)",
                get_media_file("check.svg"))
            n.set_timeout(300) # only 3 seconds
                
            n.show()             
        
        # We strip the "file:"
        os.system("/usr/bin/canberra-gtk-play --file=" + get_media_file("sounds/linnod.ogg")[5:])
            
        return False

    def __init__(self):      
        gtk.timeout_add(self.check_every, self.get_tip)                              
