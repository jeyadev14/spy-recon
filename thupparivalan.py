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

    for query in queries:
        print("\033[95m"+query)

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
 
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
    #clear()
    animate.bill()
    try:
        what = input('\033[96m Wanna Info about a domain or an IP ? [D/IP]: ')
        if what[0].upper() == 'D':
            victim = input(' Enter the website address: ')
        elif what[0].upper() == 'I':
            victim = input(' Enter the IP address (or domain to let system fetch the IP address of the domain): ')
            victim = socket.gethostbyname(victim)
            #print(f' The IP address of target is {victim}')
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
            
            elif choose == '2':
                print("\033[91mOpening Browser...in 2 secs...\n")
                time.sleep(2)
                url = "https://mattw.io/youtube-metadata/"
                webbrowser.open(url)
                
            elif choose == '3':
                url = ["https://search.censys.io/?q="+victim, "https://sitereport.netcraft.com/?url="+victim, "https://www.shodan.io/search?query="+extract_keyword(victim)]
                print('\033[91mTaking you to Censys, Netcraft & Shodan...2secs...\n')
                time.sleep(2) 
                webbrowser.open(url[0])
                time.sleep(1)
                webbrowser.open(url[1]) 
                time.sleep(1)
                webbrowser.open(url[2])    
                time.sleep(1)
                
            elif choose == '4':
                name = input("Enter the name that has be to found on social media >> ")
                os.system("cd modules && bash userrecon.sh")
                print("\033[91mInitiating Social Searcher in 5 secs...\n")
                time.sleep(5)
                webbrowser.open("https://www.social-searcher.com/google-social-search/?q="+text_to_plus_separated(name))
                
            elif choose == '5':
                print('\033[91mPinging Target...\n')
                os.system("sudo ping "+victim)           
                print('\033[91mTracerouting...\n')
                time.sleep(2)
                os.system("sudo traceroute "+victim)
                print('\033[91mLaunching Browser...\n')      
                time.sleep(5)    
                webbrowser.open("https://website.informer.com/" + victim)
                webbrowser.open("https://centralops.com/co")
                
            elif choose == '6':
                depth = input("Enter Depth Level: ")
                word_len = input("Min Number of Word Length: ")
                os.system("cewl https://www."+victim+" -d " + depth + " -m " + word_len)
             
            elif choose == '7':
                print('\033[91mTriggering Whois Website...\n')
                time.sleep(2)
                webbrowser.open("https://www.whois.com/whois/"+victim)
                                          
            elif choose == '8':
                print("Using DIG...\n\n")
                print("Name Server Info: \n")
                os.system(f"dig {victim} ns")
                time.sleep(2)
                print("Mail Server Info: \n")
                os.system(f"dig {victim} mx")
                print("DNS Info Fetched\n")
                print('\033[91mRedirecting to DNS Enum Sites...\n')
                time.sleep(3)
                webbrowser.open("https://dnschecker.org/all-dns-records-of-domain.php?query="+victim+"&rtype=ALL&dns=google")
                webbrowser.open("https://www.nslookup.io/domains/"+victim+"/dns-records/")
                
            elif choose == '9':
                print("\033[91mOpening You Get Signal...\n")
                time.sleep(2)
                webbrowser.open("https://www.yougetsignal.com/tools/web-sites-on-web-server/")
            
            elif choose == '10':
                print('\033[91mUsing DNS Recon Tool...\n')
                os.system(f'cd modules/dnsrecon && python dnsrecon.py -d {victim} -t axfr')    
                os.system(f'cd modules/dnsrecon && python dnsrecon.py -d {victim} -t zonewalk')
                
            elif choose == '11':
                print('\033[91mUsing GoBuster Tool...\n')
                os.system(f'gobuster dns -d {victim} -w /home/user/Thupparivalan\ 1.0/modules/dnsrecon/subdomains-top1mil-20000.txt')
            
            elif choose == '12':
                print('\033[91mUsing GoBuster Tool...\n')
                os.system(f'gobuster dir -u {victim} -w /home/user/Thupparivalan\ 1.0/modules/dnsrecon/directory-list-2.3-medium.txt')
  
            elif choose == '13':
                print('\033[91mUsing HostInfo Tool...\n')
                os.system('ruby ./modules/hostinfo/hostinfo.rb -b '+victim)
                
            elif choose == '14':
                while True:
                    scan_type = input("Enter the Type of Scan: ['TCP_SYN', 'ACK', 'UDP', 'ARP', 'ECHO', 'TS', 'ICMP_MASK', 'PROTOCAL_PING'], or EXIT? : ")
                    if(scan_type.upper() == 'EXIT'):
                        break;
                    scans.perform_nmap_scan1(scan_type.upper(), victim)                
            
            elif choose == '15':
                while True:
                    scan_type = input("Enter the Type of Scan: ['TCP_CONNECT','SYN','ACK','UDP','SERVICE', 'OS','AGGRESSIVE','XMAS','MAIMON','IDLE','SCTP_INIT','SCTP_COOKIE_ECHO'], or EXIT? : ")
                    if(scan_type.upper() == 'EXIT'):
                        break;
                    scans.perform_nmap_scan2(scan_type.upper(), victim) 
                    
            elif choose == '16':
                while True:
                    scan_type = input("Enter the Type of Scan:  ['FRAGMENT', 'SOURCE_PORT',' MTU', 'IP_SPOOF', 'MAC_SPOOF'], or EXIT? : ")
                    if(scan_type.upper() == 'EXIT'):
                        break;
                    scans.perform_nmap_scan3(scan_type.upper(), victim)
                    
            elif choose == '17':
                print("\033[91mDOS Mode...Ctrl+C to Exit...\n")
                os.system(f"sudo hping3 {victim} --flood")
                
            elif choose == '18':
                print("NetBIOS Info....\n")
                os.system(f'sudo nmap -p 137 -sU -Pn -v  --script nbstat.nse {victim}')
                os.system(f'sudo nmap -p 137 -sS -Pn -v  --script nbstat.nse {victim}')
                time.sleep(3)
                print("SNMP Info....\n")
                os.system(f'sudo nmap -p 161 -sU -Pn -v  --script snmp-sysdescr.nse {victim}')
                os.system(f'sudo nmap -p 161 -sU -Pn -v  --script snmp-processes.nse {victim}')
                os.system(f'sudo nmap -p 161 -sU -Pn -v  --script snmp-win32-software.nse {victim}')
                os.system(f'sudo nmap -p 161 -sU -Pn -v  --script snmp-interfaces.nse {victim}')
                os.system(f'sudo snmp-check {victim}')           
                       
            elif choose == '19':
                print("LDAP Info....\n")
                os.system(f'sudo nmap -sT -p 389 --script ldap-brute.nse {victim}')
                time.sleep(3)
                print("NFS Info....\n")
                os.system(f'sudo nmap -sT -p 2049 --script nfs-ls.nse {victim}')
                os.system(f'sudo nmap -sT -p 2049 --script nfs-statfs.nse {victim}')
                os.system(f'sudo nmap -sT -p 2049 --script nfs-showmount.nse {victim}')
                
            elif choose == '20':
                print("DNS Info....\n")
                os.system(f'sudo nmap -sT -p 53 --script broadcast-dns-service-discovery.nse {victim}')
                os.system(f'sudo nmap -sT -p 53 --script dns-brute.nse {victim}')
                time.sleep(3)    
                print("SMTP INfo....\n")
                os.system(f'sudo nmap -sT -p 25,2525,587 --script smtp-enum-users.nse {victim}')
                os.system(f'sudo nmap -sT -p 25,2525,587 --script smtp-open-relays.nse {victim}')
                os.system(f'sudo nmap -sT -p 25,2525,587 --script smtp-commands.nse {victim}')
                
            elif choose == '21':
                print('Performing Agressive Scan on Default Ports of SMB, RPC, AND FTP...\n')
                time.sleep(3)
                os.system(f'nmap -sC -sV -A -v -p 21,111,445,2049 {victim}')
                                
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


