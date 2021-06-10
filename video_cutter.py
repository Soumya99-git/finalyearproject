from moviepy.editor import VideoFileClip
import video_emotion as ve

def video_cut(start_or,end_or,start,end,ch):
    start = tuple(start)
    end = tuple(end)
    start_or = tuple(start_or)
    end_or = tuple(end_or)
    
    video = VideoFileClip("HPPS.mp4")
    new_video = video.subclip(t_start=start,t_end=end)
    new_video_test = video.subclip(t_start = start_or,t_end=end_or)
    new_video.write_videofile("video_show.mp4")
    new_video_test.write_videofile("video_test.mp4")
    if ch==2:
        ve.emotion_from_video("video_test.mp4")