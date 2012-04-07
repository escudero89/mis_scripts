#!/bin/bash

# This script download all the resources files from chromium cache.
# Well, only images with JPEG format, and up to 30kb of size.

# For google chrome
# cd /home/cristian/.cache/google-chrome/Default/Cache
cd /home/cristian/.cache/chromium/Default/Cache

find -type f -print0 -size +30k | xargs -0 file -i | grep -i -e "JPEG" -e "JPG" | awk {'print $1'} | sed 's/^..//g' | sed 's/.$//g' > /tmp/FILESTOMOVE.txt

#The command explained...

#find -size +30k = images up to 40kb are good to save.

#find -type f = find files

#xarg -0 file -i = output the mime type

#grep -i JPEG = only show give me JPEG files

#awk {'print $1'} | sed 's/^..//g' | sed 's/.$//g' = tidy up file names

#> /tmp/FILESTOMOVE.txt = create a filelist for moving.

# Now you have a list of files... I have a little command I use to move that list to somewhere.
IFS=$'\n'
mkdir -p /home/cristian/Escritorio/saved_from_google_cache/
if [ -f /tmp/FILESTOMOVE.txt ];then
     cat /tmp/FILESTOMOVE.txt |
     while read newfile; 
     do
        cp $newfile /home/cristian/Escritorio/saved_from_google_cache/
    done
fi

