import os
import cv2
import argparse
import numpy as np

def pick_imgs(target_dir):
    # 디렉토리 내의 모든 파일을 읽어옴
    all_files = sorted([f for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))])
    
    # 이미지 파일만 선택
    img_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # 전체 이미지 수
    total_images = len(img_files)

    # 이미지를 선택할 간격 계산
    interval = total_images / 256

    selected_imgs = []
    current = 0

    while len(selected_imgs) < 256 and current < total_images:
        selected_imgs.append(img_files[int(current)])
        current += interval

    assert len(selected_imgs) == 256
    return selected_imgs

def delete_other_imgs(target_dir, img_list):
    # 디렉토리 내의 모든 파일
    all_files = [f for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))]

    # 리스트에 없는 이미지 삭제
    for file in all_files:
        if file not in img_list:
            os.remove(os.path.join(target_dir, file))

if __name__ == "__main__":
    # target directory
    target_dir = 'C:\\Users\\taesh\\Dropbox\\006_researchdata\\0007_LCT\\dataset\\230910-00183785'

    # 256개의 이미지를 고르기
    img_list = pick_imgs(target_dir)

    # img_list에 없는 나머지 이미지 삭제
    delete_other_imgs(target_dir, img_list)
