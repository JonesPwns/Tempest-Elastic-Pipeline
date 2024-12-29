# Tempest Weather Station Data Processor and Visualizer

This project captures real-time weather data broadcasted by a Tempest Weather Station on UDP port 50222. The data can either be processed and indexed into an Elasticsearch instance for advanced visualization in Kibana or visualized directly in real-time using Matplotlib.

---

## Key Features

- **Real-Time Visualization**:
  - Displays wind speed data dynamically using Matplotlib with a live-updating graph.
  - Visualizes up to the last 20 data points for clarity.

- **Data Processing**:
  - Listens for UDP broadcasts from the Tempest Weather Station.
  - Parses JSON-formatted weather logs, specifically focusing on "rapid_wind" events.

- **Elasticsearch Integration (Optional)**:
  - Enriches logs with timestamps if necessary and sends processed data to Elasticsearch for storage and advanced visualization.

---

## Requirements

- **Python 3.x**
- **Python Libraries**:
  - `socket`, `json`, `matplotlib`, `seaborn`, `datetime`
- **For Elasticsearch Integration**:
  - An Elasticsearch instance running locally or remotely.
  - `elasticsearch` Python library.

---

## Usage

1. Run the script to listen for UDP broadcasts and parse Tempest Weather Station data.
2. For real-time visualization, the data will be plotted dynamically in a Matplotlib graph.
3. For Elasticsearch integration, ensure your Elasticsearch instance is running and configured to accept the parsed data.

---

## Notes

- The script focuses on "rapid_wind" data for visualization but can be extended to process other types of weather logs.
- Ensure that the Tempest Weather Station is configured to broadcast data on UDP port 50222.
