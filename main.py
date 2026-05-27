import cv2
import mediapipe as mp
from tensorflow.keras.models import load_model
import numpy as np
import time

# ===== CAMERA =====
cap = cv2.VideoCapture(0)

# ===== MEDIAPIPE =====
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# ===== CLASSES =====
classes = [
    'A','B','C','D','E','F','G',
    'I','L','M','N','O','P',
    'Q','R','S','T','U','V','W','Y'
]

# ===== LOAD MODEL =====
model = load_model('keras_model.h5')

# ===== ARRAY =====
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# ===== TEXTO =====
texto = ""

ultima_letra = ""
tempo_letra = time.time()

TEMPO_CONFIRMACAO = 1.2

while True:

    success, img = cap.read()

    if not success:
        continue

    img = cv2.flip(img, 1)

    frameRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(frameRGB)

    handsPoints = results.multi_hand_landmarks

    h, w, _ = img.shape

    letra_atual = ""

    if handsPoints:

        for hand in handsPoints:

            x_max = 0
            y_max = 0
            x_min = w
            y_min = h

            for lm in hand.landmark:

                x = int(lm.x * w)
                y = int(lm.y * h)

                x_max = max(x, x_max)
                x_min = min(x, x_min)

                y_max = max(y, y_max)
                y_min = min(y, y_min)

            margem = 40

            cv2.rectangle(
                img,
                (x_min - margem, y_min - margem),
                (x_max + margem, y_max + margem),
                (0, 255, 0),
                2
            )

            try:

                imgCrop = img[
                    y_min - margem:y_max + margem,
                    x_min - margem:x_max + margem
                ]

                imgCrop = cv2.resize(imgCrop, (224, 224))

                imgArray = np.asarray(imgCrop)

                normalized_image_array = (
                    imgArray.astype(np.float32) / 127.0
                ) - 1

                data[0] = normalized_image_array

                prediction = model.predict(data, verbose=0)

                indexVal = np.argmax(prediction)

                confianca = prediction[0][indexVal]

                letra_atual = classes[indexVal]

                # ===== MOSTRAR LETRA =====
                cv2.putText(
                    img,
                    f"{letra_atual} ({confianca:.2f})",
                    (x_min - margem, y_min - margem - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

                # ===== ADICIONAR TEXTO =====
                if confianca > 0.90:

                    if letra_atual != ultima_letra:

                        ultima_letra = letra_atual
                        tempo_letra = time.time()

                    else:

                        tempo_passado = time.time() - tempo_letra

                        if tempo_passado > TEMPO_CONFIRMACAO:

                            texto += letra_atual

                            ultima_letra = ""
                            tempo_letra = time.time()

            except:
                pass

    # ===== MOSTRAR TEXTO =====
    cv2.rectangle(img, (0, 0), (w, 80), (0, 0, 0), -1)

    cv2.putText(
        img,
        texto,
        (20, 55),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (255, 255, 255),
        3
    )

    # ===== AJUDA =====
    cv2.putText(
        img,
        "ESPACO = limpar | ESC = sair",
        (20, h - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.imshow("LIBRAS", img)

    tecla = cv2.waitKey(1)

    # ESC
    if tecla == 27:
        break

    # ESPACO limpa texto
    if tecla == 32:
        texto = ""

cap.release()
cv2.destroyAllWindows()