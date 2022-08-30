import cv2 as cv

def detect_qr(frame):
    detectQR = cv.QRCodeDetector()
    ret, _ = detectQR.detect(frame)

    return ret

def read_qr(img):
    detect = cv.QRCodeDetector()
    value, points, _ = detect.detectAndDecode(img)

    if value == '':
        return None

    return value 

def main():
    while True:
        vid = cv.VideoCapture(0)
        ret, frame = vid.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        if detect_qr(frame):
            qr_value = read_qr(frame)

            if qr_value is None: continue
            else: print(qr_value)
            break
    vid.release()


main()