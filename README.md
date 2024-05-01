# SmartGarden

SmartGarden is a system that utilizes Raspberry Pi for monitoring and controlling the environment of a garden or plant area. It integrates various sensors to gather data such as temperature, light, and humidity, and allows users to remotely access this data and receive alerts.

## Features

- **Sensor Integration**: Utilizes sensors like MLX90640 thermal sensor, BH1750 light sensor, and DHT11 humidity sensor to monitor environmental conditions.
- **Relay Control**: Enables the control of relays based on sensor readings, allowing for automated actions such as watering plants or adjusting lighting.
- **Camera Integration**: Captures photos using a connected camera module and sends them to a designated MQTT broker for remote viewing.
- **MQTT Communication**: Facilitates communication with an MQTT broker for publishing sensor data and receiving commands remotely.
- **Error Logging**: Logs errors and important events to ensure smooth operation and facilitate troubleshooting.

## Setup and Usage

1. **Hardware Setup**: Connect the sensors (MLX90640, BH1750, DHT11) and relays to the Raspberry Pi according to the provided instructions.

2. **Software Installation**:
   - Install the required Python packages using pip: `pip install -r requirements.txt`
   - Ensure that the necessary libraries for the sensors (e.g., Adafruit CircuitPython) are installed.

3. **Configuration**:
   - Update the MQTT broker details (host, port, topic) in `main.py` to match your setup.
   - Adjust any other settings or thresholds in the code as needed.

4. **Running the Program**:
   - Execute the `main.py` script to start the SmartGarden system.
   - Monitor the console for logs and any error messages.
   - Access the MQTT broker to view sensor data and control the system remotely.

## Contributors

- [Aggelos Poulos] - [poulos@gmail.com]

## License

This project is licensed under the [Aggelos Poulos] License
