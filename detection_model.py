import glob
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.layers import Dense, Flatten
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator


# Reference
# https://keras.io/api/applications/vgg/#vgg16-function
IMAGE_SIZE = [224, 224]
new_model = tf.keras.applications.VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)
for layer in new_model.layers:
    layer.trainable = False

train_path = 'E:\\motorAi\\dataset\\train'
valid_path = 'E:\\motorAi\\dataset\\test'

Label = glob.glob('E:\\motorAi\\dataset\\train/*')

x = Flatten()(new_model.output)
prediction = Dense(len(Label), activation='softmax')(x)
model = Model(inputs=new_model.input, outputs=prediction)

# Reference
# https://keras.io/api/losses/probabilistic_losses/#categoricalcrossentropy-class
model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              metrics=['accuracy'])
model.summary()

# Reference
# https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator
train_data = ImageDataGenerator(rescale=1. / 255, zoom_range=0.2, horizontal_flip=True)

test_data = ImageDataGenerator(rescale=1. / 255)

training_set = train_data.flow_from_directory('E:\\motorAi\\dataset\\train', target_size=(224, 224), batch_size=32,
                                              class_mode='categorical')

test_set = test_data.flow_from_directory('E:\\motorAi\\dataset\\test', target_size=(224, 224), batch_size=32,
                                         class_mode='categorical')

# Reference
# https://www.tensorflow.org/tutorials/images/transfer_learning
M = model.fit(training_set, validation_data=test_set, epochs=30,
              validation_steps=len(test_set))

plt.plot(M.history['loss'], label='training loss')
plt.plot(M.history['val_loss'], label='validation loss')
plt.legend()
plt.show()
plt.savefig('LossVal_loss')

plt.plot(M.history['accuracy'], label='training accuracy')
plt.plot(M.history['val_accuracy'], label='validation accuracy')
plt.legend()
plt.show()
plt.savefig('AccVal_acc')

model.save('new_model_vgg.h5')