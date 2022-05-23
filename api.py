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
def _count_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)

count = len(open('phone.csv').readlines(  ))
if (count<1):
    print(Fore.GREEN+"No Phone numbers in phone.csv, Run Setup from the begining or open an issue on github.")
    time.sleep(1)
    Exit = "Error Occured, Exitting now..."
    for char in Exit:
            sleep(0.1)
            sys.stdout.write(Fore.RED+char)
            sys.stdout.flush()
    exit()
with open('phone.csv') as f:
    num_count = sum(1 for line in open('phone.csv'))
    print(Fore.GREEN+'Total Phone Numbers -', num_count)
numbers = []
def second():
        with open('phone.csv') as f:  
            lines = f.read()
            global first, secondnum
            first = lines.split('\n', 1)[0]
            secondnum = lines.split('\n', 2)[1]
            print("1:",(first))
            print("2:",(secondnum))

with open('phone.csv') as f:
    lines = f.read()
    first = lines.split('\n', 1)[0]
    if num_count>1:
        { second()
            }
    else:
            print("1:",first)
print(Fore.RED+"Opening 'Telegram Core' Pannel")
time.sleep(2)
webbrowser.open('https://my.telegram.org/')
print(Fore.RED+"Enter the Api ID for",Fore.YELLOW+(first))
time.sleep(1)
api1 = input("Api ID: ")
time.sleep(1)
print(Fore.RED+"Enter the Api Hash for",Fore.YELLOW+(first))
time.sleep(1)
hash1 = input("Api Hash: ")
time.sleep(1)
count = len(open('phone.csv').readlines(  ))
if (count>1):
    print(Fore.RED+"Enter the Api ID for",Fore.YELLOW+(secondnum))
    time.sleep(1)
    api2 = input("Api ID: ")
    time.sleep(1)
    print(Fore.RED+"Enter the Api Hash for",Fore.YELLOW+(secondnum))
    time.sleep(1)
    hash2 = input("Api Hash: ")
    time.sleep(1)

    with open('api.csv', "w") as file:
        file.write(str(api1)+","+(hash1)+"\n"+(api2)+","+(hash2))
        print(Fore.GREEN+"Api information sucessfully written to file!")
        time.sleep(1)
        os.system('cls||clear')
        Exit = "Exitting..."
        for char in Exit:
            sleep(0.1)
            sys.stdout.write(Fore.GREEN+char)
            sys.stdout.flush()
        exit()

with open('api.csv', "w") as file:
        file.write(str(api1)+","+(hash1))
        print(Fore.GREEN+"Api information sucessfully written to file!")
        time.sleep(1)
        os.system('cls||clear')
        Exit = "Exitting..."
        for char in Exit:
            sleep(0.1)
            sys.stdout.write(Fore.GREEN+char)
            sys.stdout.flush()
        exit()