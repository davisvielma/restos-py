from config import RED, RESET, LIMITE_INFERIOR, LIMITE_SUPERIOR
from terminal.menu import menu
from terminal.operaciones import leer_entero, limpiar_pantalla

def main() -> None:
	while True:
		try:
			limpiar_pantalla()
			menu()
			opcion = leer_entero('Opción')

			if opcion < LIMITE_INFERIOR or opcion > LIMITE_SUPERIOR:
				raise ValueError(f'Ingrese un entero entre {LIMITE_INFERIOR} y {LIMITE_SUPERIOR}')

			print()

			if opcion == 1:
				print('111')
			elif opcion == 2:
				print('222')
			elif opcion == 3:
				print('333')
			elif opcion == 4:
				print('444')
			elif opcion == 5:
				print('555')
			elif opcion == 6:
				print('666')
			elif opcion == 7:
				print('777')
			else:
				break			
		except ValueError as e:
			print(RED + f'\nERROR!!! {e}.' + RESET)
		finally:
			input('\nPresione ENTER para continuar...')


if __name__ == '__main__':
	main()