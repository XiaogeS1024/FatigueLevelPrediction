import cv2
import pandas as pd
import numpy as np

# 定义视频参数
VIDEO_HEIGHT = 720
VIDEO_WIDTH = 1280
VIDEO_FPS = 10


def main():
    # keypoint文件读取
    kp_file_path = './20201202-869455049224880-1606871191380.csv'
    kp_df = pd.read_csv(kp_file_path)
    for frame_idx in range(1, max(kp_df['frame']) + 1):
        # 逐帧可视化keypoint
        kps = kp_df[kp_df['frame'] == frame_idx].reset_index(drop=True)
        show_bg = np.zeros((VIDEO_HEIGHT, VIDEO_WIDTH, 3))
        for kp_idx in range(len(kps)):
            cv2.circle(show_bg, (kps['x'][kp_idx], kps['y'][kp_idx]), 2, (0, 0, 255), 1)
        cv2.imshow("kp vis", show_bg)
        cv2.waitKey(int(1 / VIDEO_FPS * 1000))


if __name__ == '__main__':
    main()
