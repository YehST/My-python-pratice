# coding=utf-8
import cv2
import time
if __name__ == '__main__':
    cv2.namedWindow("camera", 1)
    # 開啟ip攝像頭
    video = "http://admin:admin@172.20.10.13:8081/"
    capture = cv2.VideoCapture(video)
    num = 0
    while True:
        success, img = capture.read()
        cv2.imshow("camera", img)
        # 按鍵處理,注意,焦點應當在攝像頭視窗,不是在終端命令列視窗
        key = cv2.waitKey(10)
        if key == 27:
            # esc鍵退出
            print("esc break...")
            break
        if key == ord(' '):
            # 儲存一張影象
            num = num+1
            filename = "frames_%s.jpg" % num
            cv2.imwrite(filename, img)
    capture.release()
    cv2.destroyWindow("camera")
