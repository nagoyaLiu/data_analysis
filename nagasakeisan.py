import cv2

if __name__ == '__main__':
    cap = cv2.VideoCapture("Pvideo.mp4")                  # 動画を読み込む
    video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT) # フレーム数を取得する
    video_fps = cap.get(cv2.CAP_PROP_FPS)                 # フレームレートを取得する
    video_len_sec = video_frame_count / video_fps    
    
    i = int(video_len_sec)     # 長さ（秒）を計算する
    print(video_len_sec)  
    print(i)
