import pygame
import serial
import time

# === Serial Port ===
arduino = serial.Serial('/dev/cu.usbserial-10', 9600)  # Замени на свой порт
time.sleep(2)

# === Pygame Joystick Init ===
pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

# === Constants ===
DEADZONE = 0.2

# === Preset positions ===
preset = [
    [410, 120],  # head rotation
    [532, 178],  # neck top
    [120, 310],  # neck bottom
    [465, 271],  # eye right
    [278, 479],  # eye left
    [340, 135],  # arm left
    [150, 360]   # arm right
]

# === Limits ===
NP_MIN, NP_MAX = 0, 180
NB_MIN, NB_MAX = -30, 150
HR_MIN, HR_MAX = -30, 30

# === Helpers ===
def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def apply_deadzone(value, deadzone):
    return 0 if abs(value) < deadzone else value

# === Set neutral position ===
arduino.write(b"1:90,2:60,0:0\n")
time.sleep(1)

prev_np, prev_nb, prev_hr = None, None, None
x_was_pressed = False  # флаг, чтобы не повторять цикл пока кнопку держат

try:
    while True:
        pygame.event.pump()

        # === Верхняя шея (neck top) — левый стик вверх/вниз (axis 1) ===
        left_stick_y = apply_deadzone(joystick.get_axis(1), DEADZONE)

        if abs(left_stick_y) < DEADZONE:
            np_angle = preset[1][0]
        else:
            np_angle = int(map_value(left_stick_y, -1, 1, 0, 180))
            np_angle = max(NP_MIN, min(NP_MAX, np_angle))

        # === Нижняя шея (neck bottom) — кнопки R1 и L1 (button 5 и button 4) ===
        up_pressed = joystick.get_button(11)  # Вверх на крестовине
        down_pressed = joystick.get_button(12)  # Вниз на крестовине

        if up_pressed:
            nb_angle = [120,30]
        elif down_pressed:
            nb_angle = preset[2][1]
        else:
            nb_angle = preset[2][0]

        # === Поворот головы — правый стик влево/вправо (axis 2) ===
        right_stick_x = apply_deadzone(joystick.get_axis(2), DEADZONE)

        if abs(right_stick_x) < DEADZONE:
            hr_angle = -15
        else:
            hr_angle = int(map_value(right_stick_x, -1, 1, -30, 0))
            hr_angle = max(HR_MIN, min(HR_MAX, hr_angle))

        # === Отправка на Arduino, если что-то изменилось ===
        if (np_angle != prev_np) or (nb_angle != prev_nb) or (hr_angle != prev_hr):
            command = f"1:{np_angle},2:{nb_angle},0:{hr_angle}\n"
            arduino.write(command.encode())

            prev_np, prev_nb, prev_hr = np_angle, nb_angle, hr_angle

        # === Движение на кнопку X (однократное нажатие) ===
        x_button = joystick.get_button(0)
        if x_button and not x_was_pressed:
            x_was_pressed = True
            for angle in [0, -17, 0]:
                command = f"4:{angle}\n"
                arduino.write(command.encode())
                print(f"Sent to pin 4: {angle}")
                time.sleep(0.4)
        elif not x_button:
            x_was_pressed = False

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Выход...")
    arduino.close()
    pygame.quit()
