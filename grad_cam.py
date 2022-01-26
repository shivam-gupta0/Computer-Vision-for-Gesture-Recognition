import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import cv2


# https://keras.io/examples/vision/grad_cam/
def make_gradcam_heatmap(img_array, model, last_conv_layer_name, pred_index=None):
    grad_model = tf.keras.models.Model(
        [model.inputs], [model.get_layer(last_conv_layer_name).output, model.output]
    )

    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]

    grads = tape.gradient(class_channel, last_conv_layer_output)

    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()


model = load_model("E:\\motorAi\\model_vgg_1\\new_model_vgg.h5", compile=True)
last_conv_layer_name = "block5_conv3"
model.layers[-1].activation = None

original_image = cv2.imread("E:\\motorAi\\testing\\12.jpg")

test_image_ = image.load_img("E:\\motorAi\\testing\\12.jpg", target_size=(224, 224, 3))
test_image = image.img_to_array(test_image_)
test_image = np.expand_dims(test_image, axis=0)

heatmap = make_gradcam_heatmap(test_image, model, last_conv_layer_name)
predictions = model.predict(test_image)
plt.imshow(image)
print(np.argmax(predictions))
plt.matshow(heatmap)
plt.show()
