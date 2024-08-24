def invertir(cadena: str) -> str:
	return cadena[::-1].strip()

def contador_de_palabras(cadena: str) -> str:
	lista = cadena.strip().split(' ')
	return len(lista)