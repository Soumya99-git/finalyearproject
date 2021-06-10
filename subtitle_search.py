import pysrt
import video_cutter
import model_prediction

def sub_time_stamp(sub_name,dialogue):
    subs = pysrt.open(sub_name)
    s = dialogue
    for i in range(len(subs)):
        x = subs[i].text
        if s.lower()==x.lower():
            print("Found the dialogue")
            start = str(subs[i].start)[:-4]
            end = str(subs[i].end)[:-4]
            s_or = []
            s_or.append(int(start[0:2]))
            s_or.append(int(start[3:5]))
            s_or.append(int(start[6:8]))
            e_or = []
            e_or.append(int(end[0:2]))
            e_or.append(int(end[3:5]))
            e_or.append(int(end[6:8]))

            print("Dialogue start at: "+start)
            print("Dialogue end at: "+end)
            if i==0:
                end = str(subs[i+1].end)[:-4]
            elif(i==len(subs)-1):
                start = str(subs[i-1].start)[:-4]
            else:
                start = str(subs[i-1].start)[:-4]
                end = str(subs[i+1].end)[:-4]
                
            s = []
            s.append(int(start[0:2]))
            s.append(int(start[3:5]))
            s.append(int(start[6:8]))
            e = []
            e.append(int(end[0:2]))
            e.append(int(end[3:5]))
            e.append(int(end[6:8]))

            return s_or,e_or,s,e
        else:
            continue
    print("Subtitle not found!!!")
    return -1,-1

if __name__=="__main__":

    no_lines = int(input("Enter number of lines in dialogue: "))
    if no_lines==1:
        dialogue = input("Enter dialogue: ")
    else:
        dialogue= ""
        print("Enter lines of dialogue")
        for i in range(no_lines):
            dialogue+=input()+"\n"
        dialogue = dialogue[:-1]

    srt = "subtitle.srt"

    while(True):
        print("1: Emotional analysis from video")
        print("2: Emotional analysis from text")
        print("0: Exit")
        
        ch =int(input())
        if ch==1:
            s_or,e_or,s,e = sub_time_stamp(srt,dialogue)
            video_cutter.video_cut(s_or,e_or,s,e,ch)
            print("Emotion from Text")
            print(model_prediction.emotion_from_text(dialogue))
        elif ch==2:
            s_or,e_or,s,e = sub_time_stamp(srt,dialogue)
            video_cutter.video_cut(s_or,e_or,s,e,ch)
        elif ch==3:
            break
        else:
            print("Wrong Choice")