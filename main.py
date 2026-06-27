# main.py - thecho0sen one on github
import os
import time
import sys

print("=== SIMPLE SELF OFFLINE TOOL ===")

cioata = False
ip = input("\nEnter target IPv4 adress:\n")

print("Are you sure you want to boot offline " + ip + "\n y/n")
mega = input()

if mega.lower() == 'y':
    print("get booted offline you skid")
    time.sleep(2)
    os.system("ipconfig /release")
elif mega.lower() == 'n':
    print("Well done you get one scooby snack")
    sys.exit(0)

input("\nPress Enter to exit...")
