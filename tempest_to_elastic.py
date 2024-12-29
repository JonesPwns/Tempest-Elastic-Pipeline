import socket
import json

# Configure UDP listener
UDP_IP = "0.0.0.0"  # Listen on all available network interfaces
UDP_PORT = 50222    # Tempest Weather Station broadcast port

print(f"Listening for Tempest weather data on {UDP_IP}:{UDP_PORT}...")

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

try:
    while True:
        # Receive data from the Tempest Weather Station
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Received message from {addr}: {data.decode('utf-8')}")
        
        # Attempt to parse the data as JSON
        try:
            weather_data = json.loads(data.decode("utf-8"))
            print(f"Parsed Weather Data: {json.dumps(weather_data, indent=4)}")
        except json.JSONDecodeError:
            print("Failed to parse message as JSON.")
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    sock.close()
