import os
import cv2
import h5py
import numpy as np
import glob

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images

def save_to_h5(images, h5_filename):
    with h5py.File(h5_filename, 'w') as h5file:
        h5file.create_dataset('images', data=np.array(images))

if __name__ == "__main__":
    # 이미지가 저장된 폴더 경로
    folder_path = 'path/to/your/image/folder'

    # h5 파일로 저장할 경로 및 파일명
    h5_filename = 'output.h5'

    # 이미지 불러오기
    images = load_images_from_folder(folder_path)

    # h5 파일로 저장
    save_to_h5(images, h5_filename)

    print(f"이미지들이 {h5_filename} 파일로 저장되었습니다.")
