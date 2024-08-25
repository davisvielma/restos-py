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

def fibonacci_recursivo(numero: int) -> int:
	if numero < 0:
		raise ValueError('Ingrese un numero entero positivo')

	if numero <= 1:
		return numero
	return fibonacci_recursivo(numero - 1) + fibonacci_recursivo(numero - 2)

def fibonacci_iterativo(numero: int) -> int:
	if numero < 0:
		raise ValueError('Ingrese un numero entero positivo')

	f0 = 0
	f1 = 1
	while numero > 0:
		f = f0 + f1
		f0 = f1
		f1 = f
		numero -= 1
	return f0