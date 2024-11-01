import cv2
from cvzone.HandTrackingModule import HandDetector
import time
from pynput.keyboard import Controller
import cvzone

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()

cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=1)

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", " "]]
Text = ""
Keyboard = Controller()


def draw(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[0]), 20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img


class Button:
    def __init__(self, pos, text, size=[85,85]):
        self.pos = pos
        self.text = text
        self.size = size


buttonList = []

for i in range(len(keys)):
    for x, key in enumerate(keys[i]):
        buttonList.append(Button([100 * x + 50, 100 * i + 50], key))

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    img = draw(img, buttonList)  # Always draw buttons

    if lmList and len(lmList) > 8:  # Ensure lmList is valid
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                cv2.rectangle(img, button.pos, (x + w, y + h), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                l, _, _ = detector.findDistance(8, 12, img, draw=False)

                # When we click
                if l < 50:
                    Keyboard.press(button.text)
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    Text += button.text
                    time.sleep(0.75)  # Consider reducing or removing

    cv2.rectangle(img, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, Text, (60, 425), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
