# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:58:23 2023

@author: SENATI05
"""


class constantes:
    def codigo_inicial(self):
        return 
    1437580

class persona:
    def __init__(self, nombre, dni, codigo, sexo):
        self.nombre = nombre
        self.dni = dni
        self.codigo = codigo
        self.sexo = sexo
        
    def generarcorreo(self):
        return "metodo que sera alterado"
    
class alumno(persona):
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2
        
    def calcpromedio(self):
        return "El promedio es: {}".format((self.nota1+self.nota2)/2)
    
    def generarcorreo(self, codigoaux):
        return "El codigo del alumno es 00{}@senati.pe".format((codigoaux+1))
    
class profesor(persona):
    def __init__(self, tarifa, hora):
        self.tarifa = tarifa
        self.hora = hora
    
    def generarsueldo(self):
        return "El sueldo del profesor es : {}".format((self.tarifa*self.hora))
    
    def generarcorreo(self,nombreaux):
        return "El correo del profesor es: {}@senati.pe".format(nombreaux)
    
const = constantes();

print(const.codigo_inicial())

nombre2 = str(input("Nombre del alumno: "))
dni2 = str(input("DNI del alumno: "))
sexo2 = str(input("Sexo del alumno: "))

n1 = int(input("Ingrese nota 1: "))
n2 = int(input("Ingrese nota 2: ")) 

alu = alumno(n1, n2)

alu.nombre = nombre2
alu.dni =dni2
alu.codigo = (const.codigo_inicial()+1)
alu.sexo = sexo2

print(alu.nombre)   
print(alu.dni)   
print(alu.codigo)   
print(alu.sexo)   

print(alu.calcpromedio())
print(alu.generarcorreo(const.codigo_inicial()))


print(alu.codigo+1)

nombre3 = str(input("Nombre del profesor: "))
dni3 = str(input("DNI del profesor: "))
sexo3 = str(input("Sexo del profesor: "))

t1 = int(input("Ingrese tarifa: "))
h1 = int(input("Ingrese horas: "))

prof = profesor(t1, h1)

prof.nombre = nombre3
prof.dni = dni3
prof.codigo = int(alu.codigo+1)
prof.sexo = sexo3

print(prof.nombre)
print(prof.dni)
print(prof.codigo)
print(prof.sexo)

print(prof.generarsueldo())
print(prof.generarcorreo(prof.nombre))