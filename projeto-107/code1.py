import cv2 

xs = []
ys = []

def drawBox(img, bbox):
    x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x,y), ((x+w), (y+h)), (0, 0, 255), 3, 1)
    cx = x + int(w / 2)
    cy = y + int(h / 2)
    cv2.circle(img, (cx, cy), 2, (0, 255, 0), 3)
    xs.append(cx)
    ys.append(cy)

    for i in range(len(xs)-1):
        cv2.circle(img, (xs[i], ys[i]), 2, (0, 255, 255), 1)

video = cv2.VideoCapture("car.mp4")
tracker = cv2.TrackerMIL_create()
returned, frame = video.read() 
bbox = cv2.selectROI("", frame, False)
tracker.init(frame, bbox)

while True:

    ret, frame = video.read()

    success, bbox = tracker.update(frame)
    
    if success:
        drawBox(frame, bbox)
    else:
        cv2.putText(frame, "erro..", (70, 90), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 200), 2)

    if ret:
        cv2.imshow("video", frame)

    if cv2.waitKey(2) == 32:
        break