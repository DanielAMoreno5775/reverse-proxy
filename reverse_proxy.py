#reverse proxy for 1 client and 1+ servers
#by dam0503

import socket
import sys
from itertools import cycle

#uses round-robin to distribute client requests across multiple UDP connections
def reverseProxy(clientPort, arrOfSrvPorts):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    serverAddr = ('localhost', clientPort)
    print("[proxy] : Starting up on " + serverAddr[0] + " port " + str(serverAddr[1]))
    sock.bind(serverAddr)

    #set a timeout value of 5 seconds
    sock.settimeout(5)

    # Create a cycle iterator for round-robin scheduling
    serverCycle = cycle(arrOfSrvPorts)

    #loop forever
    while True:
        try:
            #receive initial message
            data, address = sock.recvfrom(4096)

            #if the received message came from the server, ignore it
            if address[1] in arrOfSrvPorts:
                pass
            #if the message came from the client and a message was received
            elif data:
                # Get the next server in the round-robin cycle
                nextSrvPort = next(serverCycle)
                server = ('localhost', nextSrvPort)
                
                # Forward the data to the selected server
                sent = sock.sendto(data, server)

                #receive the server's response
                srvResponse, secondResponseAddr = sock.recvfrom(4096)
                #construct the response according to the assignment and figure out index of port in list
                cur = arrOfSrvPorts.index(secondResponseAddr[1])
                stringifiedSrvResponse = str(srvResponse) + " via " + str(secondResponseAddr[1]) + " [" + str(cur) + "]"
                #remove the extra b' and '
                stringifiedSrvResponse = stringifiedSrvResponse[2:]
                stringifiedSrvResponse = stringifiedSrvResponse.replace("'","")

                #if there was a response forward it to the client
                sent = sock.sendto(stringifiedSrvResponse.encode("utf-8"), address)
        #handle timeouts in case server "drops" a packet
        except socket.timeout:
            pass

#check to ensure proper number of arguments
if len(sys.argv) < 3:
    print("Usage: " + sys.argv[0] + " <client port> <server port 1> [<server port 2> ...]")
    sys.exit(1)

#get the port for the client
clientProxyPort = int(sys.argv[1])
#unwrap the server ports from the remaining arguments
arrOfServerPorts = [int(port) for port in sys.argv[2:]]

#pass all of the port values to the function
reverseProxy(clientProxyPort, arrOfServerPorts)