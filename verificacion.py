def buscarEnDiccionario(contrasenaIngresada):
	with open("common-passwords.txt", "r", encoding='utf8') as archivo:
		contrasenas = archivo.read().split("\n")
	if any(contrasenaIngresada in s for s in contrasenas):
		return(True)
	else:
		return(False)

def buscarRepeticion(contrasenaIngresada):
	numeroDeRepeticiones = 0
	letrasSinRepetir = ""
	for indice in range(0, len(contrasenaIngresada)):
		if not contrasenaIngresada[indice] in letrasSinRepetir:
			letrasSinRepetir += contrasenaIngresada[indice]
		else:
			if indice + 1 < len(contrasenaIngresada) and contrasenaIngresada[indice+1] in letrasSinRepetir:
				numeroDeRepeticiones += 1
			else:
				letrasSinRepetir += contrasenaIngresada[indice]
	if numeroDeRepeticiones == 0:
		return(False)
	else:
		return(True)

def buscarPatron(contrasenaIngresada):
	listaPatrones = ['qwerty', 'qwertyuiop', '1qaz2wsx', 'qazwsx', 'asdfg', 'zxcvbnm', '1234qwer', 'q1w2e3r4t5', 'qwer1234', 'q1w2e3r4', 'asdfasdf', 'qazwsxedc', 'asdfghjkl', 'q1w2e3', '1qazxsw2', '12QWaszx', 'qweasdzxc', 'mnbvcxz', 'a1b2c3d4', 'adgjmptw']
	for patron in listaPatrones:
		if patron in contrasenaIngresada:
			return(True)
	return(False)