# Network_Scanner
Created a Network Scanner using python, we utilised heavily Scapy, that allowed us to manipulate and analysis network traffic. We have ensured to comment as we go through the program, basic networking is a prerequisite. We have integration of the Network Scanner into a useful CLI Tool, using the optparse module.

Note: It is recommended to ensure you know your default gateway through Windows "ipconfig" command, or Linux "ifconfig" command.
It be even better to get peak at the routing table information, 
which depending on you system, the commands are different, but for Windows CMD Command: "netstat -nr", and Linux Terminal Command: "route -n".


# **Network Scanner Tool**

```
Usage: network_scanner.py [options]

Options:
  -h, --help          show this help message and exit
  -t IP, --target=IP  Target IP / IP range
```

### Run this command
```
python network_scanner.py -t [ CIDR ]
```

---

# **Network Scan Table**

| **[IP](ca://s?q=Explain_IP_addresses)** | **[MAC Address](ca://s?q=Explain_MAC_addresses)** | **[Hostname](ca://s?q=Explain_hostnames)** |
|-----------------------------------------|---------------------------------------------------|---------------------------------------------|
| 192.168.109.1                           | 00:50:56:c0:00:08                                 | Unknown                                     |
| 192.168.109.2                           | 00:50:56:e9:0d:f7                                 | _gateway                                    |
| 192.168.109.254                         | 00:50:56:fc:7e:4d                                 | Unknown                                     |


