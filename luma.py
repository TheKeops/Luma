"""
*  This app is not a hack tool! We are not responsible if used!

* This app is under development. Please report any bugs or suggestions!

Version : v1.1-demo
License : MIT License
Author : TheKeops

"""

import os
import pyfiglet
from colorama import init, Fore
import requests
import pyperclip
import datetime
import random
import string
import socket
import dns.resolver
import whois

try:
    os.makedirs("LUMA-APP/data", exist_ok=True)
    os.makedirs("LUMA-APP/log", exist_ok=True)
    open("LUMA-APP/data/domain_query_result.txt", "x", encoding="utf-8")
    open("LUMA-APP/data/my_password.txt", "x", encoding="utf-8")
    open("LUMA-APP/data/dns_query_result.txt", "x", encoding="utf-8")
    open("LUMA-APP/data/port_scanner_result.txt", "x", encoding="utf-8")

    open("LUMA-APP/log/log.log", "x", encoding="utf-8")
except:
    pass

def save_log(title=None, content=None, type=None):

    if type.strip().upper() == "LOG":
        with open("LUMA-APP/log/log.log", "a", encoding="utf-8") as f:
            f.writelines(f"- LUMA INFO [{datetime.datetime.now().strftime('%H:%M:%S')}] : TITLE : {title} - COMMENT : {content}\n")

    elif type.strip().upper() == "WARNING":
        with open("LUMA-APP/log/log.log", "a", encoding="utf-8") as f:
            f.writelines(f"- LUMA WARNING [{datetime.datetime.now().strftime('%H:%M:%S')}] : TITLE : {title} - COMMENT : {content}\n")

    elif type.strip().upper() == "ERROR":
        with open("LUMA-APP/log/log.log", "a", encoding="utf-8") as f:
            f.writelines(f"- LUMA ERROR [{datetime.datetime.now().strftime('%H:%M:%S')}] : TITLE : {title} - COMMENT : {content}\n")

def create_password(password_name,long=20):
    uzunluk = long
    karakterler = string.ascii_letters + string.digits + "!.-_"

    rastgele_string = ''.join(random.choices(karakterler, k=uzunluk))

    if str(password_name).strip() == "":
        print(f"{Fore.RED}Do not leave the introduction section blank!")
    else:
    
        with open("LUMA-APP/data/my_password.txt","a") as f:
            f.writelines(f"{password_name.strip().upper()} : {rastgele_string}\n")

def port_scan(ip, TargetPort):
    write_title_port = """
   {}[PORT SCANNER]
---------------------
""".format(Fore.CYAN)
    print(write_title_port)
    try:
        port_f = open("LUMA-APP/data/port_scanner_result.txt","a")
        port_f.writelines(f"PORT SCANING [{datetime.datetime.now()}] - IP : {ip} - PORT : {TargetPort}\n")

        for port in TargetPort:
            try:
                soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                soc.settimeout(0.5)
                result = soc.connect_ex((ip, port))

                if result == 0:
                    print(f"| Port {port} Open.")
                    port_f.writelines(f"| Port {port} Open.\n")
                else:
                    print(f"| Port {port} Close.")

                soc.close()
            except KeyboardInterrupt:
                print(f"{Fore.RED}Scanning process cancelled!")
                save_log("PORT SCANNER",f"Scanning process cancelled!",type="error")
            except socket.error:
                print(f"{Fore.RED}Connection failed!")
                save_log("PORT SCANNER",f"Connection failed!",type="error")
                break
        print(f"{Fore.GREEN}Scanning successful!")
        port_f.writelines("--------------------------------------------------------------------------------\n\n")
        save_log("PORT SCANNER",f"Scanning successful! {TargetPort}",type="log")

    except Exception as e:
        print(f"{Fore.RED}An error has occurred! {e}")
        save_log("PORT SCANNER",f"{e}",type="error")

def domain_query(domain):
    try:
        domain_query_f = open("LUMA-APP/data/domain_query_result.txt", "a")

        w = whois.whois(domain)

        print("")
        print(f"         {Fore.CYAN}[RESULT]")
        print("--------------------------")
        print(f"Domain            : {w.domain_name}")
        print(f"Registrant        : {w.registrar}")
        print(f"Registration Date : {w.creation_date}")
        print(f"End Date          : {w.expiration_date}")
        print(f"Name Servers      : {w.name_servers}")
        print(f"Mail              : {w.emails}")

        domain_query_writer =f"""
Domain            : {w.domain_name}
Registrant        : {w.registrar}
Registration Date : {w.creation_date}
End Date          : {w.expiration_date}
Name Servers      : {w.name_servers}
Mail              : {w.emails}
-------------------------------------------------------

"""

        domain_query_f.writelines(f"DOMAIN QUERY RESULT [{datetime.datetime.now()}] - DOMAIN : {domain}")
        domain_query_f.writelines(f"{domain_query_writer}")

        save_log("DOMAIN QUERY",f"{domain} Domain Query.",type="log")
    except Exception as e:
        print(f"{Fore.RED}Query failed :", e)
        save_log("DOMAIN QUERY",f"Query failed : {e}",type="error")

def ip_query(target_domain):
    try:
        ip = socket.gethostbyname(target_domain)

        print(f"| {target_domain} IP of address : {ip}")
        save_log("IP QUERY",f"{target_domain} IP of address : {ip}",type="log")

    except Exception as e:
        save_log("IP QUERY",f"{e}",type="error")

def dns_query():
    def dns_query_function(domain):
        save_log("DNS QUERY",f"A DNS query was made. DOMAIN : {domain}",type="log")

        dns_result_writer = open("LUMA-APP/data/dns_query_result.txt", "a", encoding="utf-8")

        dns_result_writer.writelines(f"DNS QUERY [{datetime.datetime.now()}] - DOMAIN : {domain}\n\n")
        kayit_turleri = ['A', 'AAAA', 'MX', 'NS', 'CNAME', 'TXT']
        print(f"{domain} DNS query started for...\n")

        for kayit in kayit_turleri:
            try:
                cevap = dns.resolver.resolve(domain, kayit)
                print(f"{kayit} Records:")
                dns_result_writer.writelines(f"{kayit} Records:\n")
                for rdata in cevap:
                    print(f" | {rdata.to_text()}")
                    dns_result_writer.writelines(f" | {rdata.to_text()}\n")
                    
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                print(f"{Fore.RED}{kayit} No record found.")
                dns_result_writer.writelines(f"{kayit} No record found.\n")
                 
            except Exception as e:
                print(f"Error occurred: {e}")
                save_log("DNS QUERY",f"Error occurred: {e}",type="error")
            print()
        dns_result_writer.writelines(f"-----------------------------------------------\n")

        input()

    print("")
    alan_adi = input("Please enter a domain name : ").strip().lower()
    if alan_adi:
        dns_query_function(alan_adi)
    else:
        print("A valid domain name was not entered.")
        save_log("DNS QUERY",f"A valid domain name was not entered.",type="error")

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
                dns_query()
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
            print("- Luma application is an open source simple cybersecurity application. The application currently runs on Windows machines and is under development. This version is a terminal version, versions with interfaces may be released in future versions.")
            print("VERSION   : v1.1-demo")
            print("LICENSE   : MIT LICENSE")
            print("DEVELOPER : TheKeops")
            input()
        elif user == "4":
            print("")
            ask = input("Are you sure you want to leave? (Y/N) : ").strip().upper()

            if ask == "Y":
                exit()
        elif user == "5":
            with open("LUMA-APP/log/log.log","r") as f:
                logs = f.readlines()
                print(f"\n      {Fore.CYAN}[LUMA LOGS]\n------------------------------------------------------")
            for i in logs:
                print(f"{i}")
            input()
        elif user == "6":
            print("")
            choose_pas = input("(0-Create Password, 1-Open Password) : ").strip()

            if choose_pas == "0":
                print("")
                password_name = input("Password Name : ").strip()
                create_password(password_name=password_name)
                save_log("CREATE PASSWORD",f"Password created successfully! [main/log/my_password.txt]",type="log")
                print(f"{Fore.GREEN}Password created successfully! [LUMA-APP/data/my_password.txt]")
            else:
                with open("LUMA-APP/data/my_password.txt", "r") as f:
                    password = f.readlines()

                print("")
                print(f"         {Fore.CYAN}[PASSWORD]")
                print("----------------------------")
                for values in password:
                    print(f"- {values}\n")
                input()

        elif user == "7":
            print("")
            ask_result = input("(0-Port Scanner, 1-Domain Query, 2-DNS Query) : ").strip()

            if ask_result == "0":
                os.system("cls")
                with open("LUMA-APP/data/port_scanner_result.txt", "r") as f:
                    file = f.read()

                print(file)
                input()
            elif ask_result == "1":
                os.system("cls")
                with open("LUMA-APP/data/domain_query_result.txt", "r") as f:
                    file = f.read()
                print(file)
                input()
            elif ask_result == "2":
                os.system("cls")
                with open("LUMA-APP/data/dns_query_result.txt", "r", encoding="utf-8") as f:
                    file = f.read()
                print(file)
                input()
            else:
                print(f"{Fore.RED}Please enter the given operations!")
                input()

        elif user == "8":
            you_ip_text = requests.get("https://api64.ipify.org/").text

            print("")
            print(f"You IP Adress : {you_ip_text} (Copied)")
            pyperclip.copy(you_ip_text)

        else:
            if user == "":
                print(f"{Fore.RED}Do not leave the introduction section blank!")    
                print("")
            else:
                print(f"{Fore.RED}'{user}' not defined!")
                print("")
# Main 
if __name__ == "__main__":
    main()
    