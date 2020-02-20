import random
import string
import sys
import subprocess

def ns(r):
    while r!="n" and r!="s":
        r=input("Escriba solo \'n\' o \'s\' según su opción: ")
    return r

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n

def opt(o,l):
    while o not in l:
        o=input("Escriba solo una de las opciónes posibles: ")
    return o

ops=sys.platform

while True:
    print("*******GENERADOR DE CONTRASEÑAS*******")
    minus=OKI(input("Indique número mínimo de minusculas: "))
    mayus=OKI(input("Indique número mínimo de mayusculas: "))
    numeros=OKI(input("Indique número mínimo de caracteres numéricos: "))
    longitud=OKI(input("Indique longitud de la contraseña: "))
    suma=minus+mayus+numeros #SUMA DE MINIMOS
    while longitud<suma: #COMPROBACION ADECUACIÓN DE LA "longitud".
        longitud=OKI(input("Longitud inadecuada: "))
    caract=string.ascii_letters+string.digits
    while True:
        contra=("").join(random.choice(caract)for i in range(longitud))
        if(sum(c.islower() for c in contra)>=minus
            and sum(c.isupper() for c in contra)>=mayus
            and sum(c.isdigit() for c in contra)>=numeros):
            break
    print("")
    print("SU CONTRASEÑA: ",contra)
    print("")
    
    conti=ns(input("¿Desea continuar?(s/n): "))
    if conti==("n"):
        break
    if ops=="win32" or ops=="linux2":
        if ops=="win32":
            import subprocess
            subprocess.call(["cmd.exe","/C","cls"])
        else:
            os.system("clear")
    else:
        continue
