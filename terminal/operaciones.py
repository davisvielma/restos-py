import os
import platform
import re

def limpiar_pantalla() -> None:
	os.system('cls') if platform.system() == 'windows' else os.system('clear')

def leer_entero(mensaje: str) -> int:
	numero = input(f'> {mensaje}: ')

	if not re.match('[\-]?[0-9]*[0-9]$', numero):
		raise ValueError('Ingrese un numero entero')
	return int(numero)

def leer_texto(mensaje: str) -> str:
	while True:
		texto = input(f'> {mensaje}: ')
		if len(texto) != 0:
			return texto