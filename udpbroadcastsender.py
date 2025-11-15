from socket import *
import time
import random
import json

BROADCAST_IP = '255.255.255.255' #special IP address for broadcast
PORT = 17000

sock_sender = socket(AF_INET, SOCK_DGRAM)
sock_sender.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

aktier = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

for i in range(10):
    aktie_dictionary = {
        "navn": random.choice(aktier),
        "antal": random.randint(1, 10),
        "pris": random.randint(100, 1500)
    }
    message: str = json.dumps(aktie_dictionary)
    print(f'Broadcaster sending: {message}')
    sock_sender.sendto(message.encode(), (BROADCAST_IP, PORT))
    time.sleep(2) # sleep for 2 seconds between messages

sock_sender.close()