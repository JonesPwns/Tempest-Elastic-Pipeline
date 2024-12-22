# Tempest-Elastic-Pipeline

This project captures real-time weather data broadcasted by a Tempest Weather Station on UDP port 50222, processes the data, and indexes it into an Elasticsearch instance. The parsed logs can then be visualized in Kibana to monitor weather conditions effectively.

Key Features:
- Listens for UDP broadcasts from the Tempest Weather Station.
- Parses JSON-formatted weather logs and enriches them with timestamps if necessary.
- Sends the processed data to Elasticsearch for storage and visualization.

Requirements:
- Python 3.x
- Elasticsearch instance running locally or remotely.
- Python libraries: socket, json, elasticsearch, datetime.
