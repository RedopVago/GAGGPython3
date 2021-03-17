#import pickle
import shelve
#import sys
# from idestudiante import estudiante as est  # [PV] Error en el nombre del Modulo
from IDestudiante2 import estudiante as est
#import os
# import mydict
from mongoengine import *
from datetime import datetime

connect('IECA',host='localhost',port=27017)


class Estudiante(Document):
    nombre = StringField(required=True)
    correo = StringField(required=True)
    contraseña = StringField(required=True)
    materias = StringField(required=True)
    asistencia = ListField(DateTimeField())


def subir(file,key):
    objeto=file[key]
    nombre, correo, contraseña, materias = objeto.getDatos()
    estudiante=Estudiante(
        nombre=nombre,
        correo=correo,
        contraseña=contraseña,
        materias=materias
    )
    estudiante.save()


def registro(file):
    print("Introduce el nombre del estudiante:")
    nombre = input()
    print("Introduce el correo del estudiante:")
    correo = input()
    print("Introduce la contraseña:")
    contraseña = input()
    print("Introduce las materias:")
    materias = input()
    sestudiante = est(nombre, correo, contraseña, materias)
    file[nombre]=sestudiante
    print("Estudiante registrado")
    print()
    return nombre


def lectura(file,nombre):
    lectura=file[nombre]
    print(f'Los datos del estudiante son: {lectura.getDatos()}')


def actualizar(file,nombre):
    print("Introduce el nuevo nombre del estudiante:")
    renombre = input()
    print("Introduce el nuevo correo del estudiante:")
    correo = input()
    print("Introduce la  nueva contraseña:")
    contraseña = input()
    print("Introduce las materias:")
    materias = input()
    datos=file[nombre]
    datos.setDatos(renombre, correo, contraseña, materias)
    renombre, correo, contraseña,materias = datos.getDatos()
    #file[nombre]=datos
    file[renombre]=datos
    del file[nombre]

    print(f"Nombre actualizado: {renombre}\nCorreo actualizado: {correo}\nContraseña actualizada: {contraseña}\nMateria actualizada: {materias}\n ")
    return renombre


def eliminar(file,nombre):
    del file[nombre]
    print("Nombre eliminado")


if __name__ == '__main__':
    print('hola')
    #directorio = {}
    #keys = []
    #continuar= True
    while(True):
        with shelve.open("studentsIO.db") as file:
            print("Que desea hacer?:")
            print("Registrar -> 1")
            print("Revisar datos -> 2")
            print("Actualizar datos -> 3")
            print("Eliminar dato -> 4")
            print("Subir a la nube -> 5")
            print("Salir -> 6")
            eleccion = int(input())
            if (eleccion == 1):
                # Registro del alumno
                nombre = registro(file)
                #directorio[nombre] = nombre
                #keys.append(nombre)
            elif (eleccion == 2):
                # Lectura de datos del alumno
                print("Ingrese el nombre del alumno a revisar")
                nombre = input()
                try:
                    #key=directorio[nombre]
                    lectura(file, nombre)
                except (KeyError,NameError):
                    print("Estudiante no registrado")

            elif (eleccion == 3):
                # Actualización de datos
                print("Ingrese el nombre del alumno a actualizar")
                nombre = input()

                try:
                    file[nombre]
                    #key=directorio[nombre]
                    renombre = actualizar(file, nombre)

                except (KeyError,NameError):
                    print("Estudiante no registrado")

            elif (eleccion == 4):
                # Eliminar datos
                print("Ingrese el nombre del alumno a eliminar")
                nombre = input()
                try:
                    file[nombre]
                    eliminar(file, nombre)
                    # directorio[nombre] = renombre
                except (KeyError,NameError):
                    print("Estudiante no registrado")

            elif (eleccion == 5):
                # Eliminar datos
                print("Inserte el nombre del estudiante para el cual se subiran los datos a la nube")
                nombre = input()
                try:
                    file[nombre]
                    print('nelson mandela')
                    subir(file, nombre)
                except (KeyError,NameError):
                    print("Estudiante no registrado")
                    print()
            elif (eleccion == 6):
                # salir
                continuar = False
            else:
                print("No selecciono correctamente")








"""
def registro(file):
    print("Introduce el nombre del estudiante:")
    nombre = input()
    print("Introduce el correo del estudiante:")
    correo = input()
    print("Introduce la contraseña:")
    contraseña = input()
    print("Introduce las materias:")
    materias = input()
    estudiante = est(nombre,correo,contraseña,materias)
    tam=sys.getsizeof(estudiante)
    print(tam)
    pickle.dump(estudiante,file)
    return nombre,tam

def lectura(file,tama,indice):
        posicion=tama*indice
        print(posicion)
        file.seek(posicion)
        unpickler = pickle.Unpickler(file)
        read_estudiante = unpickler.load()
        print(f'Los datos del estudiante son: {read_estudiante.getDatos()}')


def actualizar(file,rename,nuevocorreo,nuevacontra):
    file.seek(0)
    unpickler = pickle.Unpickler(file)
    rename_estudiante = unpickler.load()
    rename_estudiante.setDatos(rename,nuevocorreo,nuevacontra)
    nombre, correo, contraseña = rename_estudiante.getDatos()
    print(f"Nombre actualizado: {nombre}\nCorreo actualizado: {correo}\nContraseña actualizada: {contraseña}\n ")
def eliminar(file):
    pass

if __name__ == '__main__':
    directorio={}
    for i in range(2):
        with open('Estudiantes.db','wb+') as file:
            # Registro
            name,tama=registro(file)
            lista=[tama,i]
            directorio[name]=lista
            print("ingrese el nombre del estudiante al cual se accedera:")
            estudiante=input()
            valor = directorio[estudiante]
            print(valor)
            # Lectura
            lectura(file,valor[0],valor[1])

            # Actualizar
            print("Por que valor deseas actualizar el nombre?:")
            rename = input()
            print("Por que valor deseas actualizar el correo?:")
            nuevocorreo = input()
            print("Por que valor deseas actualizar la contrasenia?:")
            nuevacontra = input()
            actualizar(file,rename,nuevocorreo,nuevacontra)
            """













    
