from config import RED, RESET, LIMITE_INFERIOR, LIMITE_SUPERIOR
from terminal.menu import menu
from terminal import operaciones
from herramientas import cadenas

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
				print('444')
			elif opcion == 5:
				print('555')
			elif opcion == 6:
				print('666')
			elif opcion == 7:
				texto = operaciones.leer_texto('Ingrese una oración')
				resultado = 'verdadero' if cadenas.palindromo(texto) else 'falso'
				print(f'Resultado: {resultado}')
			else:
				break			
		except ValueError as e:
			print(RED + f'\nERROR!!! {e}.' + RESET)
		finally:
			input('\nPresione ENTER para continuar...')


if __name__ == '__main__':
	main()