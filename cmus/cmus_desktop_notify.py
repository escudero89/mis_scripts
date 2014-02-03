#! /usr/bin/env python
#
# cmus_desktop_notify.py: display song cmus is playing using notify-send.
# Copyright (C) 2011  Travis Poppe <tlp@lickwid.net>
#
# Version 2011.06.24
# http://tlp.lickwid.net/cmus_desktop_notify.py

# Usage: Run script for instructions.

# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# TODO:
#
# * Offer some configuration
# * Clean up status_data() (first iteration problem)
# * Clean up notification when some data is missing
# * Attempt to use filename when title is unavailable
# * Make work with python 3/test/etc

import sys
import time
import subprocess

import os

def print_usage():
   """Display usage info and exit."""

   print ' ##############################################################################'
   print ' # cmus_desktop_notify.py: display song cmus is playing using notify-send.    #'
   print ' # Copyright (C) 2011  Travis Poppe <tlp@lickwid.net>                         #'
   print ' #                                                                            #'
   print ' # Version: 2011.06.24                                                        #'
   print ' #                                                                            #'
   print ' # Tested on Ubuntu 11.04 with Unity window manager.                          #'
   print ' # Requirements: libnotify-bin (notify-send); probably python 2.x.            #'
   print ' ##############################################################################'
   print ' # Usage:                                                                     #'
   print ' #  1. Copy cmus_desktop_notify.py to ~/.cmus/ and make executable.           #'
   print ' #  2. Create ~/.cmus/status_display_program.sh with these contents           #'
   print ' #     and make executable (remove spaces and border):                        #'
   print ' #                                                                            #'
   print ' #     #!/bin/sh                                                              #'
   print ' #     ~/.cmus/cmus_desktop_notify.py "$*" &                                  #'
   print ' #                                                                            #'
   print ' #  3. Set the status_display_program variable in cmus (with YOUR homedir!)   #'
   print ' #                                                                            #'
   print ' #     :set status_display_program=/home/user/.cmus/status_display_program.sh #'
   print ' #                                                                            #'
   print ' #  4. Enjoy desktop notifications from cmus! Be sure to :save.               #'
   print ' ##############################################################################'
   sys.exit(2)

def status_data(item):
   """Return the requested cmus status data."""
   
   # We loop through cmus status data and use each of its known data
   # types as 'delimiters', collecting data until we reach one,
   # inserting it into the dictionary -- rinse and repeat.

   # cmus helper script provides our data as argv[1].
   cmus_data = sys.argv[1]

   # Split the data into an easily-parsed list.
   cmus_data = cmus_data.split()

   # Our temporary collector list.
   collector = []

   # Dictionary that will contain our parsed-out data.
   cmus_info = {'status':"",
                'file':"",
                'artist':"",
                'album':"",
                'discnumber':"",
                'tracknumber':"",
                'title':"",
                'date':"",
                'duration':""}

   # Loop through cmus data and write it to our dictionary.
   last_found = "status"
   for value in cmus_data:
       collector.append(value)
       # Check to see if cmus value matches dictionary key.
       for key in cmus_info:
           # If a match has been found, record the data.
           if key == value:
               collector.pop()
               cmus_info[last_found] = " ".join(collector)
               collector = []
               last_found = key

   # Return whatever data main() requests.
   return cmus_info[item]

def display_song():
   """Display the song data using notify-send."""

   # Si la cancion no tiene informacion, mostramos la otra notificacion
   if status_data("status") == "playing" or status_data("title") == "":
       subprocess.call('bash ~/.cmus/cmus-notify.sh 1', shell=True)
       
   # We only display a notification if something is playing.
   elif status_data("status") == "playing":

       # Check to see if title data exists before trying to display it.
       # Display "Unknown" otherwise.
       if status_data("title") != "":
           notify_summary = status_data("title")
       else:
           notify_summary = "Unknown"

       # Check to see if album data exists before trying to
       # display it. Prevents "Artist, " if it's blank.
       if status_data("album") != "":
           notify_body = status_data("artist") + ', ' + \
                         status_data("album")
       else:
           notify_body = status_data("artist")

       # Le agrego la duracion
       if status_data("duration") != "":
           notify_body = notify_body + ', [ ' + status_data("duration") + ' ]'

       # Create our temporary file if it doesn't exist yet.
       open("/tmp/cmus_desktop_last_track", "a").write("4")

       # Check to see when we got our last track from cmus.
       last_notice = open("/tmp/cmus_desktop_last_track", "r").read()

       # Write time stamp for current track from cmus.
       last_notice_time = str(time.time())
       open("/tmp/cmus_desktop_last_track", "w").write(last_notice_time)

       # Calculate seconds between track changes.
       track_change_duration = round(time.time() - float(last_notice))

       # Esto es para las imagenes (para cargar albumnes con fotos
       existGDBPath = status_data("file")
       wkspFldr = os.path.dirname(existGDBPath)
       
       # El default
       notify_pic = 'audio-speakers'
       
       for cover in {'Playlist.jpg', 'Back.jpg', 'back.jpg', 'Front.jpg', 'front.jpg'}:
               try:
                   cover_full = wkspFldr + '/' + cover
                   
                   with open(cover_full):
                        # Elimino los espacios en blanco
                       notify_pic = (cover_full).replace(' ', '\ ')

               except IOError:
                   #nothing
                   notify_pic

       # subprocess.call(('notify-send ' + str(track_change_duration)), shell=True)
       # Display current track notification only if 3 seconds have
       # elapsed since last track was chosen.
       if track_change_duration > 0:
           # Execute notify-send with our default song data.
           subprocess.call('notify-send -i ' + notify_pic + ' -u low -t 700 "' + \
                           notify_summary + '" "by ' + \
                           notify_body + ' "', shell=True)
                                

def main():
   try:
       # See if script is being called by cmus before proceeding.
       if sys.argv[1].startswith("status"):
           display_song()
   except:
       print_usage()

if __name__ == "__main__":
   main()

