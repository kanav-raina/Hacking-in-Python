import socket

listener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("172.17.221.67",4444))   #binding our socket so we can listen to port 4444
listener.listen(0)                    #no of connection that can be queued before connection refused
print("[+] Waiting for incoming connection")
listener.accept()                     #if u get a connection then accept it
print("[+] Got a connection")
