# time_and_auth_server

Overview:
This project implements a secure time and authentication server using SSL for secure communication. It includes functionality for generating self-signed certificates, managing server and client keys, a secure authentication server, and a secure time server and client.

Features
Self-Signed Certificate Generation: Generate a self-signed SSL certificate for secure communication.
Key Management Interface: Update server and client keys with validation and logging.
Secure Authentication Server: Authenticate clients using username and password, and issue JWT tokens.
Secure Time Server and Client: A time server that sends the current time securely to clients.
Project Structure
generate_cert.py: Script to generate a self-signed SSL certificate.
key_management.py: Script for updating server and client keys with logging and validation.
secure_auth_server.py: Secure authentication server that authenticates clients and issues JWT tokens.
secure_client.py: Secure client for sending authentication messages to the server.
secure_time_server.py: Secure time server that sends the current time to clients.
secure_time_client.py: Secure time client that receives the current time from the server.
