import cv2
import numpy as np
from pyzbar.pyzbar import decode


def decoder(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = decode(gray_img)

    for obj in barcodes:
        points = obj.polygon
        (x, y, w, h) = obj.rect

        pts = np.array(points, np.int32).reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        text = f"{barcodeData} ({barcodeType})"

        cv2.putText(
            image,
            text,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2
        )

        print("Barcode:", barcodeData, "| Type:", barcodeType)

    return image


choice = int(input("1. Scan via image\n2. Scan via WebCam\nChoice: "))

# ---------------- WEBCAM ----------------
if choice == 2:
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("❌ Webcam not accessible")
        exit()

    print("✅ Webcam started. Press Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = decoder(frame)
        cv2.imshow("QR Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# ---------------- IMAGE ----------------
else:
    img_path = input("Enter Image path: ").strip()
    img = cv2.imread(img_path)

    if img is None:
        print("❌ Image not found")
        exit()

    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        print("✅ QR Code Encoded Data:", data)
    else:
        print("❌ No QR code found")
