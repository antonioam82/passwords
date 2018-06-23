import subprocess
from VALID import ns, OKI, opt

while True:
    print("¿Que desea generar?")
    print("A)CONTRASEÑA SEGURA")
    print("B)URL SEGURA")
    opci=opt(input("Introduzca aquí su opción: "),["A","B"])#ESCRIBIR SOLO "A" o "B". 

    if opci==("A"):
        import random
        import string
        minus=OKI(input("Indique número minimo de minusculas: "))
        mayus=OKI(input("Indique número minimo de mayusculas: "))
        numeros=OKI(input("Indique número minimo de caracteres numéricos: "))
        longitud=OKI(input("Indique logitud de la contraseña: "))
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
    else:
        import secrets
        bits=OKI(input("Introduzca número de bits: "))
        url=secrets.token_urlsafe(bits)
        print("URL: ",url)
    conti=ns(input("¿Desea continuar?: "))
    if conti==("n"):
        break
    subprocess.call(["cmd.exe","/C","cls"])
