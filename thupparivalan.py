import socket
import os
import requests
import platform
import webbrowser
import tempfile
import time
from urllib.parse import urlparse

import animate
import scans

def text_to_plus_separated(text):
    words = text.split()
    plus_separated_text = '+'.join(words)
    return plus_separated_text

def extract_keyword(url):
    parsed_url = urlparse(url)
    netloc = parsed_url.netloc if parsed_url.netloc else parsed_url.path
    keyword = netloc.replace("www.", "").split('.')[0]
    return keyword

def save_output_to_file(output, suggested_filename="output.txt"):
    print("\nDo you want to save/download the output to a file?")
    choice = input("Enter 'y' to save, any other key to skip: ").strip().lower()
    if choice == 'y':
        filename = input(f"Enter filename (default: {suggested_filename}): ").strip()
        if not filename:
            filename = suggested_filename
        with open(filename, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"\033[92mOutput saved as '{filename}'.\033[0m\n")

def generate_google_dorks(url_or_ip):
    keyword = extract_keyword(url_or_ip)
    queries = [
        f'intitle:{keyword}',
        f'filetype:pdf {keyword}',
        f'site:{url_or_ip}',
        f'cache:{url_or_ip}',
        f'allinurl:{keyword}',
        f'inurl:{keyword}',
        f'allintitle:{keyword}',
        f'inanchor:{keyword}',
        f'allinanchor:{keyword}',
        f'link:{url_or_ip}',
        f'related:{url_or_ip}',
        f'info:{url_or_ip}',
        f'location:{keyword}'
    ]
    output = ""
    for query in queries:
        print("\033[95m"+query)
        output += query + "\n"
    save_output_to_file(output, suggested_filename="google_dorks.txt")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""\033[96m
 1)  Google Dork Help (ls Cmds)                 12) List Hidden Directories
 2)  YouTube Meta Data Extractor (Redirect)     13) Host Info
 3)  Passive Reconn (Website/IP)                14) Host Discovery
 4)  Social Info                                15) Ports, Services, OS & Agressive Scans
 5)  Website Footprinting                       16) Scan Beyond IDS/Firewalls
 6)  Gather Wordlist                            17) Perform DOS on Target
 7)  Whois Lookup (Redirect)                    18) NetBIOS & SNMP Enumeration
 8)  DNS Info                                   19) LDAP & NFS Enumeration                    
 9)  Reverse DNS Lookup (Redirect)              20) DNS & SMTP Enumeration
 10) Try Zone Transfer & Zone Walking           21) RPC, SMB, and FTP Enumeration 
 11) Subdomains Enum                            22) Exit
                   ( More Functions will be added soon...)                              
 """)
    print()
    
def main():
    animate.bill()
    try:
        what = input('\033[96m Wanna Info about a domain or an IP ? [D/IP]: ')
        if what[0].upper() == 'D':
            victim = input(' Enter the website address: ')
        elif what[0].upper() == 'I':
            victim = input(' Enter the IP address (or domain to let system fetch the IP address of the domain): ')
            victim = socket.gethostbyname(victim)
        else:
            print('?')
            main()
 
        while True:
            clear()
            animate.bill()
            banner()
            choose = input('\033[91mSelect the Type of Footprinting/Reconnaissance/Enumeration (1-21): ')
            
            if choose == '1':
                print("\033[91mGenerating Google Dork Commands...\n[Copy & Paste it in Google] ")
                time.sleep(1.5)
                generate_google_dorks(victim)
            
            # You can similarly add save_output_to_file for other output sections.
            # For commands that use os.system, consider using subprocess to capture output and pass it to save_output_to_file.
            
            elif choose == '2':
                print("\033[91mOpening Browser...in 2 secs...\n")
                time.sleep(2)
                url = "https://mattw.io/youtube-metadata/"
                webbrowser.open(url)
            
            # ... rest of your menu options ...

            elif choose == '22':
                print('\033[91mThank You So Much For Using Thupparivalan!\n @rahulthewhitehat :) ')
                exit()
                
            else:
                print('?')
                
            input("Press Enter to continue...")

    except socket.gaierror:
        print('Name or service not known!\033[93m')
        main()
    except UnboundLocalError:
        print('The information you entered is incorrect')
        main()
    except requests.exceptions.ConnectionError:
        print('You are Offline')
        exit()
    except IndexError:
        print('?')
        main()

if __name__ == '__main__':
    main()
