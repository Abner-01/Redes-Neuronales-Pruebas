#Creación de directorios y llenado de imágenes
#22/Enero/2021
#F.Alvarez

import os 
import random
import shutil
import glob

#Función que crea los directorios en un directorio determinado xdxd
def creamos_directorios_en(lugar):
    # Directorios a crear
    directorios = ["train/", "test/", "validation/"]
     
    # Directorio Padre 
    parent_dir = str(lugar)
      
    # Rutas
    rutas = []
    for directorio in directorios:
        rutas.append(os.path.join(parent_dir, directorio))
    
    # Si existen ya los directorios, los borramos
    for ruta in rutas:
        if os.path.exists(ruta):
            shutil.rmtree(ruta)
    
    # Creamos los directorios principales:
    for ruta in rutas:
        if not os.path.exists(ruta):
            os.mkdir(ruta)
   
    # Rutas secundarias
    perro = "dog"
    gato = "cat"
    rutas_especificas = []
    for ruta in rutas:
        rutas_especificas.append(os.path.join(ruta, perro))
        rutas_especificas.append(os.path.join(ruta, gato))
    
    # Creamos los directorios secundarios
    for ruta in rutas_especificas:
        if not os.path.exists(ruta):
            os.mkdir(ruta)
                        
# Llena con las imágenes los directorios
def llenamos_directorios(lugar):
    # Obtenemos las rutas de las carpetas
    os.chdir(lugar)
    directorios = ["train/", "test/", "validation/"]
    parent_dir = str(lugar)
    rutas = []
    for directorio in directorios:
        rutas.append(os.path.join(parent_dir, directorio))
    perro = "dog"
    gato = "cat"
    rutas_especificas = []
    for ruta in rutas:
        rutas_especificas.append(os.path.join(ruta, perro))
        rutas_especificas.append(os.path.join(ruta, gato))
    
    # Repartimos las fotos en train 500 imágenes
    for imperro in random.sample(glob.glob("train/dog*"),500):
        shutil.move(imperro, rutas_especificas[0])
    for imgato in random.sample(glob.glob("train/cat*"),500):
        shutil.move(imgato, rutas_especificas[1])    
    # Repartimos para valid 100 imágenes
    for imperro in random.sample(glob.glob("train/dog*"),100):
        shutil.move(imperro, rutas_especificas[2])
    for imgato in random.sample(glob.glob("train/cat*"),100):
        shutil.move(imgato, rutas_especificas[3])
    # Repartimos para test 50 imágenes
    for imperro in random.sample(glob.glob("train/dog*"),50):
        shutil.move(imperro, rutas_especificas[4])
    for imgato in random.sample(glob.glob("train/cat*"),50):
        shutil.move(imgato, rutas_especificas[5])

            
#Ejemplo al llamar las funciones:            
#creamos_directorios_en("C:/Users/52554/Desktop/Felipe/Python/Red_perrazos/") 
#llenamos_directorios("C:/Users/52554/Desktop/Felipe/Python/Red_perrazos/")      