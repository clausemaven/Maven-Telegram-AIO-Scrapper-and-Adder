from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest, GetFullChannelRequest
from telethon import types, utils, errors
from tqdm import tqdm
from datetime import date
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
from tqdm import tqdm
from time import sleep

os.system("title † Maven v1.2 †")
for i in tqdm(range(int(9291)), desc= Fore.RED +"Checking Rate Limits.."):
   pass 
print (Fore.YELLOW + "None!")
time.sleep(2)
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
print(Fore.BLUE + maven)
today = date.today()
print(Fore.YELLOW + "Welcome To Maven v1.2. It is:", today)
with open('phone.csv') as f:
    num_count = sum(1 for line in open('phone.csv'))
    print(Fore.GREEN+'Total Phone Numbers -', num_count)
numbers = []
def second():
        with open('phone.csv') as f:  
            lines = f.read()
            first = lines.split('\n', 1)[0]
            second = lines.split('\n', 2)[1]
            print("1:",(first))
            print("2:",(second))

with open('phone.csv') as f:
    lines = f.read()
    first = lines.split('\n', 1)[0]
    if num_count>1:
        { second()
            }
    else:
            print("1:",first)

ve = int(input("Choose an account to continue: "))
with open('phone.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    list_of_rows = list(csv_reader)   
    row_number = ve
    col_number = 1
    value = list_of_rows[row_number - 1][col_number - 1]
    
with open('api.csv', 'r') as api_obj_id:
    csv_reader = csv.reader(api_obj_id)
    list_of_rows = list(csv_reader)    
    row_number = ve
    col_number = 1
    deltaop = list_of_rows[row_number - 1][col_number - 1]
    
with open('api.csv', 'r') as hash_obj:
    csv_reader = csv.reader(hash_obj)
    list_of_rows = list(csv_reader)
    row_number = ve
    col_number = 2
    deltaxd = list_of_rows[row_number - 1][col_number - 1]
os.system('cls||clear')   
api_id = int(deltaop)
api_hash = str(deltaxd)
pphone = value
phone = utils.parse_phone(pphone)
PhoneProm = (f"Selected Phone Number: +{phone} \n")
ApiProm = (f"Selected API ID: {api_id} \n")
for char in PhoneProm:
    sleep(0.010)
    sys.stdout.write(Fore.YELLOW+char)
    sys.stdout.flush()
time.sleep(1)
for char in ApiProm:
    sleep(0.010)
    sys.stdout.write(Fore.RED+char)
    sys.stdout.flush()
time.sleep(1)

client = TelegramClient(f"./sessions/{phone}", api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

def add_users_to_group():
    global ve
    input_file = f'data/data{ve}.csv'
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f,delimiter=",",lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['srno'] = row[0]
            user['username'] = row[1]
            try:
                user['id'] = int(row[2])
                user['access_hash'] = int(row[3])
                user['name'] = row[4]
            except IndexError:
                print ('users without id or access_hash')
            users.append(user)
    #random.shuffle(users)
    chats = []
    last_date = None
    chunk_size = 10
    groups=[]

    result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash = 0
            ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup== True: # CONDITION TO ONLY LIST MEGA GROUPS.
                groups.append(chat)
            else: 
             if chat.megagroup == False:
                 Exception("Not a megagroup")
                
        except:
            continue

    print(Fore.YELLOW+'Choose a guild to add members:')
    print(Fore.LIGHTCYAN_EX)
    i=0
    for group in groups:
        print(str(i)+Fore.LIGHTCYAN_EX+ ':' + group.title)
        i+=1

    g_index = input(Fore.BLUE+"Enter the corresponding number: ")
    target_group=groups[int(g_index)]
    print(Fore.BLUE+'\n\nGroup Selected:\t' + groups[int(g_index)].title)

    target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)

    mode = int(input("Enter 1 to add by username or 2 to add by ID: "))
    startfrom = int(input("Start From = "))
    endto = int(input("End To = "))
    delta_xd = False
    error_count = 0
    deltacount= (endto-startfrom)
    os.system('cls||clear')

    for user in users:
        global status
        
        status = 'do'
        countt = 6
        if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):

            try:
     
                if mode == 1:
                    if user['username'] == "":
                        print('no username, moving to next')
                        continue
                    user_to_add = client.get_input_entity(user['username'])
                elif mode == 2:
                    user_to_add = InputPeerUser(user['id'], user['access_hash'])
                else:
                    sys.exit("Invalid Mode Selected. Please Try Again.")
                client(InviteToChannelRequest(target_group_entity,[user_to_add]))
                #print("Waiting 60 Seconds...")
                status = (Fore.GREEN+'Sucessfully added'+Style.RESET_ALL)
                time.sleep(60)
            except PeerFloodError:
                status = 'PeerFloodError'
                print(Fore.RED+'Account is rate limited, stopping now for 24 hours')
                time.sleep(86400)
                #print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
            except UserPrivacyRestrictedError:
                status = (Fore.RED+'PrivacyError'+Style.RESET_ALL)
            except errors.RPCError as e:
                status = e.__class__.__name__
        
    
            except Exception as d:
            	status = d
            except:
                traceback.print_exc()
                print(Fore.RED+"Unexpected Error")
                error_count += 1
                if error_count > 10:
                    sys.exit('too many errors')
                continue
            channel_full_info = client(GetFullChannelRequest(channel=target_group_entity))
                
            countt = int(channel_full_info.full_chat.participants_count)
            os.system('cls||clear')
            print(Fore.LIGHTMAGENTA_EX)
            print(f"Attempting to add {user['name']} To {target_group.title} Total amount of members added: {countt}/{deltacount}- {status}")
        elif int(user['srno']) > int(endto):
            #print("Members Added Successfully!")
            delta_xd = True
    print("Done!" if delta_xd else "Error!")       

def list_users_in_group():
    global ve
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]
    
    result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash = 0
            ))
    chats.extend(result.chats)
    
    for chat in chats:
        try:
            if chat.megagroup== True:
                groups.append(chat)
            # if chat.megagroup== True:
        except:
            continue
    
    print(Fore.YELLOW+'Choose a group to scrape members from:')
    i=0
    for g in groups:
        print(str(i) + '- ' + g.title)
        i+=1
    
    g_index = input(Fore.RED+"Enter a Number: ")
    target_group=groups[int(g_index)]
    import os
    os.system('cls||clear')
    print(Fore.RED+'Scraping In Progress')
    print(Fore.BLUE+'Group Selected:\t' + groups[int(g_index)].title)
    
    print('Fetching Members...')
    all_participants = []
    all_participants = client.get_participants(target_group)
    
    print('Saving In file...')
    
    with open(f"data/data{ve}.csv","w",encoding='UTF-8') as f:
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        writer.writerow(['sr. no.','username','user id', 'access hash','name','group', 'group id', 'status'])
        i = 0
        for user in all_participants:
            i += 1
            if user.username:
                username= user.username
            else:
                username= ""
            if user.first_name:
                first_name= user.first_name
            else:
                first_name= ""
            if user.last_name:
                last_name= user.last_name
            else:
                last_name= ""
            name= (first_name + ' ' + last_name).strip()
            if isinstance(user.status, types.UserStatusOnline):
                status = 1
        
            elif isinstance(user.status, types.UserStatusOffline):
                if time.time()-(user.status.was_online).timestamp() <=86400:
                    status = 2
                else:
                    status = 31634268763763
            writer.writerow([i,username,user.id,user.access_hash,name,target_group.title, target_group.id, status])      
    print('Members scraped successfully.')
    

def printCSV():
    global ve
    


    lines = list()


    def main():
        lines = list()
        with open(f'data/data{ve}.csv', 'r',encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == '31634268763763':
                        lines.remove(row)
        with open('11.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)

    def main1():
        lines = list()
        with open('11.csv', 'r',encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == 'username':
                        lines.remove(row)
        
        with open('22.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)

    main()
    main1()


    with open("22.csv","r",encoding='UTF-8') as source:
        rdr = csv.reader(source)

        with open(f"data/data{ve}.csv","w",encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['sr. no.','username','user id', 'access hash','name','group', 'group id', 'status'])
            i = 0
            for row in rdr:
                i += 1
                writer.writerow((i,row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                
                
    os.remove("11.csv")
    os.remove("22.csv")
    #os.remove("unf.csv")
    print(f"Successfully Filtered And Saved In data{ve}.csv")
    
    

# print('Fetching Members...')
# all_participants = []
# all_participants = client.get_participants(target_group, aggressive=True)
def autos():
    print(Fore.GREEN+'What do you want to do? Below are a list of functions')
    print((Fore.RED+"1:Scrape and get user list from a group\n2:Add users from existing CSV to Group\n3:Scrape and create a new CSV and the add users to a group"))
    print((Fore.YELLOW+"4:Filter users by Last Seen\n5-Scrape and filter\n6-Filter user CSV data and add them to a Group\n7-Scrape Members, filter users, And add to Group\n"))
    mode = int(input(Fore.BLUE+"Enter your option with the corresponding number: ")) 
    os.system('cls||clear')


    if mode == 1:
        list_users_in_group()
    elif mode == 2:
        add_users_to_group()
    elif mode == 3:
        printCSV()
    elif mode == 4:
        list_users_in_group()
        add_users_to_group()
    elif mode == 5:
        list_users_in_group()
        printCSV()
    elif mode == 6:
        printCSV()
        add_users_to_group()
    elif mode == 7:
        list_users_in_group()
        printCSV()
        add_users_to_group()
autos()
import os
os.system('cls||clear')
stat = input('Done!\nChoose From Below:\nPress 1 to Repeat The Script\nOr press enter to quit: ')
if stat == '1':
    os.system('cls||clear')
    autos()

else:
    quit()
    
