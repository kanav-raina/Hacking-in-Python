import subprocess
import optparse

def get_arguments():
    parser=optparse.OptionParser()   #optparse to take command line arguments
    parser.add_option("-i","--interface",dest="interface",help="interface to change MAC address")
    parser.add_option("-m","--mac",dest="mac_address",help="New MAC address")
    (options,arguments)= parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface,use --help for more info")
    elif not options.mac_address:
        parser.error("please specify a mac_address,use --help for more info")
    return options

def change_mac(interface,mac_address):
    print("Changing MAC address for "+interface+" to "+mac_address)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])
options=get_arguments()
change_mac(options.interface,options.mac_address)
