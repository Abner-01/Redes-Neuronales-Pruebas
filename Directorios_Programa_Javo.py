# Esta función toma un directorio FUENTE conteniendo todos los archivos
# debe de existir un directorio de ENTRENAMIENTO, una parte irá al directorio
# de PRUEBA, el TAMAÑO DE PARTIDO determina la proción de los archivos.
# Necesita que las imagenes esten numeradas.
# a SPLIT SIZE to determine the portion
# The files should also be randomized, so that the training set is a random
# X% of the files, and the test set is the remaining files
# SO, for example, if SOURCE is PetImages/Cat, and SPLIT SIZE is .9
# Then 90% of the images in PetImages/Cat will be copied to the TRAINING dir
# and 10% of the images will be copied to the TESTING dir
# Also -- All images should be checked, and if they have a zero file length,
# they will not be copied over

# Se puede agregar el parámetro extra NOMBRE para asignar un nombre personalizado a los archivos
# en caso contrario, se asignara automáticamente ENTRENAMIENTO y PRUEBA respectivamente 


import cv2
import random
import os
from shutil import copyfile
import shutil


def separar_datos(FUENTE, ENTRENAMIENTO, PRUEBA, TAMANO_PARTICION, NOMBRE_ENTRENAMIENTO = None, NOMBRE_PRUEBA = None):
    
### Prueba de barra en la función
    if FUENTE[-1] != "/":
        FUENTE += "/"
    if ENTRENAMIENTO[-1] != "/":
        ENTRENAMIENTO += "/"
    if PRUEBA[-1] != "/":
        PRUEBA += "/"
        
### Borramos los directorios en caso de ya existir 
    if os.path.exists(ENTRENAMIENTO):
        shutil.rmtree(ENTRENAMIENTO)     
        
    if os.path.exists(PRUEBA):
        shutil.rmtree(PRUEBA)
        
    os.mkdir(ENTRENAMIENTO)
    os.mkdir(PRUEBA)  
     
#### Se crea una array vacio donde estarán todos los archivos
    archivos = []
          
#### Se recorren todos los archivos en FUENTE
    for elemento in os.listdir(FUENTE):
        datos = FUENTE + elemento
        if (os.path.getsize(datos) > 0):
            archivos.append(elemento)
        else:
            print('Se saltó el elemento' + elemento)
            print('Tamaño invalido! i.e Longitud Zero.')

    longitud_data_entremiento = int(len(archivos) *  TAMANO_PARTICION)
    longitud_data_prueba = int(len(archivos) - longitud_data_entremiento)
    conjunto_aleatorio = random.sample(archivos, len(archivos))
    conjunto_entrenamiento = conjunto_aleatorio[0:longitud_data_entremiento]
    conjunto_prueba = conjunto_aleatorio[-longitud_data_prueba:]

    for elementos in conjunto_entrenamiento:
        temp_train_data = FUENTE + elementos
        final_train_data =  ENTRENAMIENTO + elementos
        copyfile(temp_train_data, final_train_data)

    for elementos in conjunto_prueba:
        temp_test_data = FUENTE + elementos
        final_test_data =  PRUEBA + elementos
        copyfile(temp_train_data, final_test_data)
# AQUÍ TERMINA EL CODIGO PARA REPARTIR EN CONJUNTOS DE ENTRENAMIENTO Y PRUEBA 



# AQUÍ EMPIEZA EL CÓDIGO PARA CAMBIAR NOMBRES
    contador_de_archivos = 0 #Este va a ser un iterador externo para enumerar los archivos
    
    os.chdir(PRUEBA)
    os.chdir(ENTRENAMIENTO)
    if NOMBRE_ENTRENAMIENTO is None:  #Si no tiene un nombre personalizado de entrenamiento
        for i in os.listdir(ENTRENAMIENTO):
            contador_de_archivos += 1
            imagen = cv2.imread(i)
            cv2.imwrite('imagen.jpg', imagen, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            os.rename('imagen.jpg', "ENTRENAMIENTO_" + str(contador_de_archivos) + '.jpg')
            os.remove(i)
        contador_de_archivos = 0
        
    
    os.chdir(PRUEBA)
    if NOMBRE_PRUEBA is None: #Si no tiene un nombre personalizado de prueba
        for i in os.listdir(PRUEBA):
            contador_de_archivos += 1
            imagen = cv2.imread(i)
            cv2.imwrite('imagen.jpg', imagen, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
            os.rename('imagen.jpg', "PRUEBA_" + str(contador_de_archivos) + '.jpg')
            os.remove(i)
        contador_de_archivos = 0
    
    os.chdir(ENTRENAMIENTO)
    if NOMBRE_ENTRENAMIENTO is not None:  #Si tiene un nombre personalizado de entrenamiento
        for i in os.listdir(ENTRENAMIENTO):
            contador_de_archivos += 1
            imagen = cv2.imread(i)
            cv2.imwrite('imagen.jpg', imagen, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
            os.rename('imagen.jpg', NOMBRE_ENTRENAMIENTO + str(contador_de_archivos) + '.jpg')
            os.remove(i)
        contador_de_archivos = 0
        
    os.chdir(PRUEBA) 
    if NOMBRE_PRUEBA is not None: #Si tiene un nombre personalizado de prueba 
        for i in os.listdir(PRUEBA):
            contador_de_archivos += 1
            imagen = cv2.imread(i)
            cv2.imwrite('imagen.jpg', imagen, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) 
            os.rename('imagen.jpg', NOMBRE_PRUEBA + str(contador_de_archivos) + '.jpg')
            os.remove(i)
        contador_de_archivos = 0
     




   
FUENTE = "D:/PruebasRedesNeuronales/fuente"
ENTRENAMIENTO = "D:/PruebasRedesNeuronales/entrenamiento"
PRUEBA = "D:/PruebasRedesNeuronales/prueba"
TAMAÑO_PARTICION = .8

separar_datos(FUENTE, ENTRENAMIENTO, PRUEBA, TAMAÑO_PARTICION, NOMBRE_ENTRENAMIENTO = "linda", NOMBRE_PRUEBA = "te_extrano" )