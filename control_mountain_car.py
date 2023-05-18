import gym
import cv2
import numpy as np
from keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
from PIL import Image

gesture_detection_model = load_model("model_vgg.h5", compile=True)


def action_input(image):
    input_image = Image.fromarray(image, 'RGB')
    input_image = input_image.resize((224, 224))
    input_image = np.array(input_image)
    input_image = np.expand_dims(input_image, axis=0)
    input_image = preprocess_input(input_image)
    result = gesture_detection_model.predict(input_image)

    return np.argmax(result)


web_cam = cv2.VideoCapture(0)

while web_cam.isOpened():
    env = gym.make('MountainCar-v0')
    # https://gym.openai.com/docs/
    for i_episode in range(20):
        observation = env.reset()
        for t in range(10000):
            _, frame = web_cam.read()
            cv2.imshow('Image', frame)
            env.render()
            action = action_input(frame)
            observation, reward, done, info = env.step(action)
            print(action, observation)
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break
    web_cam.release()
    cv2.destroyAllWindows()
    env.close()
