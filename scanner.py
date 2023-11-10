import multiprocessing
from scapy.all import IP, TCP, sr1

def scan_port(target_ip, port):
    syn_packet = IP(dst=target_ip) / TCP(dport=port, flags="S")  
    response = sr1(syn_packet, timeout=1, verbose=0)   
    if response and response.haslayer(TCP) and response[TCP].flags == 0x12:
        print(f"Port {port} on {target_ip} is open.")
def tcp_syn_scanner(target_ip, ports):
    pool = multiprocessing.Pool() 
    pool.starmap(scan_port, [(target_ip, port) for port in ports])   
    pool.close()
    pool.join()
if __name__ == "__main__":
    target_ip = input("Please intup ip to scan: ")
    ports_to_scan = range(1, 1025)
    print(f"Scanning ports on {target_ip} using TCP SYN scanner...")
    tcp_syn_scanner(target_ip, ports_to_scan)
   
