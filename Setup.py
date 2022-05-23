
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest, GetFullChannelRequest
from telethon import types, utils, errors
from tqdm import tqdm
from datetime import date
from contextlib import suppress
import sys
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
import colorama 
import time 
import sys
import csv
import traceback
import time
import random
import os
import re
import pickle
import webbrowser
import json
import subprocess
from os import system
import os
os.system("title † Maven v1.2 †")
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
phone = "Running Phone.py...Step 1/3 \n"
for char in phone:
    sleep(0.025)
    sys.stdout.write(Fore.MAGENTA+char)
    sys.stdout.flush()
    sleep(0.025)
print(Fore.LIGHTCYAN_EX + "Press Enter after entering your phone number to continue...")
subprocess.call('start /wait python phone.py', shell=True)
input()
api = "Running Api.py...Step 2/3 \n"
for char in api:
    sleep(0.025)
    sys.stdout.write(Fore.MAGENTA+char)
    sys.stdout.flush()
sleep(0.025)
print(Fore.LIGHTCYAN_EX + "Press Enter after entering your Api ID and Api Hash to continue...")
subprocess.call('start /wait python api.py', shell=True)
input()
maven = "Running Maven.py...Step 3/3 \n"
for char in maven:
    sleep(0.025)
    sys.stdout.write(Fore.MAGENTA+char)
    sys.stdout.flush()
sleep(1)
bye = "This command prompt will close shortly, have fun using Maven! :)\n"
for char in bye:
    sleep(0.025)
    sys.stdout.write(Fore.YELLOW+char)
    sys.stdout.flush()
subprocess.call('start /wait python maven.py', shell=True)
time.sleep(0.5)


