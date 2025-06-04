import cv2

# Загрузка предобученного классификатора для распознавания лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Захват видео с камеры (0 — встроенная камера)
cap = cv2.VideoCapture(2)

while True:
    # Считывание кадра
    ret, frame = cap.read()
    if not ret:
        break

    # Преобразование в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Отрисовка прямоугольников вокруг лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Показ изображения
    cv2.imshow('Face Detection', frame)

    # Выход при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
