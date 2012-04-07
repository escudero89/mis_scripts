import os, fnmatch, random

import sys

from xml.dom.minidom import Document

from xml.etree.ElementTree import Element, SubElement, tostring

def createXml(subdirectory='', dura_f='1795.0', dura_t='5.0'):
	atributos = ["year","month","day","hour","minute","second"]
	atrdentros = ["2009","08","04","00","00","00"]
	
	directorios = showFiles(subdirectory)
	
	random.shuffle(directorios) # comment this line to avoid shuffle of files
	
	string = "<background>\n" # Voy creando basicamente con string
	
	# Principio basico
	string += "  <starttime>\n"
	for atributo, atrdentro in zip(atributos,atrdentros):
		string += "    <" + atributo + ">" + atrdentro + "</" + atributo + ">\n"
	string += "  </starttime>\n"
	
	# Comentario del mismo archivo
	string += "<!-- This animation will start at midnight. -->\n" 
	
	for i in range(len(directorios)):
		# Documentos creados estaticos
		string += "  <static>\n"
		string += "    <duration>" + dura_f + "</duration>\n"
		string += "    <file>" + directorios[i] + "</file>\n"
		string += "  </static>\n"
		# Documentos creados dinamicos
		string += "  <transition>\n"
		string += "    <duration>" + dura_t + "</duration>\n"
		string += "    <from>" + directorios[i] + "</from>\n"
		if i + 1 == len(directorios):  # Circular
			proximo = 0
		else:
			proximo = i + 1
		string += "    <to>" + directorios[proximo] + "</to>\n"
		string += "  </transition>\n"

	string += "</background>"

	return string


def showFiles(subdirectory=''):	
    if subdirectory:
        path = subdirectory
    else:
        path = os.getcwd()
    
    # Elijo las extensiones de archivos de dibujo que voy a utilizar, por defecto las basicas
    extensiones = [".jpg", ".png", ".bmp", "jpeg"]    
    directorios = []
    for root, dirs, names in os.walk(path):
        for name in names:
            extension = os.path.splitext(name)[1]
	    try: 
                i = extensiones.index(extension)
            except ValueError:
                i = -1 # no match
            if (i != -1):
                directorios.append(root + "/" + name)

    return directorios
	
if __name__ == "__main__":
    
    files = open("background-1.xml","w")
        
    l = len(sys.argv)
    string = createXml()
    
    if l > 3:
	    string = createXml(sys.argv[1], sys.argv[2], sys.argv[3])
    elif l > 2:
	    string = createXml(sys.argv[1], sys.argv[2])
    elif l > 1:
		string = createXml(sys.argv[1])    
    
    print >> files, string
