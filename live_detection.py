import cv2
import numpy as np
from keras.models import load_model
from PIL import Image


model = load_model("E:\\motorAi\\model_vgg_1\\new_model_vgg.h5", compile=True)

web_cam = cv2.VideoCapture(0)
while web_cam.isOpened():
    _, frame = web_cam.read()
    cv2.imshow('Image', frame)
    test_image = Image.fromarray(frame, 'RGB')
    test_image = test_image.resize((224, 224))
    test_image = np.array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    predictions = model.predict(test_image)

    print(predictions)
    classes = np.argmax(predictions)
    print(classes)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
web_cam.release()
cv2.destroyAllWindows()
