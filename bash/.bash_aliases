###############################################################################
# My alias, just for fun
###############################################################################

alias home='cd ~';
alias cristian='cd /media/Cristian/';

alias actualizaf='sudo apt-get update; sudo apt-get -fy upgrade';
alias actualiza='sudo apt-get update; sudo apt-get -f upgrade';
alias actualizar='sudo sudo rm /var/lib/apt/lists/* -vf; rm /var/lib/apt/lists/lock; actualiza';

alias quitar_espacios='rename "y/ /_/" *';

alias ultimo_reboot='last -x | grep reboot'
alias ultimo_shutdown='last -x | grep shutdown'

alias bash_aliases='gedit ~/Repositorios/mis_scripts/bash/.bash_aliases';
alias actualizar_wallpapers='python ~/Repositorios/mis_scripts/python/wallpaper_changer/wallpaper_changer.py "/media/Cristian/Copy/Stuff/Wallpapers" "180.0" "0.0"; sudo mv background-1.xml /usr/share/backgrounds/contest/precise.xml';

alias ..='cd ..';
alias ...='.. && ..';
alias ....='... && ..';

alias ll='ls -l';

alias j='jobs -l'

# Count number of files, links and directories
alias listar='for t in files links directories; do echo `find . -maxdepth 1 -type ${t:0:1} | wc -l` $t; done 2> /dev/null';

# Find duplicates files
alias duplicados='find -not -empty -type f -printf "%s\n" | sort -rn | uniq -d | xargs -I{} -n1 find -type f -size {}c -print0 | xargs -0 md5sum | sort | uniq -w32 --all-repeated=separate';

# Linux Mint
alias cinnamon-restart='cinnamon –replace -d :0.0 > /dev/null 2>&1 &';

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
function calc () { echo "$*" | bc -l; }

function say () { mplayer "http://translate.google.com/translate_tts?tl=en&q=$(echo $@ | sed 's/[ ]/\+/g')" &>/dev/null; }

function push () { git add . ; git add . -u; git status; git commit -m "$*"; git push; }

###############################################################################
# GLADOS VOICE
# Needs Tom’s LADSPA Plugins (apt-get install tap-plugins), try to simulate Glados

MYURL="http://translate.google.com/translate_tts?tl=en&q=";
MYLANG="&langpair=auto|";

function glados () { mplayer -speed 1.2 -af ladspa=/usr/lib/ladspa/tap_pitch.so:tap_pitch:1.5:0:0:-4 $(echo $MYURL$@ | sed 's/[ ]/\+/g') &>/dev/null; }

function gladoses() { glados $@$MYLANG"es"; }
function gladosfr() { glados $@$MYLANG"fr"; }

function rand () { awk "BEGIN { srand(); print int(rand()*$@) }"; }

# ganked these from people
#not an alias, but I thought this simpler than the cd control
#If you pass no arguments, it just goes up one directory.
#If you pass a numeric argument it will go up that number of directories.
#If you pass a string argument, it will look for a parent directory with that name and go up to it.

up() {
    dir=""
    if [ -z "$1" ]; then
        dir=..
    elif [[ $1 =~ ^[0-9]+$ ]]; then
        x=0
        while [ $x -lt ${1:-1} ]; do
            dir=${dir}../
            x=$(($x+1))
        done
    else
        dir=${PWD%/$1/*}/$1
    fi
    cd "$dir";
}

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
P_RED="\[\033[31;1m\]"
P_YELLOW="\[\033[33;1m\]"
P_WHITE="\[\033[37;1m\]"
SELECT="if [ \$? = 0 ]; then echo \"${P_WHITE}\"; else echo \"${P_RED}\"; fi"

# Sample Command using color: echo -e "${CYAN}This is BASH
#${RED}${BASH_VERSION%.*}${CYAN} - DISPLAY on ${RED}$DISPLAY${NC}\n"
if [ "$fun" = yes ]; then

    echo -e "Welcome ${myname}, to another ${LCYAN}Aperture Science Terminal${NC}."
    echo -e "The current date is $(date +%d/%m/%y', at '%H:%M:%S)."  
    
    PS1="\n${RESET}${debian_chroot:+($debian_chroot)}${P_WHITE}\`${SELECT}\`$namePS1 ${NORMAL}[ ${BLUE}\d${NORMAL} | ${LBLUE}\A${NORMAL} ]${P_WHITE} :\w${NORMAL}\n ${P_WHITE}\$${NORMAL} "
fi

# Para multiples escritorios
function multiple_desks {
	echo -e -n "${WHITE}Cantidad de escritorios ${NC}[horizontal vertical]: ";
	read x y;

	if [ $x -gt 0 ] && [ $y -gt 0 ]; then
		gconftool-2 --type=int --set /apps/compiz-1/general/screen0/options/hsize $x;
		gconftool-2 --type=int --set /apps/compiz-1/general/screen0/options/vsize $y;
	else
		echo -e "${RED}Numero incorrecto de escritorios:${NC} $x x $y.";
	fi
}
