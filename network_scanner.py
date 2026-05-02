#!/usr/bin/python
# author: Fionn Finane
import socket
import scapy.all as scapy
import optparse
# Network Scanner Algorithm
# Objective --> Discover clients on the network.
# Steps:
# 1. To enhance the network scanner through leveraging the command line.
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="ip", help="Target IP / IP range")
    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error("[-] Please specify an target ip / ip range, use --help for more info.")
    return options
# 2. Create arp request directed to broadcast MAC asking for IP.
def scan(ip):
    # Use ARP to ask who has target IP.
    arp_request = scapy.ARP(pdst=ip)
    # Set destination MAC to broadcast MAC.
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine both arp request and the broadcast MAC into 1 packet.
    arp_request_broadcast = broadcast/arp_request
    # Send packet and receive response.
    # Extracting all answered packets in 1 second.
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # Parse the response.
    clients_list = []
    for response in answered_list:
        client_info ={"ip": response[1].psrc, "mac": response[1].hwsrc}
        try:
            hostname = socket.gethostbyaddr(client_info["ip"])[0]
            client_info["hostname"] = hostname
        except socket.herror:
            client_info["hostname"] = "Unknown"
        clients_list.append(client_info)
    return clients_list
# 3. Print the results.
def print_result(results_list):
    print("IP\t\t\tMAC Address\t\t\tHostname\n-----------------------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"] + "\t\t" + client["hostname"])

# Calling the methods above.
options = get_args()
scan_results = scan(options.ip)
print_result(scan_results)
