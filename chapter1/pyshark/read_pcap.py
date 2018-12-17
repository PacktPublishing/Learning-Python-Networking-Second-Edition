#!/usr/bin/env python3

import pyshark

#cap = pyshark.FileCapture('http.cap', display_filter="dns")
#for pkt in cap:
#	print(pkt)
	
cap = pyshark.FileCapture('http.cap', keep_packets=False)

def print_info_layer(packet):
	print("[Protocol:] "+packet.highest_layer+" [Source IP:] "+packet.ip.src+" [Destination IP:]"+packet.ip.dst)

cap.apply_on_packets(print_info_layer)
