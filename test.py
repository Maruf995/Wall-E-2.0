import serial
import time

# === Serial Port ===
arduino = serial.Serial('/dev/cu.usbserial-10', 9600)  # Замените на свой порт
time.sleep(2)  # Подождать, пока Arduino перезагрузится

# === Углы ===
RIGHT_ARM_UP = 80
RIGHT_ARM_DOWN =20

LEFT_ARM_UP = 70
LEFT_ARM_DOWN =130


# === Пины ===
LEFT_ARM = 5
RIGHT_ARM = 6

def send_command(servo, angle):
    command = f"{servo}:{angle}\n"
    arduino.write(command.encode())
    print(f"Sent -> Servo {servo}: {angle}")

try:
    send_command(LEFT_ARM, LEFT_ARM_UP)
    time.sleep(1)

    send_command(LEFT_ARM, LEFT_ARM_DOWN)
    time.sleep(1)

    send_command(RIGHT_ARM, RIGHT_ARM_UP)
    time.sleep(1)

    send_command(RIGHT_ARM, RIGHT_ARM_DOWN)
    time.sleep(1)

except KeyboardInterrupt:
    print("Остановлено пользователем.")
    arduino.close()
