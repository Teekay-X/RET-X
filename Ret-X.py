import socket
import os
import time

def fetch():
  os.system("clear")
  logo()
  url = input("\u001b[33mENTER WEBSITE(e.g: google):")

  full_url = f"www.{url}.com"

  try:
    ip_addr = socket.gethostbyname(full_url)

    print("\nFecthing IP...\n")
    time.sleep(2)
    print(f"{url}'s IP: {ip_addr} \n")

  except Exception as err:
    print(err)
    time.sleep(2)
    logo()
    menu()


def more():
  os.system("termux-open https://github.com/Teekay-X")
  logo()
  menu()

def logo():
  os.system("clear")
  logo= """ \u001b[31m
   ____    _____   _____          __  __
  |  _ \  | ____| |_   _|         \ \/ /
  | |_) | |  _|     | |    _____   \  /
  |  _ <  | |___    | |   |_____|  /  \
      |_| \_\ |_____|   |_|           /_/\_\
"""
  print(logo)



def about():
 ab = """
 \033[41m\033[35mAuthor   : Asahluma Mabhongo [ Teekay-X ] \033[0m
 \033[41m\033[35mGithub   : https://github.com/Teekay-X \033[0m
 \033[41m\033[35mFacebook : https://facebook.com/tee.kay16 \033[0m
 \033[41m\033[35mVersion  : 0.1 \033[0m                     

  \033[41m \033[35m [00] Main Menu     [99] Exit \033[0m
"""
 print (ab)
 answ = input("\033[40m \033[32m[-] Choose:>> \033[0m")

 if answ == "00":
    logo()
    menu()
 elif answ == "99":
      exiti()
 else:
    print ("\033[31m[\033[32m!\033[31m]\033[32m INVALID OPTION!! \033[0m")
    quit()

def exiti():
 logo()
 ex = """
 \033[31m=========================================

 \033[41m \033[36mThanks For Using This Tool Have a  good day :)\033[0m 
  """
 print (ex)
 quit()


def menu():
  menu = """ \u001b[38m
  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀MENU▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
  [1]FETCH IP        [2] MORE

  [3] ABOUT          [4] EXIT
  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀SELECT▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""
  print (menu)
  ans = input("\u001b[35mChoose[=>]:")
  if ans == "1":
    fetch()
  elif ans == "2":
     more()
  elif ans == "3":
     about()
  elif ans == "4":
      exiti()
  else:
    print("\u001b[32m[\u001b[31m!\u001b[32m]\u001b[31m INVALID OPTION!")
    time.sleep(2)
    logo()
    menu()
logo()
menu()
