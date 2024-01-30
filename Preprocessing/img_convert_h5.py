import os
import cv2
import h5py
import re
import numpy as np
import glob

def resize_image(image, size=(256, 256)):
    return cv2.resize(image, size, interpolation=cv2.INTER_AREA)

def extract_number(file_name):
    # 파일명에서 숫자를 추출하는 함수
    match = re.search(r'(\d+)', file_name)
    return int(match.group()) if match else float('inf')

def load_images_from_folder(folder):
    images = {"ct": [], "xray1": '', "xray2": ''}
    
    # 정렬 실행
    files = os.listdir(folder)
    files.sort(key=extract_number)    
    
    for filename in files:
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        
        if img is None:
            continue

        # 이미지 크기가 256x256이 아닐 경우 리사이징
        resized_img = resize_image(img)
        
        if "ct" in filename:
            images["ct"].append(resized_img)
        elif "front" in filename:
            images["xray1"] = resized_img
        elif "side" in filename:
            images["xray2"] = resized_img

    return images

def save_to_h5(images, h5_filename):
    with h5py.File(h5_filename, 'w') as h5file:
        for key in images:
            h5file.create_dataset(key, data=np.array(images[key]))

def process_folders(parent_folder, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    subfolders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]
    for folder in subfolders:
        images = load_images_from_folder(folder)
        save_folder = os.path.join(output_dir, os.path.basename(folder))
        h5_filename = os.path.join(save_folder, 'ct_xray_data.h5')
        os.makedirs(save_folder, exist_ok=True)

        save_to_h5(images, h5_filename)
        print(f"{folder}의 이미지들이 {h5_filename} 파일로 저장되었습니다.")

if __name__ == "__main__":
    parent_folder = '../3DGAN/data/custom-dataset'
    output_dir = '../3DGAN/data/dataset'
    process_folders(parent_folder, output_dir)
