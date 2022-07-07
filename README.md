# Control-the-Mountain-Car-v0-Gym-env-using-webcam
# Mountain-Car-v0 Gym environment
This environment takes three actions 0,1, and 2.
0 is moving left, 1 is no movement, and two is moving right.
# Dataset
The number of gestures to control the car will be three since there are three different actions in the Mountain-Car-v0 Gym environment.
![12](https://user-images.githubusercontent.com/85798077/177854587-3cf15dc0-ee6c-40e4-bed9-31711f276502.jpg)
![11](https://user-images.githubusercontent.com/85798077/177854922-25ebde1e-da77-4f46-bf1a-229f6f7dbe2e.jpg)
![8](https://user-images.githubusercontent.com/85798077/177855154-71272dc3-c60c-4b71-aa35-d0f4de94780b.jpg)
Pictures are taken from mobile phones and webcams to create a dataset. 
So that number of images can be increased, and different quality and angles can be included in the dataset.
# Training Model
With a small dataset, transfer learning provides an advantage and much better performance because it is already trained on a vast and general enough dataset. 
To select a suitable pre-trained model, I looked for research papers to find out which model works better with gesture detection. And I found out that VGG16 is compatible with gesture detection from this paper.
https://link.springer.com/chapter/10.1007/978-981-16-7118-0_11
Not every model will provide the desired outcome with every dataset when using transfer learning to train models.
# Training / Validation accuracy
![accuracy](https://user-images.githubusercontent.com/85798077/177856119-16d0af3f-9a5e-42c1-91d5-81628ec52a92.png)
# Training /Validation loss
![loss](https://user-images.githubusercontent.com/85798077/177856137-d92cbd26-9358-446d-91ad-f4b42ed79172.png)
# Model Testing
The model was tested using a webcam in real-time for real-time. 
The model was accurate when there was only a gesture visible through the webcam.

https://drive.google.com/file/d/1_Z6X9H3A8wBm5kjjrZqmXt7vjH895D4Y/view?usp=sharing

#  A model visual explanation using the Grad-CAM
Grad-Cam to interpret model prediction because it produces a coarse localization map highlighting the critical regions in the image for predicting the concept.
Which helps to visualize precisely what the model looks at in the picture for a particular class prediction.
Grad-CAM can be used to better understand a model by providing insight into model failure modes.
Below image shows what the model looks at when detecting gesture for Action = 2.
![2022-01-25](https://user-images.githubusercontent.com/85798077/177856926-bda25b78-eca6-4d50-a611-819fab1d85f6.png)

