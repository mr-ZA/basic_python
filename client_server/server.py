import socket

HOST = "127.0.0.1"
PORT = "9999"
PORT = int(PORT)

# supports the context manager type
with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))         #  associate the socket with a specific network interface
    sock.listen()
    conn, addr = sock.accept()      # data / ip     [block, waits for connection on call]
    with conn:
        print ("Connected by: ", addr)
        while True:
            data = conn.recv(16384)
            udata = data.decode("utf-8")
            print("Data: " + udata)
            if not data:
                continue
            conn.sendall(data)