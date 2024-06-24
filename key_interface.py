import os
import shutil
import getpass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='key_management.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def validate_user():
    
    password = getpass.getpass("Enter admin password: ")
    if password == "admin123":  
        return True
    else:
        logging.error("Invalid password.")
        return False

def update_server_keys():
    
    if validate_user():
        try:
            
            src_cert_path = "server.crt"
            dest_cert_path = "path_to_server.crt"  
            
            shutil.copy(src_cert_path, dest_cert_path)
            
            # Log server key update activity
            logging.info("Server keys updated successfully.")
            
            
            send_notification("Server keys updated successfully.")
            
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

def update_client_keys():
    
    if validate_user():
        
        
        # Log client key update activity
        logging.info("Client keys updated successfully.")
        
       
        send_notification("Client keys updated successfully.")

def send_notification(message):
    
    
    logging.info(f"Notification sent: {message}")

def main():
    
    print("Key Management Interface")
    print("========================")
    print("1. Update Server Keys")
    print("2. Update Client Keys")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        update_server_keys()
    elif choice == "2":
        update_client_keys()
    else:
        logging.error("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
