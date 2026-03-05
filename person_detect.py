from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Run YOLO detection
    results = model(frame)

    person_count = 0   # counter

    for r in results:
        for box in r.boxes:

            cls = int(box.cls[0])          # class id
            conf = float(box.conf[0])      # confidence value

            # detect only person with confidence > 60%
            if cls == 0 and conf > 0.6:

                person_count += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 3)

                cv2.putText(frame, "Person", (x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    # Show people count
    cv2.putText(frame, f"People Count: {person_count}", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

    # Show camera title
    cv2.putText(frame, "AI Surveillance Camera", (20,80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 3)

    cv2.imshow("People Counting System", frame)

    # press ESC to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()