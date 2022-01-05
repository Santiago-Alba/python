#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
	try:
		saludo=int(input("Coloque su numero: "))
		if saludo % 2 == 0:
			print("PAR")
		elif saludo % 2 != 0:
			print("IMPAR")
		break
	except:
		print("Ingrese solo numeros")


































def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
