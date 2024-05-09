import socket
import sys


#print out an invalid syntax message if the command doesn't have enough arguments
if len(sys.argv) == 2:
    #get the server's hostname from the command-line arguments and then the computer's IP address
    socketIPAddr = socket.gethostbyname("localhost")
    #get the port number from the command-line arguments
    socketPortNum = int(sys.argv[1])

    #create the UDP socket for the client
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #bind the socket to an IP address and a port number
    server_address = (socketIPAddr, socketPortNum)

    #set a timeout value of 5 seconds
    mysocket.settimeout(5)
    #define the message to be sent
    message = 'PING'
    #define the max buffer size
    bufSize = 4096

    # Loop that will execute 2 times, temporarily
    for i in range(1, 11):
        #initialize finalStr
        finalStr = ""
        #try-except block that will catch timeouts
        try:
            #send the message
            sent = mysocket.sendto(message.encode("utf-8"), server_address)
            #create the start of the finalStr with the sending part
            finalStr = "{:<3} : client sent {}... ".format(i, message)
            #receive data from server
            data, server = mysocket.recvfrom(bufSize)
            #appended received data to finalStr
            finalStr += "received "
            finalStr += str(data)
        except socket.timeout:
            #if the recvfrom function timed out, append that
            finalStr += "Timed Out"
        #once everything else is done, print finalStr
        finally:
            print(finalStr)

    #close the socket once the loop is finished
    mysocket.close()
else:
    print("Invalid syntax: py", sys.argv[0], "<port number>")
    print("Good Example: py", sys.argv[0], "8008")