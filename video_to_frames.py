import cv2
import os


def video_frames(video_file): 
    for i in os.listdir("./images"):
        os.remove("./images/"+i)

    capture = cv2.VideoCapture(video_file)
    cur_frame = 0
    image_list = []
    while(True):
        ret,frame = capture.read()

        im_name = "./images/frame"+str(cur_frame)+".jpg"
        image_list.append(im_name)
        cur_frame+=1
        try:
            cv2.imwrite(im_name,frame)
        except:
            break

    capture.release()
    cv2.destroyAllWindows()

    return image_list