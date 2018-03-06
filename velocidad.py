import platform

dicto = { 
    'i386':30,
    'Intel64 Family 6 Model 42 Stepping 7, GenuineIntel':60,
    'Intel64 Family 6 Model 78 Stepping 3, GenuineIntel':45,
    }

def velocidad():
    VELOCIDAD_PROM = 50
    procesador = platform.processor()
    if procesador in dicto:
        return dicto[procesador]
    else:
        return VELOCIDAD_PROM

T_PETICION = velocidad()