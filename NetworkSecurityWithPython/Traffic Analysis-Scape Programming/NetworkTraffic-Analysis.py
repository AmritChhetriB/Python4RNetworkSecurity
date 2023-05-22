# Author: Amrit Chhetri, Digital Forensic Researcher
# Purpose: Network Traffics Sniffing and Analysis
# Module: Scapy, https://pypi.org/project/scapy/
# Installations: pip3 install scape or using Interpreter option in PyCharm
# https://www.wireshark.org/download/automated/captures/

import scapy.layers.l2
from scapy.all import *

networkPackets = PcapReader("NM_2023-03-27T03-17-54.pcap")
# Detecting ARP Spoofing
def isARPSpoofed(packetArg):
    if packetArg.haslayer(scapy.layers.l2.ARP) and packetArg[scapy.layers.l2.ARP].op == 2:
            print(packetArg.show())
    else:
            print("No ARP Spoofing")
for networkPacket in networkPackets:
    print(networkPacket.show())
    isARPSpoofed(networkPacket)



