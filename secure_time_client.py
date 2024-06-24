import socket
import ssl

def secure_time_client(host, port):
    # Create a secure SSL context
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    # Load the server's certificate (server.crt)
    context.load_verify_locations("server.crt")  
    
    # Create a socket and wrap it with SSL
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print("Connected to the server.")
            
            
            data = ssock.recv(1024).decode("utf-8")
            print(f"Received time from server: {data}")

if __name__ == "__main__":
    HOST = 'localhost'  
    PORT = 8443        
    
    secure_time_client(HOST, PORT)
