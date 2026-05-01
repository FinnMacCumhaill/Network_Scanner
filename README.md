# Network-Scanner
Created a basic, but powerful network scanner using python, we utilised heavily Scapy, that allowed us to manipulate and analysis network traffic. We have ensured to comment as go through the program, basic networking is a prerequisite. We have interrogated this Network Scanner into a useful CLI Tool, using the optparse module.

Note: It is recommended to ensure you know your default gateway through Windows "ipconfig" command, or Linux "ifconfig" command.
It be even better to get peak at the routing table information, 
which depending on you system, the commands are different, but for Windows CMD Command: "netstat -nr", and Linux Terminal Command: "route -n".

Network Scanner Tool in action below:

-----------------------------------------------------------------------------------------------------

python network_scanner.py --help
Usage: network_scanner.py [options]

Options:
  -h, --help          show this help message and exit
  -t IP, --target=IP  Target IP / IP range


python network_scanner.py --target [Network Address/Gateway]/[subnet-prefix]


------------------------------------------------------------------------------------------------------
