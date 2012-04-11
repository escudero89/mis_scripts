#!/bin/bash
# <URSLEEP: A bedtime Calculator, based in sleepyti.me.>
#
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

c[0]="\033[1;32m"; # verde
c[1]="\e[1;31m"; # rojo
c[2]="\e[1;34m"; # celeste
c[3]="\e[1;33m"; # amarillo
c[4]="\e[1;30m"; # gris
c[5]="\033[0m";

function despertarse {

    echo -e -n "# Hora actual:" ${c[1]}$(date +%H:%M)${c[5]}" + (minutos [0]) ";
    read extra
    
    if [[ $extra =~ ^[0-9]+$ ]]; then
        tiempo_modificado=$(date --date "$dte $extra minutes" +"%H:%M");
        echo -e "# Hora modificada:" ${c[3]}$tiempo_modificado${c[5]}"."
    else   
        extra=0;
    fi
    
    tiempo_dormir=$(date --date "$dte $((45+$extra)) minutes" +"%H:%M");

    echo -e "# Probablemente estes durmiendo a las:" ${c[0]}$tiempo_dormir${c[5]}".";

    mins=$((105+$extra));
    step=90;

    for i in $(seq 1 6); do
        echos[$i]=$(date --date "$dte $mins minutes" +"%H:%M");
        
        mins=$(($mins+$step));
    done

    echosjoin=$(printf ${c[2]}" %s "${c[5]} "${echos[@]}")

    echo "#" 
    echo "# Prueba levantarte en los siguientes horarios:"
    echo -e "#" $echosjoin

} 

function acostarse {
    
    echo -e -n "# Hora de despertarse [HH MM]: ";    

    read hora minutos;    
    flag=false;
    
    while [[ $hora < 0 ]]; do
        echo -n "# Por favor, ingrese hora de despertarse [HH MM]: ";
        read hora minutos;
        flag=true;       
    done;
    
    if [[ flag ]]; then
        echo -e "# Hora modificada:" ${c[3]}$(date --date "$hora$minutos" +"%H:%M")${c[5]}"."
    fi
    
    mins=105;
    step=90;

    for i in $(seq 1 6); do
        minus=$(((-1) * ($mins + $step * (6 - $i))));
        echos[$i]=$(date --date "$hora$minutos 24hour $minus minutes" +"%H:%M");        
    done

    echosjoin=$(printf ${c[2]}" %s "${c[5]} "${echos[@]}")

    echo "#" 
    echo "# Prueba acostarte en los siguientes horarios:"
    echo -e "#" $echosjoin
    
}

separador="#------------------------------------------------------------------";

echo $separador;

echo -e "# ${c[3]}URSLEEP, a bedtime calculator!${c[5]} (Basado en http://sleepyti.me/)"
echo -e "# ${c[4]}adaptado por Cristian Escudero (escudero89@gmail.com).${c[5]}"
echo -e "# ${c[4]}Este archivo se encuentra bajo licencia GPLv3.${c[5]}";
echo "#"

echo -n "# Ingrese una opcion ([I]rse a dormir, [d]espertarse): " 
read opcion

if [[ $opcion == "d" ]]; then
    acostarse;    
else
    despertarse;
fi

echo $separador; 
