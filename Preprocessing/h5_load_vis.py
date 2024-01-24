import h5py
import cv2
import numpy as np

# h5 파일 load 하기
def load_file(file_path):
    hdf5 = h5py.File(file_path, 'r')
    ct_data = np.asarray(hdf5['ct'])
    x_ray1 = np.asarray(hdf5['xray1'])
    x_ray2 = np.asarray(hdf5['xray2'])
    x_ray1 = np.expand_dims(x_ray1, axis=-1)  # 채널 차원 추가
    x_ray2 = np.expand_dims(x_ray2, axis=-1)  # 채널 차원 추가
    hdf5.close()
    return ct_data, x_ray1, x_ray2

# 이미지 정규화
def normalize_image(image):
    return cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')

# 이미지 시각화
def visualize_images(ct_data, x_ray1, x_ray2):
    # 첫 번째 CT 슬라이스를 시각화
    # 모든 슬라이스 시각화
    for i in range(len(ct_data)):
        ct_image = ct_data[i]  # 예제로 첫 번째 슬라이스 사용
        ct_image_normalized = normalize_image(ct_image)
        cv2.imshow('CT Image', ct_image_normalized)

    # X-ray 이미지 시각화
    x_ray1_normalized = normalize_image(x_ray1)
    x_ray2_normalized = normalize_image(x_ray2)
    cv2.imshow('X-ray 1', x_ray1_normalized)
    cv2.imshow('X-ray 2', x_ray2_normalized)

    cv2.waitKey(0)  # 창이 닫히지 않도록 기다림
    cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기

if __name__ == "__main__":
    # h5 파일 경로
    filename = "ct_xray_data.h5"
    ct_data, x_ray1, x_ray2 = load_file(filename)

    # 시각화
    visualize_images(ct_data, x_ray1, x_ray2)
