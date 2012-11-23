###############################################################################
# My alias, just for fun
###############################################################################

alias home='cd ~';
alias cristian='cd /media/Cristian/';

alias actualizaf='sudo apt-get update; sudo apt-get -fy upgrade';
alias actualiza='sudo apt-get update; sudo apt-get -f upgrade';
alias actualizar='sudo rm /var/lib/apt/lists/lock; actualiza'

alias quitar_espacios='rename "y/ /_/" *';

alias ultimo_reboot='last -x | grep reboot'
alias ultimo_shutdown='last -x | grep shutdown'

alias bash_aliases='gedit ~/Repositorios/mis_scripts/bash/.bash_aliases';
alias actualizar_wallpapers='python ~/Repositorios/mis_scripts/python/wallpaper_changer/wallpaper_changer.py "/media/Cristian/Stuff/Wallpapers" "180.0" "0.0"; sudo mv background-1.xml /usr/share/backgrounds/contest/precise.xml';

alias ..='cd ..';
alias ...='.. && ..';
alias ....='... && ..';

# Find duplicates files
alias duplicados='find -not -empty -type f -printf "%s\n" | sort -rn | uniq -d | xargs -I{} -n1 find -type f -size {}c -print0 | xargs -0 md5sum | sort | uniq -w32 --all-repeated=separate';

SMILEY="${WHITE}:)${NORMAL}"
FROWNY="${RED}:(${NORMAL}"
SELECT="if [ \$? = 0 ]; then echo \"${SMILEY}\"; else echo \"${FROWNY}\"; fi"

# Expand the history size
HISTFILESIZE=10000
HISTSIZE=100

## Color for manpages by oyvindio
export LESS_TERMCAP_mb=$'\E[01;31m'
export LESS_TERMCAP_md=$'\E[01;31m'
export LESS_TERMCAP_me=$'\E[0m'
export LESS_TERMCAP_se=$'\E[0m'                           
export LESS_TERMCAP_so=$'\E[01;44;33m'                                 
export LESS_TERMCAP_ue=$'\E[0m'
export LESS_TERMCAP_us=$'\E[01;32m'

# Functions

# Define a quick calculator function
calc () { echo "$*" | bc -l; }

say () { mplayer "http://translate.google.com/translate_tts?tl=en&q=$(echo $@ | sed 's/[ ]/\+/g')" &>/dev/null; }

push () { git add . ; git add . -u; git status; git commit -m "$*"; git push; }

###############################################################################
# GLADOS VOICE
# Needs Tom’s LADSPA Plugins (apt-get install tap-plugins), try to simulate Glados

MYURL="http://translate.google.com/translate_tts?tl=en&q=";
MYLANG="&langpair=auto|";

glados () { mplayer -speed 1.2 -af ladspa=/usr/lib/ladspa/tap_pitch.so:tap_pitch:1.5:0:0:-4 $(echo $MYURL$@ | sed 's/[ ]/\+/g') &>/dev/null; }

gladoses() { glados $@$MYLANG"es"; }
gladosfr() { glados $@$MYLANG"fr"; }

rand () { awk "BEGIN { srand(); print int(rand()*$@) }"; }

###############################################################################
# My stuff, just for fun
###############################################################################

# Default PS1, I want GLaDOS instead
fun=yes
namePS1='GLaDOS'
myname='Cristian'

# Define a few Color's
BLACK='\e[0;30m'
BLUE='\e[0;34m'
GREEN='\e[0;32m'
CYAN='\e[0;36m'
RED='\e[0;31m'
PURPLE='\e[0;35m'
BROWN='\e[0;33m'
LGRAY='\e[0;37m'
DGRAY='\e[1;30m'
LBLUE='\e[1;34m'
LGREEN='\e[1;32m'
LCYAN='\e[1;36m'
LRED='\e[1;31m'
LPURPLE='\e[1;35m'
YELLOW='\e[1;33m'
WHITE='\e[1;38m'
NC='\e[0m'              # No Color

# Used in PS1
RESET="\[\017\]"
NORMAL="\[\033[0m\]"
RED="\[\033[31;1m\]"
YELLOW="\[\033[33;1m\]"
WHITE="\[\033[37;1m\]"
SELECT="if [ \$? = 0 ]; then echo \"${WHITE}\"; else echo \"${RED}\"; fi"

# Sample Command using color: echo -e "${CYAN}This is BASH
#${RED}${BASH_VERSION%.*}${CYAN} - DISPLAY on ${RED}$DISPLAY${NC}\n"
if [ "$fun" = yes ]; then

    echo -e "Welcome ${myname}, to another ${LCYAN}Aperture Science Terminal${NC}."
    echo -e "The current date is $(date +%d/%m/%y', at '%H:%M:%S)."  
    
    PS1="\n${RESET}${debian_chroot:+($debian_chroot)}${WHITE}\`${SELECT}\`$namePS1 ${NORMAL}[ ${BLUE}\d${NORMAL} | ${LBLUE}\A${NORMAL} ]${WHITE} :\w${NORMAL}\n ${WHITE}\$${NORMAL} "
fi


