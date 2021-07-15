import sys


import settings


arguments = sys.argv

def start():
	if arguments[-2] == settings.LOGIN and arguments[-1] == settings.PASSWORD:
		print("OK")
	else:
		print("Wrong password or login")	