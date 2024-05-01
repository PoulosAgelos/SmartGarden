# camera.py
import time
import board
import busio
import adafruit_mlx90640
from logger import log_info, log_error

class CameraController:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.mlx = adafruit_mlx90640.MLX90640(self.i2c)
        self.mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ
        self.frame = [0] * 768  # 24x32 pixels

    def capture_photo(self, filename):
        try:
            self.mlx.getFrame(self.frame)
            with open(filename, "w") as f:
                for row in self.frame:
                    f.write(' '.join([str(i) for i in row]) + '\n')
            log_info(f"Thermal image captured: {filename}")
        except Exception as e:
            log_error(f"Error capturing thermal image: {e}")

# Παράδειγμα χρήσης του CameraController
# if __name__ == "__main__":
#     controller = CameraController()
#     while True:
#         timestamp = time.strftime("%Y%m%d%H%M%S")
#         filename = f"thermal_image_{timestamp}.txt"
#         controller.capture_photo(filename)
#         time.sleep(5)
