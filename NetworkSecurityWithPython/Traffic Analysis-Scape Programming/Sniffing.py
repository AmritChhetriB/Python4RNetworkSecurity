# Author: Amrit Chhetri, Digital Forensic Researcher
# Purpose: Network Traffics Sniffing and Analysis
# Module: Scapy, https://pypi.org/project/scapy/
# Installations: pip3 install scape or using Interpreter option in PyCharm

from scapy.all import *
networkPackets = sniff(count=16)
#Writing to PCAP file
wrpcap("Sniffed.pcap", networkPackets)
#Displaying packets
for networkPacket in networkPackets:
    print(networkPacket.show())
