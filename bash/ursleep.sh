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

separador="#------------------------------------------------------------------";

color[0]="\033[1;32m"; # verde
color[1]="\e[1;31m"; # rojo
color[2]="\e[1;34m"; # celeste
color[3]="\e[1;33m"; # amarillo
color[4]="\e[1;30m"; # gris
color[5]="\033[0m";

echo $separador;

echo -e "# ${color[3]}URSLEEP, a bedtime calculator!${color[5]} (Basado en http://sleepyti.me/)"
echo -e "# ${color[4]}# adaptado por Cristian Escudero (escudero89@gmail.com).${color[5]}"
echo -e "# ${color[4]}Este archivo se encuentra bajo licencia GPLv3.${color[5]}";
echo "#"

echo -e "# Hora actual:" ${color[1]}$(date +%H:%M)${color[5]}".";

tiempo_dormir=$(date --date "$dte 45 minutes" +"%H:%M");

echo -e "# Probablemente estes durmiendo a las:" ${color[0]}$tiempo_dormir${color[5]}".";

mins=105;
step=90;

for i in $(seq 1 6); do
    echos[$i]=$(date --date "$dte $mins minutes" +"%H:%M");
    
    mins=$(($mins+$step));
done

echosjoin=$(printf ${color[2]}" %s "${color[5]} "${echos[@]}")

echo "#" 
echo "# Prueba levantarte en los siguientes horarios:"
echo -e "#" $echosjoin

echo $separador; 
