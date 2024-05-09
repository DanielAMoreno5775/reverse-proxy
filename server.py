import random 
import socket
import sys

#print out an invalid syntax message if the command doesn't have enough arguments
if len(sys.argv) == 2:
    #get the port number from the command-line arguments
    socketPortNum = int(sys.argv[1])
    #get the IP address for the local computer; arrays were necessary as my computer had multiple IP addresses for each adapter and only one worked
    socketIPAddr = socket.gethostbyname("localhost")

    #create the UDP socket for the server
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #bind the socket to an IP address and a port number
    serverSocket.bind((socketIPAddr, socketPortNum)) 

    #set the message that will be sent back to the client
    message = "PONG"
    #define the max buffer size
    bufSize = 4096

    #print ready message
    print("[server] : ready to accept data...")
    #runs the program forever
    while True: 
        #wait for a message from the client
        receivedMsg, address = serverSocket.recvfrom(bufSize)

        #generates random integer from [0, 10)
        rand = random.randint(0, 10)  
        #if rand is less than 7 (70% chance), reply
        if rand <= 7: 
            #print the received message
            receiptMsg = "[client] : {}".format(receivedMsg)
            print(receiptMsg)
            #and send a message back
            serverSocket.sendto(message.encode("utf-8"), address)
        #otherwise, say that the packed was dropped
        else:
            print("[server] : packet dropped")
else:
    print("Invalid syntax: py", sys.argv[0], "<port number>")
    print("Good Example: py", sys.argv[0], "8008")