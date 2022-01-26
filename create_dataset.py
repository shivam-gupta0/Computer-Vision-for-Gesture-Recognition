import cv2
import time
import os


def create_dataset(path, total_images):
    for image in range(total_images):
        web_cam = cv2.VideoCapture(0)
        time.sleep(2)
        _, frame = web_cam.read()
        image_name = os.path.join(dataset_path, '{}.jpg'.format(str(image)))
        cv2.imwrite(image_name, frame)
        cv2.imshow('Image', frame)
        time.sleep(3)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            web_cam.release()
        if image == total_images:
            web_cam.release()


dataset_path = "E:\\motorAi\\dataset"
total_images = 30
create_dataset(dataset_path, total_images)
