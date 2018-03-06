from velocidad import T_PETICION
import re

CURP =r"[A-Z]{4}\d{6}[A-Z]{6}\d{2}"
#pwd = "ROCA930620HDFDSN08" #PRUEBA

def incNum(digito):
    d = ord(digito)
    if d == 57:
        return chr(48)
    d += 1
    return chr(d)

def incLet(letra):
    l = ord(letra)
    if l == 90:
        return chr(65)
    l += 1
    return chr(l)

def incChar(char):
    if ord(char) <= 57:
        return incNum(char)
    elif ord(char) <= 90:
        return incLet(char)

def cambiar(cadena, letra, pos):
    c = list(cadena)
    c[pos] = letra
    return "".join(c) 

def incrementar(cadena, pos=1):
    i = cadena[-pos]
    i = incChar(i)
    if not i == '0' or i == 'A' or i == 'a':
        return cambiar(cadena, i, -pos)
    else:
        cad = cambiar(cadena, i, -pos)
        return incrementar(cad, pos+1)

def calcTime(milisegundos):
    mil=milisegundos
    cad = str(mil) + " milisegundos"
    sec=0
    mins=0
    hrs=0
    days=0
    sem=0
    mes=0
    anos=0
    if mil>=1000:
        sec = int(mil/1000)
        mil = mil%1000
        if mil:
            cad= str(mil) + " milisegundos"
    if sec>=60:
        mins = int(sec/60)
        sec = sec%60
        if sec:
            cad = str(sec) + " segundos y " + cad 
    if mins>=60:
        hrs = int(mins/60)
        mins = mins%60
        if mins:
            cad = str(mins) + " minutos, " + cad
    if hrs>=24:
        days = int(hrs/24)
        hrs = hrs%24
        if hrs:
            cad = str(hrs) + " horas, " + cad
    if days>=7:
        sem = int(days/7)
        days = days%7
        if days:
            cad = str(days) + " día(s), " + cad
    if sem>=4:
        mes = int(sem/4)
        sem = sem%4
        if sem:
            cad = str(sem) + " seman(as), " + cad
    if mes>=12:
        anos = int(mes/12)
        mes = mes%12
        if mes:
            cad = str(mes) + " mes(es), " + cad
    if anos:
        cad = str(anos) + " años, " + cad
    return cad
    

def hackCURP(pwd):
    if re.match(CURP, pwd):
        hack = "AAAA000000AAAAAA00"
        tiempo = 0
        while not hack == pwd:
            hack = incrementar(hack)
            print(hack)
            tiempo += T_PETICION
        print(tiempo)
    else: 
        return -1

def valorLetra(letra):
    if letra.islower():
        return ord(letra)-ord('a')
    else:
        return ord(letra)-ord('A')
    
#Si no conoce nada = 0
#Si conoce nombre = 1
#Si conoce nombre y fecha de nacimiento = 2
#Si conoce nombre, fecha de nacimiento y lugar de nacimiento = 3
#Si conoce todos sus datos = 4
def calcCURP(pwd, conoce=0):
    if re.match(CURP, pwd):
        tiempo = 1
        op = []
        if conoce < 1:
            for c in pwd[0:4]:
                op.append(valorLetra(c))
        if conoce < 2:
            for c in pwd[4:10]:
                op.append(int(c))
        if conoce < 3:
            for c in pwd[10:16]:
                op.append(valorLetra(c))
        if conoce < 4:
            for c in pwd[16:]:
                op.append(int(c))
        for n in op:
            if n:
                tiempo *= n
        return calcTime(tiempo*T_PETICION)
    else:
        return -1
