# discovery_server.py
import pickle
import socket
from threading import Thread

class DiscoveryServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = {}

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"Discovery Server started on {self.host}:{self.port}")
        self.accept_connections()

    def accept_connections(self):
        while True:
            client_socket, client_address = self.server.accept()
            print(f"{client_address} connected")
            self.clients[client_address] = client_socket
            self.send_client_list()

    def send_client_list(self):
        client_list = [address for address in self.clients]
        for client_socket in self.clients.values():
            client_socket.send(pickle.dumps(client_list))

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    server = DiscoveryServer(host, port)
    server.start()
