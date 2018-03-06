from medidorPass import Tiempo, calcDescubrir, findFails
from curpFB import calcCURP, hackCURP, CURP

import getpass
import re

print("Esta es una herramienta basada en python. \nSu finalidad es: \n - Medir la seguridad de una contraseña \n - Revisar el tiempo promedio en que podría ser descubierta")
print("---------------------------------------------------")
print("\nIntroduce la contraseña a detectar:")

#try:
pwd = getpass.getpass()
seguridad = findFails(pwd)
if seguridad == 100:
    print("Sin recomendaciones\n\nFelicidades. \nTu contraseña cumple con todas las especificaciones de seguridad del estandar de INTECO.\n")
print("Tu contraseña es %.2f%% segura\n" % seguridad)  

    #Cálculo de tiempo de hallar la contraseña.
print("---------------------------------------------------")
print("\nAhora calcularemos el tiempo en que tardaríamos en encontrar tu contraseña por fuerza bruta:")
if re.match(CURP, pwd):
    print("No deberías poner tu CURP o RFC. Sabiendo que la has puesto, tardarían:\n")
    print(calcCURP(pwd) + " si no conocen nada de ti.\n")
    print(calcCURP(pwd, 1) + " si conocen tu nombre.\n")
    print(calcCURP(pwd, 2) + " si conoce nombre y fecha de nacimiento.\n")
    print(calcCURP(pwd, 3) + " si conoce nombre, fecha de nacimiento y lugar de nacimiento.\n")
    print(calcCURP(pwd, 4) + " si saben toda tu información (Porque es alguien cercano o te investigaron en redes ).\n")

    #elif Está dentro del diccionario SAUL, TE TOCA

else:
    print("El tiempo que tardaríamos en encontrar tu contraseña por fuerza bruta es: ")
    print(calcDescubrir(pwd))
#except Exception as err:
    #print('ERROR:', err)