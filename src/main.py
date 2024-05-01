# main.py
import time
import paho.mqtt.client as mqtt
from sensors import SensorController
from camera import CameraController
from logger import log_info, log_error

# Στοιχεία σύνδεσης MQTT broker
MQTT_BROKER_HOST = "your_broker_ip_address"
MQTT_BROKER_PORT = 1883
MQTT_TOPIC = "sensor_data"
MQTT_PHOTO_TOPIC = "photo"

# Δημιουργία MQTT client
client = mqtt.Client()

# Συνάρτηση σύνδεσης με τον MQTT broker
def on_connect(client, userdata, flags, rc):
    log_info("Connected to MQTT broker.")
    client.subscribe(MQTT_TOPIC)

# Συνάρτηση αποστολής δεδομένων στον MQTT broker
def send_sensor_data(temperature, light, humidity):
    try:
        client.publish(MQTT_TOPIC, f"Temperature: {temperature}, Light: {light}, Humidity: {humidity}")
        log_info("Sensor data sent to MQTT broker.")
    except Exception as e:
        log_error(f"Error sending sensor data to MQTT broker: {e}")

# Συνάρτηση αποστολής φωτογραφίας μέσω MQTT
def send_photo(filename):
    try:
        with open(filename, "rb") as f:
            photo_data = f.read()
        client.publish(MQTT_PHOTO_TOPIC, photo_data)
        log_info(f"Photo sent via MQTT: {filename}")
    except Exception as e:
        log_error(f"Error sending photo via MQTT: {e}")

# Αρχικοποίηση του SensorController και του CameraController
sensor_controller = SensorController()
camera_controller = CameraController()

# Σύνδεση με τον MQTT broker και εκκίνηση του κύκλου ανάγνωσης δεδομένων
client.on_connect = on_connect
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)
client.loop_start()

# Κύκλος λήψης φωτογραφιών και αποστολής δεδομένων
while True:
    try:
        # Λήψη φωτογραφίας
        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = f"photo_{timestamp}.jpg"
        camera_controller.capture_photo(filename)
        log_info(f"Photo captured: {filename}")

        # Αποστολή φωτογραφίας μέσω MQTT
        send_photo(filename)

        # Ανάγνωση δεδομένων αισθητήρων
        temperature = sensor_controller.read_temperature()
        light = sensor_controller.read_light()
        humidity = sensor_controller.read_humidity()
        log_info(f"Temperature: {temperature}, Light: {light}, Humidity: {humidity}")

        # Έλεγχος και έναρξη/διακοπή των relays
        sensor_controller.control_relays(humidity, light)

        # Αποστολή δεδομένων στον MQTT broker
        send_sensor_data(temperature, light, humidity)

        time.sleep(300)  # Περίμενε 5 λεπτά μεταξύ των κύκλων ελέγχου

    except Exception as e:
        log_error(f"Error in main loop: {e}")
