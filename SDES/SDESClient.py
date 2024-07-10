# Import the socket module 
import socket            

# Create a socket object 
s = socket.socket()      

# Define the port on which you want to connect 
port = 12345            

# Connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

# Send the key to the server
key = input("Enter key value: ")
s.send(key.encode())

# Receive data from the server and decode it to get the string
print (s.recv(1024).decode())

# Close the connection 
s.close()
