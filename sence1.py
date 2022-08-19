from re import I
import cv2
import numpy as np

INFILE = "C:\\Users\\B20735\\Desktop\\博士研究\\日本トップテン\\チャンネルNO11\\10.mp4" # movie file
# C:\Users\B20735\Desktop\博士研究\日本トップテン\チャンネルNO1
THRESH = 55.55679398148148 # threshold 

ESC_KEY = 27     # Escキー
INTERVAL= 1      # 待ち時間

WINNAME = "test"
cv2.namedWindow(WINNAME)

class MovieIter(object): #動画のフレームを返すイテレータ
    def __init__(self, moviefile, size=None, inter_method=cv2.INTER_AREA):
        #TODO: check if moviefile exists
        self.org = cv2.VideoCapture(moviefile)
        self.framecnt = 0
        self.size = size #frame size
        self.inter_method = inter_method
    def __iter__(self):
        return self
    def __next__(self):
        self.end_flg, self.frame = self.org.read()
        if not self.end_flg: # end of the movie
            raise StopIteration()
        self.framecnt+=1
        if self.size: # resize when size is specified
            self.frame = cv2.resize(self.frame, self.size, interpolation=self.inter_method)
        return self.frame
    def __del__(self): # anyway it works without destructor 
        self.org.release()

def MSE(pic): # mean square error
    return np.mean(np.square(pic))
    
def MAE(pic): # mean absolute error
    return np.mean(np.abs(pic))

def main():
    picsize = (64, 36)
    data =[]
    frame_cnt = 0
    frame_ultima = np.zeros((*picsize[::-1], 3)) # create empty image
    
    for frame in MovieIter(INFILE, None):
        frame_penult = frame_ultima
        frame_ultima = cv2.resize(frame, picsize, interpolation=cv2.INTER_AREA) #指定サイズに縮小
        
        cv2.imshow(WINNAME, frame)
        key = cv2.waitKey(1) # quit when esc-key pressed
        if key == ESC_KEY:
            break
        
        #差分画像作成
        diff = frame_ultima.astype(np.int) - frame_penult.astype(np.int)

        

        if MAE(diff)>=THRESH: #閾値よりMAEが大きい場合、カットと判定
            #print("Cut detected!: frame {}".format(frame_cnt))
            #print([frame_cnt])
            #print([frame_cnt])
            data.append(frame_cnt)      
             
        
   
        
        frame_cnt+=1
    

    global i
    i = len(data)
    print("この動画のシーンの数は{}です。".format(i))
    
                        

if __name__ == "__main__":
    main()


# if __name__ == '__main__':
#     cap = cv2.VideoCapture("Pvideo.mp4")                  # 動画を読み込む
#     video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT) # フレーム数を取得する
#     video_fps = cap.get(cv2.CAP_PROP_FPS)                 # フレームレートを取得する
#     video_len_sec = video_frame_count / video_fps    
    
#     j = int(video_len_sec)     # 長さ（秒）を計算する
#     #print(video_len_sec)  
#     print("この動画長さは{}秒です。".format(j))
#     print('---------------------------------')
#     jikan = j /i
print("一つのシーンの平均時間は{}秒です。".format(jikan))


