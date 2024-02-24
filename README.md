[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



# Simple-Client-Server-Application
This repository contains a simple client-server application implemented in Python using sockets.
## Description

The client-server application consists of two scripts: one for the server side and the other for the client side. The server listens for requests from the client, looks up values based on the keys received, and sends them back to the client. The client sends keys to the server and prints the corresponding values received from the server.

## Usage

### Server Side

1. Run the `server.py` script on the machine that will act as the server.
   ```bash
   python server.py
- The server will start listening for incoming connections.

### Client Side

1. Run the `client.py` script on the machine that will act as the server.
   ```bash
   python client.py
- Enter keys when prompted. The client will send these keys to the server.
- The client will receive the corresponding values from the server and print them.

- **Usage**: Provides instructions on how to use the client and server scripts, including starting the server, running the client, and exiting the program.

### Files Structure Section
```
## Lists the files included in the repository and their purposes

- `server.py`: Python script for the server side.
- `client.py`: Python script for the client side.
- `ozax.txt`: Text file containing key-value pairs for the server to look up.
```
### Exiting the Program
```
To exit the program, simply enter '@' as the key on the client side. This will terminate the connection between the client and server.
```
## Requirements

- Python 3.x
