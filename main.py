# 바코드 리더를 활용한 도서 판매 관리

import cv2
import pyzbar.pyzbar

cap = cv2.VideoCapture(0)

running = True
while running:
    success, frame = cap.read()

    if success:
        for code in pyzbar.decode(frame):
            my_code = code.data.decode('utf-8')
            print('CODE: ', my_code)

        cv2.imshow('cam', frame)

        key = cv2.waitKey(1)
        if key == 27:
            running = False

cap.release()
cv2.destroyAllWindows()
