import socket
import ssl
import threading
import jwt
import hashlib
import logging

logging.basicConfig(level=logging.INFO)

SECRET_KEY = "your_secret_key"
USER_DATABASE = {"admin": hashlib.sha256("password123".encode()).hexdigest()}

def authenticate_user(username, password):
    hashed_password = USER_DATABASE.get(username)
    return hashed_password == hashlib.sha256(password.encode()).hexdigest()

def handle_client(client_socket, address):
    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        
        # Ensure data is a bytes-like object
        if not isinstance(data, bytes):
            raise ValueError("Expected bytes-like object.")
        
        # Decode the received data into a string
        data_str = data.decode('utf-8').strip()
        
        # Split the string into username and password
        username, password = data_str.split(":")
        
        if authenticate_user(username, password):
            payload = {"username": username}
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
            
            # Send the token back to the client
            client_socket.sendall(token.encode('utf-8'))
        else:
            client_socket.sendall("Authentication failed.".encode('utf-8'))
            
    except Exception as e:
        logging.error(f"Error handling client {address}: {e}")
    finally:
        client_socket.close()


def secure_auth_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)  # Specify TLS 1.2 protocol version
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8444))
    server_socket.listen(5)
    logging.info("Secure authentication server started.")

    while True:
        client_socket, address = server_socket.accept()
        secure_client_socket = context.wrap_socket(client_socket, server_side=True)
        client_thread = threading.Thread(target=handle_client, args=(secure_client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    secure_auth_server()
