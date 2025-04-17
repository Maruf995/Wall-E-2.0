import serial
import time

# === Подключение к Arduino ===
arduino = serial.Serial('/dev/cu.usbserial-10', 9600)  # Укажи свой порт
time.sleep(2)

# === Функция для отправки угла ===
def set_servo_angle(pin, angle):
    command = f"{pin}:{angle}\n"
    arduino.write(command.encode())
    print(f"Отправлено: {command.strip()}")
    time.sleep(1)  # Задержка, чтобы серво успело переместиться

# === Последовательность углов ===
angles = [0,45,0]
angles2 = [0, -17, 0]

# === Перемещаем серво на пине 5 по указанным углам ===
for angle2 in angles2:
    # set_servo_angle(5, angle)  # Устанавливаем угол для пина 5
    set_servo_angle(4, angle2)  # Устанавливаем угол для пина 5
    time.sleep(1)  # Задержка между движениями

# === Закрытие соединения с Arduino ===
arduino.close()
