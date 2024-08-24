import os
import platform

def limpiar_pantalla() -> None:
	os.system('cls') if platform.system() == 'windows' else os.system('clear')

def leer_entero(mensaje: str) -> int:
	numero = input(f'> {mensaje}: ')
	if not numero.isdigit():
		raise ValueError('Ingrese un numero entero positivo')
	return int(numero)