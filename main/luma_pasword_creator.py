import random
import string
from colorama import init, Fore

init(autoreset=True)

def create_password(password_name,long=20):
    uzunluk = long
    karakterler = string.ascii_letters + string.digits + "!@#$()"

    rastgele_string = ''.join(random.choices(karakterler, k=uzunluk))

    if str(password_name).strip() == "":
        print(f"{Fore.RED}Do not leave the introduction section blank!")
    else:
    
        with open("main/log/my_password.txt","a") as f:
            f.writelines(f"{password_name.strip().upper()} : {rastgele_string}\n")

