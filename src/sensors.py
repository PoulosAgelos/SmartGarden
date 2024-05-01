# control_sensor.py
import board
import busio
import adafruit_bh1750
import adafruit_dht
import digitalio
from logger import log_info, log_error


class SensorController:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.light_meter = adafruit_bh1750.BH1750(self.i2c)
        self.dht = adafruit_dht.DHT11(board.D17)
        self.relay_humidity = digitalio.DigitalInOut(
            board.DXX)  # Αντικαταστήστε το XX με τον αριθμό του pin του relay για την υγρασία
        self.relay_light = digitalio.DigitalInOut(
            board.DYY)  # Αντικαταστήστε το YY με τον αριθμό του pin του relay για το φως

    def read_light(self):
        try:
            return self.light_meter.lux
        except Exception as e:
            log_error(f"Error reading light: {e}")
            return None

    def read_humidity(self):
        try:
            return self.dht.humidity
        except Exception as e:
            log_error(f"Error reading humidity: {e}")
            return None

    def control_relays(self, humidity, light):
        try:
            # Έλεγχος του relay για την υγρασία
            if humidity < 20:
                self.relay_humidity.value = True  # Ενεργοποίηση του relay για την υγρασία
            else:
                self.relay_humidity.value = False  # Απενεργοποίηση του relay για την υγρασία

            # Έλεγχος του relay για το φως
            if light < 100:  # Ορίστε το όριο φωτεινότητας που επιθυμείτε
                self.relay_light.value = True  # Ενεργοποίηση του relay για το φως
            else:
                self.relay_light.value = False  # Απενεργοποίηση του relay για το φως
        except Exception as e:
            log_error(f"Error controlling relays: {e}")


# Παράδειγμα χρήσης του SensorController
if __name__ == "__main__":
    controller = SensorController()
    while True:
        light = controller.read_light()
        humidity = controller.read_humidity()
        controller.control_relays(humidity, light)  # Έλεγχος των relays βάσει της υγρασίας και του φωτός
        log_info(f"Light: {light}, Humidity: {humidity}")
