import cv2
from cvzone.FaceDetectionModule import FaceDetector  # cvzone 라이브러리에서 얼굴 감지 모듈 가져오기
from cvzone.SerialModule import SerialObject  # cvzone 라이브러리에서 시리얼 통신 모듈 가져오기

# 웹캠에서 비디오를 가져오기 위한 VideoCapture 객체 생성
cap = cv2.VideoCapture(0)

# 얼굴 감지를 위한 FaceDetector 객체 생성
detector = FaceDetector()

# 아두이노와의 시리얼 통신을 위한 SerialObject 객체 생성
arduino = SerialObject("/dev/cu.usbmodem1301")  # 아두이노의 포트에 따라 적절히 변경해야 함

while True:
    # 웹캠에서 프레임을 읽어옴
    success, img = cap.read()

    # 이미지에서 얼굴을 감지하고 감지된 얼굴 주위에 바운딩 박스를 그림
    img, bboxs = detector.findFaces(img)

    # 얼굴이 감지되면 아두이노로 데이터를 보냄
    if bboxs:
        arduino.sendData([1])  # 얼굴이 감지되면 아두이노에 '1'을 보냄
    else:
        arduino.sendData([0])  # 얼굴이 감지되지 않으면 아두이노에 '0'을 보냄

    # 화면에 웹캠 영상을 표시
    cv2.imshow("cam", img)

    cv2.waitKey(1)

