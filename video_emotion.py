import emo_det as em
import video_to_frames as vf


def emotion_from_video(video_file):
    emotions = {"happy":0,"sad":0,"neutral":0,"fear":0,"angry":0,"face_not_found":0}

    image_paths  = vf.video_frames(video_file)


    for i in range(0,len(image_paths)):
        emotion = em.emotion_image(image_paths[i])
        if emotion=="happy":
            emotions["happy"]+=1
        elif emotion=="sad":
            emotions["sad"]+=1
        elif emotion=="neutral":
            emotions["neutral"]+=1
        elif emotion=="angry":
            emotions["angry"]+=1
        elif emotion=="fear":
            emotions["fear"]+=1
        elif emotion=="No valid image":
            emotions["face_not_found"]+=1

    print(emotions)
    return emotions