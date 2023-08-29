import time
import cv2
import webbrowser
import psutil

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

detector = cv2.QRCodeDetector()
last_decoded_text = ""
link_opened = False
link_opened_time = 0
delay_between_links = 10 

while cap.isOpened():
    success, img = cap.read()

    start = time.perf_counter()

    decodedText, points, _ = detector.detectAndDecode(img)
    if len(decodedText) == 0 and points is not None:
        x1 = points[0][0][0]
        y1 = points[0][0][1]
        x2 = points[0][2][0]
        y2 = points[0][2][1]

        x_center = (x2 - x1) / 2 + x1
        y_center = (y2 - y1) / 2 + y1

        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.circle(img, (int(x_center), int(y_center)), 3, (0, 0, 255), 2)

    if decodedText != last_decoded_text:
        last_decoded_text = decodedText
        link_opened = False

    current_time = time.time()
    if len(decodedText) > 0 and not link_opened and (current_time - link_opened_time) > delay_between_links:

        browser_processes = [proc.name() for proc in psutil.process_iter(attrs=['name'])]
        browser_name = "chrome.exe"
        if browser_name in browser_processes:
            webbrowser.open(decodedText)
            link_opened = True
            link_opened_time = current_time

    end = time.perf_counter()
    total_time = end - start
    fps = 1 / total_time

    cv2.putText(img, f"FPS: {int(fps)}", (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0))
    cv2.imshow('img', img)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
