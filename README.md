# Reverse Proxy

## Instructions
 1. Open up 4 terminal windows in the same folder as the three .py files
 2. In the first terminal window, type in a command that meets the following pattern: py server.py <port number>.
 3. In the second terminal window, type in a command that meets the following pattern: py server.py <port number>. Use a different port number from Step 2.
 4. In the third terminal window, type in a command that meets the following pattern: py reverse_proxy.py <client port number> <server port number 1> <server port number 2>. If you have more than 2 servers, just list them after <server port number 2>.
 5. In the fourth terminal window, type in a command that meets the following pattern: py client.py <port number>. Use a different port number from Steps 2 and 3.
 5. End server.py and reverse_proxy.py by pressing [Ctrl] + [Pause|Break] or the equivalent on your OS. [Ctrl] + [C] will not work.

## Results

The client will send 10 packets to the reverse proxy server which assigns it to the two servers with round robin. The server will respond 70% of the time and drop the packet the other 30%.

Here is a screenshot of what the first server printed in the terminal

![](./server%201%20screenshot.png)

Here is a screenshot of what the second server printed in the terminal

![](./server%202%20screenshot.png)

Here is a screenshot of what the reverse proxy server printed in the terminal

![](./proxy%20screenshot.png)

Here is a screenshot of what the client printed in the terminal

![](./client%20screenshot.png)