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


import random
import os
from shutil import copyfile
import shutil
#Jeje

def separar_datos(FUENTE, ENTRENAMIENTO, PRUEBA, TAMANO_PARTICION, NOMBRE_ENTRENAMIENTO = None, NOMBRE_PRUEBA = None):
### Borramos los directorios en caso de ya existir 
### Para ENTRENAMIENTO
    if os.path.exists(ENTRENAMIENTO):
        shutil.rmtree(ENTRENAMIENTO)
### Para PRUEBA
    if os.path.exists(PRUEBA):
        shutil.rmtree(PRUEBA)
    os.mkdir(ENTRENAMIENTO)
    os.mkdir(PRUEBA)
    
#### Se crea una array vacio donde estarán todos los archivos
    archivos = []
    
### Prueba de barra en la función
    if FUENTE[-1] != "/":
        FUENTE += "/"
    if ENTRENAMIENTO[-1] != "/":
        ENTRENAMIENTO += "/"
    if PRUEBA[-1] != "/":
        PRUEBA += "/"
        
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
        
    if NOMBRE_ENTRENAMIENTO is None:  #Si no tiene un nombre personalizado de entrenamiento
        os.chdir(ENTRENAMIENTO) 
        for i in os.listdir(ENTRENAMIENTO):
            contador_de_archivos += 1
            nombre_del_archivo, extension = os.path.splitext(i)#Obtenemos la extension 
            os.rename(i, "ENTRENAMIENTO_" + str(contador_de_archivos) + extension)
        contador_de_archivos = 0
        
    if NOMBRE_PRUEBA is None: #Si no tiene un nombre personalizado de prueba
        os.chdir(PRUEBA) 
        for i in os.listdir(PRUEBA):
            contador_de_archivos += 1
            nombre_del_archivo, extension = os.path.splitext(i)#Obtenemos la extension 
            os.rename(i, "PRUEBA_" + str(contador_de_archivos) + extension)
        contador_de_archivos = 0
    
    if NOMBRE_ENTRENAMIENTO is not None:  #Si tiene un nombre personalizado de entrenamiento
        os.chdir(ENTRENAMIENTO) 
        for i in os.listdir(ENTRENAMIENTO):
            contador_de_archivos += 1
            nombre_del_archivo, extension = os.path.splitext(i)#Obtenemos la extension 
            os.rename(i, NOMBRE_ENTRENAMIENTO + str(contador_de_archivos) + extension)
        contador_de_archivos = 0
        
    if NOMBRE_PRUEBA is not None: #Si tiene un nombre personalizado de prueba
        os.chdir(PRUEBA) 
        for i in os.listdir(PRUEBA):
            contador_de_archivos += 1
            nombre_del_archivo, extension = os.path.splitext(i)#Obtenemos la extension 
            os.rename(i, NOMBRE_PRUEBA + str(contador_de_archivos) + extension)
        contador_de_archivos = 0
     




   
FUENTE = "D:/felip/Redes_Neuronales_Team/Redes-Neuronales-Pruebas/Prueba del programa/FUENTE"
ENTRENAMIENTO = "D:/felip/Redes_Neuronales_Team/Redes-Neuronales-Pruebas/Prueba del programa/ENTRENAMIENTO/"
PRUEBA = "D:/felip/Redes_Neuronales_Team/Redes-Neuronales-Pruebas/Prueba del programa/PRUEBA"
TAMAÑO_PARTICION = .8

separar_datos(FUENTE, ENTRENAMIENTO, PRUEBA, TAMAÑO_PARTICION, NOMBRE_ENTRENAMIENTO = "ABNER_MI_PERRO", NOMBRE_PRUEBA = "JAVO_TAMBOR" )