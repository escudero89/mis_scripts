#!/bin/sh
~/.cmus/cmus_desktop_notify.py "$*" &
#~/.cmus/cmus-status.py "$*" &

if [ "$#" -ge 1 ]; then
        # Trabaja junto a CMUS para mostrar una notificacion del estilo filename [duration]
        Str="$(echo $(cmus-remote -Q | head -n 3 | cut -d ' ' -f 2- | cut -d '/' -f 6-))"; 
        Filename="$(echo ${Str##*'/'})";
        Tiempo="$(echo $(bc <<< 'obase=60;'$(echo ${Filename##* })))";

        notify-send -i audio-speakers "$(echo ${Filename%%.mp3*})" "[$(echo $Tiempo)] >> $(echo ${Str%/*})";
        
fi
