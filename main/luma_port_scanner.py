import socket
from colorama import init, Fore
import datetime

from luma_log import save_log

init(autoreset=True)

def port_scan(ip, TargetPort):
    write_title_port = """
   {}[PORT SCANNER]
---------------------
""".format(Fore.CYAN)
    print(write_title_port)
    try:
        port_f = open("main/data/luma_port_scanner_result.txt","a")
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
