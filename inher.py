import socket

class test:
    def __init__(self):
        print("Объект создан")
        self.create_socket()

    def create_socket(self):
        HOST = "127.0.0.1"
        PORT = "9999"
        PORT = int(PORT)

        # supports the context manager type
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((HOST, PORT))  # associate the socket with a specific network interface
            print("socket created")


def main():
    t_obj = test()

if __name__ == '__main__':
    main()