import socket
import json
from elasticsearch import Elasticsearch
from datetime import datetime

# Configure Elasticsearch client
es = Elasticsearch(["http://localhost:9200"])
index_name = "tempest-weather"

# UDP listener configuration
UDP_IP = "0.0.0.0"
UDP_PORT = 50222

# Create a socket to listen for UDP packets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for Tempest weather data on {UDP_IP}:{UDP_PORT}...")

while True:
    try:
        # Receive data from the weather station
        data, addr = sock.recvfrom(1024)
        decoded_data = data.decode('utf-8')

        # Parse the JSON log from the Tempest weather station
        weather_data = json.loads(decoded_data)

        # Enrich with a timestamp if not present
        if "timestamp" not in weather_data:
            weather_data["timestamp"] = datetime.utcnow().isoformat()

        # Index the data into Elasticsearch
        response = es.index(index=index_name, document=weather_data)

        # Log success to the console
        print(f"Data indexed to Elasticsearch: {response['result']}")

    except json.JSONDecodeError:
        print("Received malformed JSON data.")

    except Exception as e:
        print(f"An error occurred: {e}")
