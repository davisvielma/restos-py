import os
import platform
import re
import time

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

def controlador_de_funcion(funcion, numero: int) -> None:
	print(f'\n{funcion.__name__}')
	print('===================')
	inicio = time.time()
	resultado = funcion(numero)
	fin = time.time()
	print(f'Resultado: {resultado}')
	print(f'Tiempo de ejecucion: {fin - inicio} segundos')