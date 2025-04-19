import cv2

vid_capture = cv2.VideoCapture(0)

if vid_capture.isOpened() == False:
    print("Error opening video")

else:
    fps = vid_capture.get(5)
    print("fps: ", fps)

frame_count = vid_capture.get(7)
print('Frame count : ', frame_count)

while(vid_capture.isOpened()):

    ret, frame = vid_capture.read()
    if ret == True:
        cv2.imshow('Frame', frame)

        key = cv2.waitKey(1000)

        if key == ord('q'):
            break

vid_capture.release()
cv2.destroyAllWindows()