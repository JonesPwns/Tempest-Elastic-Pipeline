import socket
import json
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

# Use Seaborn for styling
sns.set_theme()

# Real-time data storage
wind_speeds = []
timestamps = []

# Initialize the figure
fig, ax = plt.subplots()
line, = ax.plot([], [], label="Wind Speed (m/s)")
ax.set_title("Real-Time Wind Speed")
ax.set_xlabel("Time")
ax.set_ylabel("Wind Speed (m/s)")
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Update function for real-time plotting
def update_plot(frame):
    if timestamps and wind_speeds:
        line.set_data(timestamps, wind_speeds)
        ax.relim()
        ax.autoscale_view()
    return line,

# Function to listen for UDP broadcast messages
def listen_udp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 50222))
    print("Listening for Tempest weather data on 0.0.0.0:50222...")

    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(f"Received message from {addr}: {data.decode('utf-8')}")
            message = json.loads(data.decode('utf-8'))
            
            # Only process rapid wind data
            if message["type"] == "rapid_wind":
                ob = message["ob"]
                timestamp = datetime.datetime.fromtimestamp(ob[0], datetime.timezone.utc).strftime('%H:%M:%S')
                wind_speed = ob[1]
                
                # Update data
                timestamps.append(timestamp)
                wind_speeds.append(wind_speed)
                
                # Keep only the last 20 data points for better visualization
                if len(timestamps) > 20:
                    timestamps.pop(0)
                    wind_speeds.pop(0)
                
                print(f"Parsed Data - Timestamp: {timestamp}, Wind Speed: {wind_speed} m/s")
        except Exception as e:
            print(f"Error: {e}")

# Start real-time plotting
ani = FuncAnimation(fig, update_plot, interval=1000, cache_frame_data=False)

# Run the UDP listener in a blocking manner
try:
    listen_udp()
except KeyboardInterrupt:
    print("Exiting...")
