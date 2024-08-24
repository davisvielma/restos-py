import config

def main() -> None:
	print('Mensaje con formato predeterminado')
	print(config.RED + 'Mensaje con letra roja')
	print(config.WHITE + 'Mensaje con letra blanca')
	print(config.RED + 'Mensaje con letra roja antes del reseteo' + config.RESET)
	print('Mensaje luego del reseteo')

if __name__ == '__main__':
	main()