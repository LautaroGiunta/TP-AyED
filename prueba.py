import sys
import getpass
'''user_1 = "estudiante1@ayed.com"
psw_1 = "111222"
user_2 = "estudiante2@ayed.com"
psw_2 = "333444"
user_3 = "estudiante3@ayed.com"
psw_3 = "555666"
'''

user_1 = str("1")
psw_1 = str("11")
user_2 = str("2")
psw_2 = str("22")
user_3 = str("3")
psw_3 = str("33")

def menu(user, psw):
	print("hola ", user)



















print("Log IN")
for bandera in range(0,3):  #
	user = input("Ingrese el usuario: ")
	psw = getpass.getpass("Ingrese el contraseña: ")
	for i in psw:
	       print ('*', end='')
	print("\n")
	if user == user_1 and psw == psw_1:
		print("1")
		menu(user, psw)
	elif user == user_2 and psw == psw_2:
		print("2")
	elif user == user_3 and psw == psw_3:
		print("3")
	elif bandera == 2:
		print("Excediste los intentos")
		sys.exit(0)
	else:
		print("Intente denuevo")
		