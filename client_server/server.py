import socket

sock = socket.socket()

sock.bind( ("", 14900) )
sock.listen(2)
conn, addr = sock.accept()      # data / ip
data = conn.recv(16384)
udata = data.decode("utf-8")
print("Data: " + udata)