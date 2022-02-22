import socket,os

os.system("clear")


s=socket.socket()

s.bind(("192.168.2.35",4444))

s.listen(10)

con, addr = s.accept()
print(f"[+] Connection comes From {addr[0]}:{addr[1]} ")
data = con.recv(1024)

with open("Mic_Nibbling_Savage.mp4","wb") as f:
    f.write(data)


s.close()


    
    

