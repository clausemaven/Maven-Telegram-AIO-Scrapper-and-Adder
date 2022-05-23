from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest, GetFullChannelRequest
from telethon import types, utils, errors
from tqdm import tqdm
from datetime import date
from contextlib import suppress
import colorama 
from colorama import init
from colorama import Fore, Back, Style
import time 
import sys
import csv
import traceback
import time
import random
import os
import re
import pickle
import ctypes
import subprocess

def Number():
    import os
    os.system("title † Maven v1.2 †")
    global numb2
    import os
    os.system('cls||clear')
    maven = """
            ███▄ ▄███▓ ▄▄▄    ██▒   █▓▓█████  ███▄    █    
            ▓██▒▀█▀ ██▒▒████▄ ▓██░   █▒▓█   ▀  ██ ▀█   █    
            ▓██    ▓██░▒██  ▀█▄▓██  █▒░▒███   ▓██  ▀█ ██▒   
            ▒██    ▒██ ░██▄▄▄▄██▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒   
            ▒██▒   ░██▒ ▓█   ▓██▒▒▀█░  ░▒████▒▒██░   ▓██░   
            ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒    
            ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ░  ░░ ░░   ░ ▒░   
            ░      ░     ░   ▒     ░░     ░      ░   ░ ░    
                ░         ░  ░   ░     ░  ░         ░    
                                ░                        """
    print (Fore.BLUE + maven)
    time.sleep(1)
    print(Fore.YELLOW + " \nPlease enter your phone number with your country code")
    time.sleep(1)
    
    num1 = input( Fore.GREEN + "Enter your phone number here: ")
    time.sleep(1)
    Question = input("Do you want to enter another phone number? [Yes/No] ")
    if Question == ("Yes"):
        time.sleep(1)
        num2 = input( Fore.GREEN + "Enter your secondary phone number here: ")
        time.sleep(1)
        lines = [num1, num2]
        with open('phone.csv', 'w') as f:
            f.write('\n'.join(lines))
            print(Fore.RED+"Written to file. Go back to the command prompt and press enter")
            time.sleep(1)
            os.system('cls||clear')
            print(Fore.RED + "Exitting...")
            time.sleep(2)
    elif Question == ("No"):
        with open('phone.csv', 'w') as f:
            f.write(num1)
            print(Fore.RED+"Written to file. Go back to the command prompt and press enter")
            time.sleep(2)
            os.system('cls||clear')
            print(Fore.RED + "Exitting...")
            time.sleep(2)
Number()



