# Import the socket library 
import socket			 

#Create a socket object 
s = socket.socket()		 
print ("Socket successfully created!")

# Reserve a port on your computer  
# Here, 12345 but it can be anything 
port = 12345			

# Bind it to the port 
# Leave the IP Field Empty (inputted an empty string)
# This makes the server listen to requests coming from other computers on the network 
s.bind(('', port))		 
#print ("Socket Binded to %s" %(port)) 

# Put the socket to a listening mode 
s.listen(5)	 
print ("Socket is Listening...")		 


#Function to implement S-DES
def DES(key):
	P10 = [3,5,2,7,4,10,1,9,8,6]
	P8 = [6,3,7,4,8,5,10,9]
	new = ""
	for i in P10:
		new = new + key[i-1]
	print("Applied P10: ", new)

	sub1_l = new[1:5] + new[0]
	sub1_r = new[6:10] + new[5]
	lcs1 = sub1_l + sub1_r
	print("LCS-1: ", lcs1)

	new2 = ""
	for j in P8:
		new2 = new2+lcs1[j-1]
	print("Applied P8 (Subkey 1): ", new2)

	sub2_l = lcs1[2:5] + lcs1[0] + lcs1[1]
	sub2_r = lcs1[7:10] + lcs1[5] + lcs1[6]
	lcs2 = sub2_l + sub2_r
	print("LCS-2: ",lcs2)

	new3 = ""
	for k in P8:
		new3 = new3 + lcs2[k-1]
	print("Applied P8 (Subkey 2): ", new3)

# A forever loop until we interrupt it or an error occurs 
while True: 

	# Establish a connection with the client
	c, addr = s.accept()	 
	print ('Got connection from', addr )
	
	# Send a thank you message to the client
	#Encoding to send a byte type message
	c.send('Thank you for connecting!'.encode()) 

	#Receiving the key
	key = c.recv(1024).decode()
	print("Key received - ",key)
	
	DES(key)
	
	# Close the connection with the client 
	c.close()
	
	# Break once connection closed
	break
