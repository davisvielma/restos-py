def invertir(cadena: str) -> str:
	return cadena[::-1].strip()

def contador_de_palabras(cadena: str) -> str:
	lista = cadena.strip().split(' ')
	return len(lista)

def acronimos(cadena: str) -> str:
	lista = cadena.strip().title().split(' ')
	texto = ''
	for palabra in lista:
		texto += palabra[0]
	return texto

def palindromo(cadena: str) -> bool:
	lista = cadena.strip().lower().split(' ')
	texto = ''.join(lista)
	return texto == invertir(texto)
