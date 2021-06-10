from deepface import DeepFace
import cv2
import os

def emotion_image(image_file):
    image = cv2.imread(image_file)
    try:
        res = DeepFace.analyze(image,actions=["emotion"])
        print(res['dominant_emotion'])
        return  str(res['dominant_emotion'])
    except:
        print("No visible face in frame")
        return "No valid image"

