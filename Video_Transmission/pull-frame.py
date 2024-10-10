import cv2

vidcap = cv2.VideoCapture("test.mp4")
start = 13
frame_delay = 13
success, image = vidcap.read()
count = 1
while success:
    if (count == start) or ((count - start) % frame_delay == 0 and count > start):
        cv2.imwrite("detected/frame%d.png" % count, image)
    success, image = vidcap.read()
    count += 1
