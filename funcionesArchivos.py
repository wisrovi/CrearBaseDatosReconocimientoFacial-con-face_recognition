import os.path
import os
from shutil import copyfile


def ExisteArchivo(url):
    return os.path.isfile(url)

def borrarArchivo(url):
    os.remove(url)
    
def crearArchivo(url):
    file = open(url,"w")
    file.write("Wisrovi.rodriguez@gmail.com")
    file.close()
    
def copiarArchivo(urlOrigen, urlDestino):
    copyfile(urlOrigen, urlDestino)
    