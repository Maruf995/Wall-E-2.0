#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  150  // Минимальная длительность импульса
#define SERVOMAX  600  // Максимальная длительность импульса

// Диапазоны углов по портам
int minAngles[] = { -30,  0,  -30, -30, -30, 0 , 0};  // 0: Поворот головы
int maxAngles[] = {  30, 180, 150,  30,  30, 180 , 180};  // Максимальные углы для каждого сервопривода

void setup() {
  Serial.begin(9600);  // Ожидаем данные от Python через последовательный порт
  pwm.begin();         // Инициализируем PWM драйвер
  pwm.setPWMFreq(50);  // Устанавливаем частоту для сервомоторов
  delay(10);           // Ждем завершения инициализации
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');  // Читаем строку с данными
    input.trim();  // Убираем лишние пробелы и символы

    // Обрабатываем строку
    while (input.length() > 0) {
      int commaIndex = input.indexOf(',');
      String part;
      if (commaIndex != -1) {
        part = input.substring(0, commaIndex);
        input = input.substring(commaIndex + 1);
      } else {
        part = input;
        input = "";
      }

      // Разделяем на число и угол
      int colonIndex = part.indexOf(':');
      if (colonIndex != -1) {
        int servoNum = part.substring(0, colonIndex).toInt();  // Номер серво
        int angle = part.substring(colonIndex + 1).toInt();    // Угол для серво

        // Применяем индивидуальные ограничения углов
        angle = constrain(angle, minAngles[servoNum], maxAngles[servoNum]);

        // Управляем серво
        setServoAngle(servoNum, angle);
      }
    }
  }
}

// Функция для управления углом сервопривода
void setServoAngle(uint8_t servoNum, int angle) {
  // Преобразуем угол в импульс
  int pulse = map(angle, minAngles[servoNum], maxAngles[servoNum], SERVOMIN, SERVOMAX);
  pulse = constrain(pulse, SERVOMIN, SERVOMAX);  // Ограничиваем пределы импульса

  pwm.setPWM(servoNum, 0, pulse);  // Отправляем сигнал на конкретный сервомотор
}
