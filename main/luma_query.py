import socket
from colorama import init, Fore
import whois
import datetime
import dns.resolver

from luma_log import save_log

init(autoreset=True)

def domain_query(domain):
    try:
        domain_query_f = open("main/data/luma_domain_query_result.txt", "a")

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

        save_log("DOMAİN QUERY",f"{domain} Domain Query.",type="log")
    except Exception as e:
        print(f"{Fore.RED}Query failed :", e)
        save_log("DOMAİN QUERY",f"Query failed : {e}",type="error")

def ip_query(target_domain):
    try:
        ip = socket.gethostbyname(target_domain)

        print(f"| {target_domain} IP of address : {ip}")
        save_log("IP QUERY",f"{target_domain} IP of address : {ip}",type="log")

    except Exception as e:
        save_log("IP QUERY",f"{e}",type="error")

def dns_query():
    pass

