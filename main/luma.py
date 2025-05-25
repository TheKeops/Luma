"""
* This application not hack tools. We are not responsible if used!

* This file is there to run and collect other files.

v1.1-demo-dev

"""

import os
import pyfiglet
from colorama import init, Fore
from pathlib import Path
import requests

# Luma Command Files.
from luma_port_scanner import port_scan
from luma_query import ip_query, domain_query
from luma_log import save_log
from luma_pasword_creator import create_password

def main():
    init(autoreset=True)

    figlet_text = pyfiglet.figlet_format("LUMA", font= 'slant')

    commands_text = f"""
-------------------------------
* This program not hack tools!
-------------------------------

0 - Port Scan : Port scaning
1 - Query     : Query ip, dns, domain.
2 - Clear     : Console clear.
3 - About     : This program about.
4 - Exit      : Program shutdown.
5 - Logs      : Open log file.
6 - Password  : Create password or read my password.
7 - Result    : The port scaning and domain query result.
8 - MyIP      : Gives its own external IP address.
"""

    while True:
        print(f"{Fore.CYAN}{figlet_text}")
        print(commands_text)

        user = input("Give a Command : ").lower().strip()

        if user == "0":
                print("")
                ask_port_input = input("(0-MyInputs, 1-All) : ").strip()

                if ask_port_input == "0":
                    try:
                        print("")
                        ip_Adress = input("Ip Adress : ").strip()
                        port_numbers_input = input("Enter Port Numbers : ").strip().split(",")
                        
                        port_numbers = []

                        for prts in port_numbers_input:
                            port_numbers.append(int(prts))

                        port_scan(ip_Adress, port_numbers)
                    except Exception as e:
                        print(f"{Fore.RED}An error has occurred!")
                        save_log("PORT SCANNER",f"{e}",type="error")
                else:
                    try:
                        print("")
                        ip_Adress = input("Ip Adress : ").strip()
                        
                        port_numbers = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 8080]

                        port_scan(ip_Adress, port_numbers)

                    except Exception as e:
                        print(f"{Fore.RED}An error has occurred!")
                        save_log("PORT SCANNER",f"{e}",type="error")

        elif user == "1":
            print("")
            os.system("cls")

            ask_query = input("(1-Domain Query, 2-IP Query, 3-DNS Query) : ").strip()

            if ask_query == "1":
                domain_input = input("Enter a Domain : ").strip()
                domain_query(domain_input)
                input()
                os.system("cls")
            elif ask_query == "2":
                domain_input = input("Enter a Domain (IP) : ").strip()
                ip_query(domain_input)
                input()
                os.system("cls")
            elif ask_query == "3":
                pass
            else:
                print(f"{Fore.RED} No action found! (1,2,3)")
                save_log("QUERY",f"No action found!",type="error")

        elif user == "2":
            os.system("cls")
        elif user == "3":
            os.system("cls")
            print("")
            print(f"{Fore.CYAN}[LUMA ABOUT]")
            print("---------------------------")
            print("- Luma application is an open source simple cybersecurity application. The application currently runs on Windows machines and is under development. This version is for developers and the commands are divided into libraries.")
            print("- v1.1-demo-dev")
            input()
        elif user == "4":
            print("")
            ask = input("Are you sure you want to leave? (Y/N) : ").strip().upper()

            if ask == "Y":
                exit()
        elif user == "5":
            with open("main/log/log.log","r") as f:
                logs = f.readlines()
                print(f"\n      {Fore.CYAN}[LUMA LOGS]\n------------------------------------------------------")
            for i in logs:
                print(f"{i}")
            input()
        elif user == "6":
            print("")
            choose_pas = input("(1-Create Password, 2-Open Password) : ").strip()

            if choose_pas == "1":
                print("")
                password_name = input("Password Name : ").strip()
                create_password(password_name=password_name)
                save_log("CREATE PASSWORD",f"Password created successfully! [main/log/my_password.txt]",type="log")
                print(f"{Fore.GREEN}Password created successfully! [main/log/my_password.txt]")
            else:
                with open("main/log/my_password.txt", "r") as f:
                    password = f.readlines()

                print("")
                print(f"         {Fore.CYAN}[PASSWORD]")
                print("----------------------------")
                for values in password:
                    print(f"- {values}\n")
                input()

        elif user == "7":
            print("")
            ask_result = input("(0-Port Scanner, 1-Domain Query) : ").strip()

            if ask_result == "0":
                os.system("cls")
                with open("main/data/luma_port_scanner_result.txt", "r") as f:
                    file = f.read()

                print(file)
                input()
            else:
                os.system("cls")
                with open("main/data/luma_domain_query_result.txt", "r") as f:
                    file = f.read()

                print(file)
                input()

        elif user == "8":
            you_ip_text = requests.get("https://api64.ipify.org/").text

            print("")
            print(f"You IP Adress : {you_ip_text}")

        else:
            if user == "":
                print(f"{Fore.RED}Do not leave the introduction section blank!")    
                print("")
            else:
                print(f"{Fore.RED}'{user}' not defined!")
                print("")

if __name__ == "__main__":
    main()
