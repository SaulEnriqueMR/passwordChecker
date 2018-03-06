import re
from velocidad import T_PETICION

#Funciones
def findFails(pwd):
    seguridad = 100.0
    if pwd == "":
        seguridad = 0
        print("¡SIN CONTRASEÑA NO ESTARAS SEGURO!")
    elif pwd.isspace():
        seguridad = 11.1111
        print("Una contraseña así no te ayudará a estar seguro.")
    else:
        print("Recomendaciones para aumentar la seguridad de tu contraseña:")
        cad = ''.join(e for e in pwd if e.isalnum())
        if cad.isalnum():
            if cad.isdigit():
                seguridad -= 11.1111
                print("- Incluir letras en tu contraseña")
            elif cad.isalpha():
                seguridad -= 11.1111
                print("- Incluir números en tu contraseña")
        if pwd.islower():
            seguridad -= 22.2222
            print("- Incluir mayúsculas en tu contraseña")
        elif pwd.isupper():
            seguridad -= 22.2222
            print("- Incluir minúsculas en tu contraseña")
        elif pwd.istitle():
            seguridad -= 11.1111
            print("- Intercalar entre mayúsculas y minúsculas")
        if re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', pwd) is None:
            seguridad -= 33.3333
            print("- Incluir caracteres especiales")
        if len(pwd) < 8:
            seguridad -= 33.3333
            print("- Introducir como mínimo %d caracteres más" % (8-len(pwd)))
    return seguridad

class Tiempo:
    mil=0
    sec=0
    mins=0
    hrs=0
    days=0
    sem=0
    mes=0
    anos=0

    def calcTime(self):
        while self.mil>=1000:
            self.sec += 1
            self.mil -= 1000
            while self.sec>=60:
                self.mins += 1
                self.sec -=60
                while self.mins>=60:
                    self.hrs+=1
                    self.mins-=60
                    while self.hrs>=24:
                        self.days+=1
                        self.hrs-=24
                        while self.days>=7:
                            self.sem+=1
                            self.days-=7
                            while self.sem>= 4:
                                self.mes+=1
                                self.sem-=4
                                while self.mes>=12:
                                    self.anos+=1
                                    self.mes-=1

    def incrementarExp(self, mul):
        self.mil*=mul
        self.sec*=mul
        self.mins*=mul
        self.hrs*=mul
        self.days*=mul
        self.sem*=mul
        self.anos*=mul
        self.calcTime(self)

    def __str__(self):
        cad = ""
        if self.anos>0:
            cad+=str(self.anos) +" años "
        if self.mes>0:
            cad+=str(self.mes) +" meses "
        if self.sem>0:
            cad+=str(self.sem) +" semanas "
        if self.days>0:
            cad+=str(self.days) +" días "
        if self.hrs>0:
            cad+=str(self.hrs) +" horas "
        if self.mins>0:
            cad+=str(self.mins) +" minutos "
        if self.sec>0:
            cad+=str(self.sec) +" segundos y "
        if self.mil>0:
            cad+= str(self.mil) +" milisegundos."
        return cad


def calcDescubrir(pwd):
    tiempo = Tiempo
    cont = 1
    for c in pwd[::-1]:
        tiempo.mil += (ord(c)*T_PETICION)
        tiempo.incrementarExp(tiempo, cont)
        tiempo.calcTime(tiempo)
        cont+=1
    return tiempo.__str__(tiempo)


    



