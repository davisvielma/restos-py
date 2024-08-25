import time

def es_par(numero: int) -> bool:
	return numero % 2 == 0

def factorial_recursivo(numero: int) -> int:
	if numero < 0:
		raise ValueError('Ingrese un numero entero positivo')

	if numero ==  0 or numero == 1:
		return 1
	return factorial_recursivo(numero - 1) * numero

def factorial_iterativo(numero: int) -> int:
	if numero < 0:
		raise ValueError('Ingrese un numero entero positivo')

	resultado = 1
	while numero > 1:
		resultado *= numero
		numero -= 1
	return resultado

def controlador_factorial(funcion, numero: int) -> None:
	print(f'\n{funcion.__name__}')
	print('===================')
	inicio = time.time()
	resultado = funcion(numero)
	fin = time.time()
	print(f'El factorial de {numero} es {resultado}')
	print(f'Su tiempo de ejecucion es {fin - inicio} segundos')

