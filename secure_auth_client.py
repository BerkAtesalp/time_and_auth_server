import socket
import ssl

HOST = '127.0.0.1'  # Server IP Address
PORT = 8444         # Server Port
MESSAGE = b"admin:password123"  # Username and Password

def secure_auth_client(host, port, message):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)  
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Wrap the socket with the SSL context
        secure_socket = context.wrap_socket(s, server_hostname=host)
        
        try:
            secure_socket.connect((host, port))
            secure_socket.sendall(message)
            
            # Receive data from the server
            data = secure_socket.recv(1024)
            
            # Print received data
            print(f"Received: {data.decode('utf-8')}")
            
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    secure_auth_client(HOST, PORT, MESSAGE)
