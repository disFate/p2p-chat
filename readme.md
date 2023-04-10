# P2P Chat System

This P2P chat system is a simple Python implementation that allows users to discover each other through a central server and then communicate peer-to-peer. The server is only used for discovering and connecting clients, and it does not store any messages. Clients can send messages to other clients and store received messages locally.

## System Components

1. **discovery_server.py** - The server for handling user discovery.
2. **p2p_client.py** - The client for handling user interface, data storage, and communication.

## Dependencies

- Python 3.x

## How to Run

1. First, run `discovery_server.py` to start the server.

```bash
python discovery_server.py
```

2. Next, run `p2p_client.py` to start a client. You can start multiple clients for multi-user communication.

```bash
python p2p_client.py
```

3. In the client, enter a username when prompted.

4. Then, you can choose to send a message or show message history.

## Usage

1. Run `discovery_server.py` to start the server.
2. Run one or more `p2p_client.py` clients.
3. In the client, enter a username when prompted.
4. Connect to the discovery server to get a list of other online clients.
5. Choose an action based on the prompts, such as sending a message or showing message history.

## Notes

- The discovery server must always be online to handle connection requests from new clients.
- If a client fails to connect to the discovery server, it will not be able to get a list of other clients.
- Messages sent between clients will be stored locally on each client and will not be transmitted through the server.
- The current implementation does not support encryption and authentication. Therefore, it is not recommended to use this system on public networks.