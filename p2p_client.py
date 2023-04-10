# p2p_client.py
import socket
import pickle
import time
from threading import Thread


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

class P2PClient:
    def __init__(self, discovery_host, discovery_port):
        self.discovery_host = discovery_host
        self.discovery_port = discovery_port
        self.message_history = []

    def update_peer_list(self, interval):
        while True:
            time.sleep(interval)
            self.connect_to_discovery()
            print("Updated peer list:", self.peer_list)

    def connect_to_discovery(self):
        self.discovery_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.discovery_client.connect((self.discovery_host, self.discovery_port))
        data = self.discovery_client.recv(1024)
        self.peer_list = pickle.loads(data)
        self.discovery_client.close()
        print("Connected peers:", self.peer_list)

    def send_message(self, recipient, message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(recipient)
                s.send(pickle.dumps(message))
                self.message_history.append(message)
                print("Message sent.")
        except Exception as e:
            print("Error sending message:", e)

    def start_receiver(self, host, port):
        self.receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receiver.bind((host, port))
        self.receiver.listen(5)
        print(f"Receiver started on {host}:{port}")
        self.accept_connections()

    def accept_connections(self):
        while True:
            sender_socket, sender_address = self.receiver.accept()
            Thread(target=self.handle_sender, args=(sender_socket,)).start()

    def handle_sender(self, sender_socket):
        try:
            data = sender_socket.recv(1024)
            message = pickle.loads(data)
            self.message_history.append(message)
            print(f"Message from {message['sender']}: {message['content']}")
        except Exception as e:
            print("Error receiving message:", e)
        finally:
            sender_socket.close()

if __name__ == "__main__":
    if __name__ == "__main__":
        discovery_host = "127.0.0.1"
        discovery_port = 12345
        username = input("Enter your username: ")
        local_host = get_local_ip()
        local_port = 0  # 设置为0将允许操作系统自动分配一个可用端口

        client = P2PClient(discovery_host, discovery_port)
        client.connect_to_discovery()

        Thread(target=client.start_receiver, args=(local_host, local_port)).start()
        Thread(target=client.update_peer_list, args=(30,)).start()

        # ...其他代码不变

    while True:
        print("Choose an option:")
        print("1. Send a message")
        print("2. Show message history")
        option = input()

        if option == "1":
            print("Choose a recipient from the list:")
            for idx, peer in enumerate(client.peer_list):
                print(f"{idx + 1}. {peer}")
            recipient_idx = int(input()) - 1
            recipient = client.peer_list[recipient_idx]
            content = input("Enter your message: ")

            message = {"sender": username, "content": content}
            client.send_message(recipient, message)
        elif option == "2":
            print("Message history:")
            for msg in client.message_history:
                print(f"{msg['sender']}: {msg['content']}")
