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



import random
import os
from shutil import copyfile


def separar_datos(FUENTE, ENTRENAMIENTO, PRUEBA, TAMANO_PARTICION):
#### Se crea una array vacio donde estarán todos los archivos
    archivos = []
    
### Prueba de barra en la función
    if FUENTE[-1] != "/":
        FUENTE += "/"
        
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
# YOUR CODE ENDS HERE
CAT_SOURCE_DIR = "/tmp/PetImages/Cat/"
TRAINING_CATS_DIR = "/tmp/cats-v-dogs/training/cats/"
TESTING_CATS_DIR = "/tmp/cats-v-dogs/testing/cats/"
DOG_SOURCE_DIR = "/tmp/PetImages/Dog/"
TRAINING_DOGS_DIR = "/tmp/cats-v-dogs/training/dogs/"
TESTING_DOGS_DIR = "/tmp/cats-v-dogs/testing/dogs/"

split_size = .9
separar_datos(CAT_SOURCE_DIR, TRAINING_CATS_DIR, TESTING_CATS_DIR, split_size)
separar_datos(DOG_SOURCE_DIR, TRAINING_DOGS_DIR, TESTING_DOGS_DIR, split_size)