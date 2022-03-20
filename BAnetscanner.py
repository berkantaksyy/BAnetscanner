import scapy.all as scanner
import sys

if ("--help" in sys.argv):
    print("""
    If you choose '1', write the area to be scanned. 
    If you choose '2', BAnetscanner scanned 192.168.1.1/24
    If you choose '3', BAnetscanner scanned 127.0.0.1/24
    If you choose '4', BAnetscanner scanned 10.0.2.1/24""")
    sys.exit()




print("Welcome !!")
print("BAnetscanner ready")

while True:
    try:
        print("-------------------------------------------------------------------")
        print("Which do you want to choose for scan ip operation?")
        print("1-)I write\n2-)Scan 192.168.1.1/24\n3-)Scan 127.0.0.1/24\n4-)Scan 10.0.2.1/24")
        choose_operation = str(input("Choose: "))
        print("-------------------------------------------------------------------")
    except:
        print("Pls, choose 1,2,3 or 4!")
        continue
    else:
        break

def new_scanner(ip_address):
    arp_scanner = scanner.ARP(pdst=ip_address)
    packet_scanner = scanner.Ether(dst="ff:ff:ff:ff:ff:ff")
    new_packet = packet_scanner/arp_scanner
    (answered,unanswered) = scanner.srp(new_packet,timeout=1)
    answered.summary()

if choose_operation == "1":
    scan_ip_address = str(raw_input("The area you will scan: "))
    new_scanner(scan_ip_address)
elif choose_operation == "2":
    new_scanner("192.168.1.1/24")
elif choose_operation == "3":
    new_scanner("127.0.0.1/24")
elif choose_operation == "4":
    new_scanner("10.0.2.1/24")
else:
    print("You didn't make the right choice [1,2,3,4]")
    print("Restart the programs.")


