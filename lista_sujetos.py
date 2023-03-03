import numpy as np
import random
from faker import Faker



numeros_de_cuenta = []
nombres_alumnos = []
materias_reprobadas = []
def crea_numeros_cuenta():

    for i in range(5000):

        cuenta = ''.join([str(random.randrange(10))for j in (range(9))])
        
        if cuenta.startswith('4') and cuenta[1] == '1' and cuenta[2] == '7':
            numeros_de_cuenta.append(cuenta)
        
        if cuenta.startswith('4') and cuenta[1] =='1' and cuenta[2] == '8':
            numeros_de_cuenta.append(cuenta)
    print(numeros_de_cuenta)
    print(len(numeros_de_cuenta))

def crea_nombres():
    fake=Faker()

    for i in range(400):
        nombre = fake.name()
        nombres_alumnos.append(nombre)

    print(nombres_alumnos)

def adeudo_materias():
   

    for i in range(10):

        x = random.randint(0,1)

        if x == 1:
            materias_reprobadas.append("yes")
        if x == 0:
            materias_reprobadas.append("no")
    
    print(materias_reprobadas)




crea_numeros_cuenta()
#crea_nombres()
#adeudo_materias()


