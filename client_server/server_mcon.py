import selectors
import socket

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print ("Accept connection from: ", addr)
    conn.setblocking (False)
    data = types.SimpleNameSpace (addr = addr, inb = b'', out = b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register (conn, events, data=data)

def initialize():
    sel = selectors.DefaultSelector()
    host = "127.0.0.1"
    port = 9999

    lsock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)  # initialize socket object
    lsock.bind ((host, port))   # set it to concrete ip and port
    lsock.listen()      # set to listen
    print("listening on: ", (host,port))
    lsock.setblocking (False)   # no blocking after connection, we can wait for events on one or more sockets and then read and write data when it’s ready.
    sel.register(lsock, selectors.EVENT_READ, data=None)    # registers the socket to be monitored with sel.select(). For I/O events

    while True:
        events = sel.select(timeout=None)   # blocks until there are sockets ready for I/O. Returns a list of (key, event)
                                            # key - fileobj attribute (socket), mask - event mask of ready operations
        for key, mask in events:
                                            # if socket sends some data - so it's already accepted socket, so we call service_connection, if new - accept_wrapper
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)

if __name__ == '__main__':
    initialize()