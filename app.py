from config import RED, RESET, LIMITE_INFERIOR, LIMITE_SUPERIOR
from terminal.menu import menu
from terminal import operaciones
from herramientas import cadenas
from herramientas import algebra

def main() -> None:
	while True:
		try:
			operaciones.limpiar_pantalla()
			menu()
			opcion = operaciones.leer_entero('Opción')

			if opcion < LIMITE_INFERIOR or opcion > LIMITE_SUPERIOR:
				raise ValueError(f'Ingrese un entero entre {LIMITE_INFERIOR} y {LIMITE_SUPERIOR}')

			print()

			if opcion == 1:
				texto = operaciones.leer_texto('Ingrese una cadena de texto')
				print(f'Cadena original:  \"{texto.strip()}\"')
				print(f'Cadena invertida: \"{cadenas.invertir(texto)}\"')
			elif opcion == 2:
				texto = operaciones.leer_texto('Ingrese una cadena de texto')
				print(f'Numero de la palabras: {cadenas.contador_de_palabras(texto)}')
			elif opcion == 3:
				texto = operaciones.leer_texto('Ingrese una el nombre de una organización')
				print(f'Acrónimo: {cadenas.acronimos(texto)}')
			elif opcion == 4:
				numero = operaciones.leer_entero('Ingrese un numero')
				resultado = 'par' if algebra.es_par(numero) else 'impar'
				print(f'El numero {numero} es {resultado}')
			elif opcion == 5:
				numero = operaciones.leer_entero('Ingrese un numero')
				algebra.controlador_factorial(algebra.factorial_recursivo, numero)
				algebra.controlador_factorial(algebra.factorial_iterativo, numero)
			elif opcion == 6:
				print('666')
			elif opcion == 7:
				texto = operaciones.leer_texto('Ingrese una oración')
				resultado = 'si' if cadenas.palindromo(texto) else 'no'
				print(f'La cadena \"{texto}\" {resultado} es palindromo')
			else:
				break			
		except ValueError as e:
			print(RED + f'\nERROR!!! {e}.' + RESET)
		finally:
			input('\nPresione ENTER para continuar...')


if __name__ == '__main__':
	main()