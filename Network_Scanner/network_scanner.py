import scapy.all as scapy  #using scapy module

#using parser to get arguments from command line
def get_arguments():
    parser = optparse.OptionParses()
    parser.add_option("-t", "--target", dest="target", help="Target IP / IP range.")
    (options, arguments) = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip) #creating ARP packet 
    broadcast = scapy.Ether(dst= "ff:ff:ff:ff:ff:ff") # creating Ethernet object
    arp_request_broadcast = broadcast/arp_request # appending two packets to send
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0] # sending packets and receiving a response 


    
    clients_list = [] 
    for e in answered_list: #iterating through a list
        client_dict = {"ip":e[1].psrc, "mac":e[1].hwsrc} # creating dictionary for each client containing two keys
        clients_list.append(client_dict) # appending dict
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC address\n-------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client)

options = get_arguments()
scan_result = scan(options.target) 
print_result(scan_result)
