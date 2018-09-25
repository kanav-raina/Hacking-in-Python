import socket

connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #(family,type)
ip=raw_input("Enter the host ip")

port=int(input("Enter the pore"))
connection.connect((ip,port))
