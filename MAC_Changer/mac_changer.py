import subprocess
import optparse
import re

#using parses to manualy add interface and mac address from command line
def get_argumnets():
    parser = optparse.OptionParses()
    parser.add_option("-i", "--interface", dest="interface", help="Changing MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = get_arguments()
    if not options.interface: # checking  if interface is given
       parser.error("[-] Please enter an interface, use --help for info")
       get_arguments()
    elif not options.new_mac: # checking if new mac address is given
         parser.error("[-] Please enter a MAC address, use --help for info")
         get_arguments()
    return options


def  change_mac(interface, new_mac):
    print("[+] Changing MAC addres for " + interface + " to " + new_mac)
    #commands getting executed to change mac address
    subprocess.call("ifconfig" + interface +" down", shell= True)
    subprocess.call("ifconfig" + interface +" hw ether" + new_mac, shell= True)
    subprocess.call("ifconfig" + interface +" up", shell= True)



def get_current_mac(interface):
    #getting desired interface
    ifconfig_result = subprocess.check_output(["ifconfing", interface])
    print(ifconfig_result)

    #getting current mac address of device
    mac_address_search_result = re.search(r"\w\w:\w\:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0) # checking if we got the mac address
    else:
        print("[-] Couldn't read MAC address") # 
        

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Currenct MAC = " + str(current_mac)) # printing current mac address

change_mac(options.interface, options.new_mac) # changing mac address

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac: # checking if mac address was changed successfully 
    print("[+] MAC adress was successfully changed to " + current_mac)
else:
    print("[-] Couldn't change the MAC address")




