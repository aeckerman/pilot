import os
from colorama import Style

def Pilot(command, verbose):
	if verbose == True:
		print(Style.BRIGHT + "Command execute: " + Style.RESET_ALL + command)
		os.system(command)
	else:
		os.system(command)
