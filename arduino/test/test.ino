#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Настройки сигнала для серво
#define SERVOMIN  150 // Импульс для 0°
#define SERVOMAX  600 // Импульс для 180°

void setup() {
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(50); // Частота 50 Гц для серво
  delay(10);

  Serial.println("Servo 0 moving from 0° to 15° and back...");

  // Плавно вращаем серво 0 от 0 до 15 градусов
  for (int angle = 0; angle <= 5; angle++) {
    setServoAngle(3, angle);   // Устанавливаем угол
    delay(10);                 // Пауза для плавности (можно менять)
  }

  // Плавно возвращаем серво от 15 до 0 градусов
  for (int angle = 5; angle >= 0; angle--) {
    setServoAngle(4, angle);   // Устанавливаем угол
    delay(10);                 // Пауза для плавности (можно менять)
  }

  Serial.println("Done.");
}

void loop() {
  // Пока ничего не делаем
}

void setServoAngle(uint8_t servoNum, int angle) {
  angle = constrain(angle, 0, 180);  // Ограничиваем угол от 0 до 180
  int pulse = map(angle, 0, 180, SERVOMIN, SERVOMAX);  // Преобразуем угол в импульс
  pwm.setPWM(servoNum, 0, pulse);   // Устанавливаем импульс на канале сервопривода
}
