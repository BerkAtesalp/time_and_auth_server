import socket
import ssl
import threading
import logging
import time

logging.basicConfig(level=logging.INFO)

def handle_client(client_socket, address):
    try:
        logging.info(f"Connection from {address} established.")
        current_time = time.ctime(time.time()) + "\n"
        client_socket.sendall(current_time.encode())
    except Exception as e:
        logging.error(f"Error handling client {address}: {e}")
    finally:
        client_socket.close()

def secure_time_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates TCP Socket with IPV4
    server_socket.bind(('127.0.0.1', 8443))
    server_socket.listen(5)
    logging.info("Secure time server started.")

    while True:
        client_socket, address = server_socket.accept()
        secure_client_socket = context.wrap_socket(client_socket, server_side=True)
        client_thread = threading.Thread(target=handle_client, args=(secure_client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    secure_time_server()
