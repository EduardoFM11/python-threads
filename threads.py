from threading import Thread
from time import sleep

lista_entradas = list()

def obtener_ciclo():
	while True:
		try:
			entrada = input("Ingresa una letra")
			lista_entradas.clear()
			lista_entradas.append(entrada)
		except:
			print("ERROR")

def marquesina(entrada):
	while True:
		print(entrada)
		sleep(1)

def main():
	thread_ciclo = Thread(target = obtener_ciclo)
	thread_marquesina = Thread(target = marquesina, args=(lista_entradas,))
	thread_ciclo.start()
	thread_marquesina.start()
	thread_marquesina.join()
	thread_ciclo.join()

if __name__=="__main__":
    main()