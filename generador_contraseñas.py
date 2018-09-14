import subprocess
from VALID import ns, OKI, opt
import random
import string

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
        contraseña=("").join(random.choice(caract)for i in range(longitud))
        if(sum(c.islower() for c in contraseña)>=minus
            and sum(c.isupper() for c in contraseña)>=mayus
            and sum(c.isdigit() for c in contraseña)>=numeros):
            break
    print("")
    print("SU CONTRASEÑA: ",contraseña)
    print("")
    
    conti=ns(input("¿Desea continuar?: "))
    if conti==("n"):
        break
    try:
        subprocess.call(["cmd.exe","/C","cls"])
    except:
        continue
