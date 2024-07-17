# All the scans that will be performed using Thupparivalan!
import os

def perform_nmap_scan1(scan_type, target_ip):
    scan_commands = {
        'ARP': f'sudo nmap -sn -PR {target_ip} -v --reason',
        'UDP': f'sudo nmap -sn -PU {target_ip} -v --reason --disable-arp-ping',
        'ECHO': f'sudo nmap -sn -PE {target_ip} -v --reason --disable-arp-ping',
        'TS': f'sudo nmap -sn -PP {target_ip} -v --reason --disable-arp-ping',
        'ICMP_MASK': f'sudo nmap -sn -PM {target_ip} -v --reason --disable-arp-ping',
        'TCP_SYN': f'sudo nmap -sn -PS {target_ip} -v --reason --disable-arp-ping',
        'PROTOCAL_PING': f'sudo nmap -sn -PO {target_ip} -v --reason --disable-arp-ping',
        'ACK': f'sudo nmap -sn -PA {target_ip} -v --reason --disable-arp-ping'
    }
    
    command = scan_commands.get(scan_type)
    if command:
        os.system(command)
    else:
        print(f'Invalid scan type: {scan_type}. Please choose a valid scan type.')
        
def perform_nmap_scan2(scan_type, target_ip):
    scan_commands = {
        'TCP_CONNECT': f'nmap -sT {target_ip} -Pn -v --reason',
        'SYN': f'sudo nmap -sS {target_ip} -Pn -v --reason',
        'ACK': f'sudo nmap -sA {target_ip} -Pn -v --reason',
        'UDP': f'sudo nmap -sU {target_ip} -Pn -v --reason',
        'XMAS': f'sudo nmap -sX {target_ip} -Pn -v --reason',
        'MAIMON': f'sudo nmap -sM {target_ip} -Pn -v --reason',
        'OS': f'sudo nmap -O {target_ip} -Pn -v --reason',
        'AGGRESSIVE': f'sudo nmap -A {target_ip} -Pn -v --reason',
        'IDLE': f'sudo nmap -sI {target_ip} -Pn -v --reason',
        'SCTP_INIT': f'sudo nmap -sY {target_ip} -Pn -v --reason',
        'SCTP_COOKIE_ECHO': f'sudo nmap -sZ {target_ip} -Pn -v --reason',  
        'SERVICE': f'sudo nmap -sC -sV {target_ip} -Pn -v --reason'   
    }
    
    command = scan_commands.get(scan_type)
    if command:
        os.system(command)
    else:
        print(f'Invalid scan type: {scan_type}. Please choose a valid scan type.')
        
def perform_nmap_scan3(scan_option, target_ip):
    scan_commands = {
        'FRAGMENT': f'sudo nmap -f {target_ip} -Pn -v --reason',
        'SOURCE_PORT': f'sudo nmap -g 80 {target_ip} -Pn -v --reason', # can change port if needed
        'MTU': f'sudo nmap -mtu 8 {target_ip} -Pn -v --reason',
        'IP_SPOOF': f'sudo nmap -D RND:10 {target_ip} -Pn -v --reason', # change rnd value
        'MAC_SPOOF': f'sudo nmap -sT --spoof-mac 0 {target_ip} -Pn -v --reason'
    }
    
    command = scan_commands.get(scan_option)
    if command:
        os.system(command)
    else:
        print(f'Invalid scan option: {scan_option}. Please choose a valid scan option.') 
