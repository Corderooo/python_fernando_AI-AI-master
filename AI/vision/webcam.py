import cv2

video = cv2.VideoCapture(0)

offset = 0

if video.isOpened   ():                                                                                                                 
    while True:
        ret_v, frame = video.read()
        frame[:, :, :] = frame[:, :, :] + offset
        offset += 1
        
            
        cv2.imshow("Window", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
