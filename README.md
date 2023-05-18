# Computer Vision for Gesture Recognition <br>
Welcome to my Computer Vision for Gesture Recognition project! This repository showcases my expertise in computer vision and artificial intelligence, specifically in the domain of gesture recognition using deep learning and image processing techniques. Through a comprehensive set of components, including data collection, model training, live detection, and visualization using Grad-CAM, this project demonstrates my skills as a proficient machine learning and computer vision engineer.<br>

# **Project Highlights**<br>
**Gesture Recognition in MountainCar-v0:** Experience the power of computer vision in action! The control_mountain_car.py script demonstrates real-time gesture recognition within the popular OpenAI Gym's MountainCar-v0 environment. By capturing frames from a webcam and leveraging a pre-trained VGG16 model, the script intelligently predicts gestures to control the car's actions.<br>

**Dataset Creation:** Building a robust dataset is vital for training accurate gesture recognition models. With the create_dataset.py script, easily create your own dataset by capturing images from a webcam. Set the desired dataset path and number of images, and the script automatically saves the images for further processing.<br>

**Detection Model Training:** Utilizing the power of deep learning, the detection_model.py script trains a VGG16-based model for gesture recognition. By leveraging transfer learning and fine-tuning techniques, the model achieves high accuracy on the collected dataset. Visualize the training progress, including loss and accuracy curves, to gain insights into the model's performance.<br>

**Grad-CAM Visualization:** Dive deeper into the inner workings of the gesture recognition model with the grad_cam.py script. Implement the Grad-CAM technique to visualize the model's attention on input images. Gain valuable insights into which regions of the image contribute most to the model's predictions, enhancing interpretability and understanding.<br>

**Live Gesture Recognition:** Experience real-time gesture recognition with the live_detection.py script. By leveraging the trained model, the script captures frames from a webcam, predicts gestures in real-time, and displays the results on the screen. Witness the model's ability to detect and classify gestures on the fly.<br><br>





# **Dataset**<br>
Pictures captured from mobile phones and webcams were used to create a diverse and extensive dataset for gesture recognition. This approach allowed for an increased number of images and inclusion of different qualities and angles, enhancing the dataset's representativeness.
![3](https://user-images.githubusercontent.com/85798077/177858459-6ae88fd7-0d0d-484b-af4b-74da866a6c45.jpg)
![2](https://user-images.githubusercontent.com/85798077/177858509-3df970f4-d911-4e33-9f52-4c53f4851146.jpg)
![1](https://user-images.githubusercontent.com/85798077/177858549-a1c66ec5-3596-4d87-ba7c-752561c43a41.jpg)

# Training Model<br>
With a small dataset, transfer learning provides an advantage and much better performance because it is already trained on a vast and general enough dataset. <br>

For training the gesture recognition model, transfer learning proved advantageous due to the small dataset size. Leveraging pre-trained models that were already trained on large and diverse datasets yields better performance. After researching various papers, I identified VGG16 as a compatible model for gesture detection, as described in the paper link to paper. Not every pre-trained model may yield desired results for every dataset when utilizing transfer learning.<br>
https://link.springer.com/chapter/10.1007/978-981-16-7118-0_11<br>
During the training process, the accuracy and loss of the model were monitored to assess its performance. The following graphs depict the training/validation accuracy and loss:<br>

# Training / Validation accuracy<br>
![accuracy](https://user-images.githubusercontent.com/85798077/177856119-16d0af3f-9a5e-42c1-91d5-81628ec52a92.png)<br>
# Training /Validation loss<br>
![loss](https://user-images.githubusercontent.com/85798077/177856137-d92cbd26-9358-446d-91ad-f4b42ed79172.png)<br>
# Model Testing<br>
To test the model, a webcam was utilized for real-time gesture recognition. The model demonstrated high accuracy when detecting gestures visible through the webcam.<br>

To provide a visual explanation of the model's predictions, Grad-CAM was employed. Grad-CAM generates a coarse localization map highlighting the crucial regions in an image that contribute to the model's concept prediction. This technique enables a precise visualization of the model's focus for a specific class prediction. By using Grad-CAM, we gain insight into the model's decision-making process and understand its failure modes. The image below illustrates the regions of interest for Action = 2:<br>



![2022-01-25](https://user-images.githubusercontent.com/85798077/177856926-bda25b78-eca6-4d50-a611-819fab1d85f6.png)

For a more comprehensive understanding of the project, including the trained model and additional details, please refer to the Google Drive link.

https://drive.google.com/file/d/1_Z6X9H3A8wBm5kjjrZqmXt7vjH895D4Y/view?usp=sharing<br>
By demonstrating proficiency in capturing diverse datasets, training models using transfer learning, conducting real-time testing, and providing visual explanations with Grad-CAM, this project showcases my expertise as a skilled machine learning and computer vision engineer.


# **Usage and Customization**<br>
To utilize this project effectively, follow the steps below:<br>

Ensure all dependencies are installed by running:<br>

Explore each component's functionality and customize it to fit your specific needs. Modify paths, adjust hyperparameters, and experiment with different architectures to further enhance the project.<br>

Run the provided scripts and witness the results firsthand. Analyze the accuracy of the gesture recognition model, observe Grad-CAM visualizations, and interact with the MountainCar-v0 environment using hand gestures.<br>


# **Conclusion**
This GitHub repository serves as a testament to my skills and expertise as a machine learning and computer vision engineer. By leveraging deep learning models, image processing techniques, and real-time detection, this project demonstrates my ability to develop advanced computer vision solutions. I believe this project showcases the range of my skills and would be an excellent demonstration of my capabilities to potential recruiters in the field of computer vision and artificial intelligence.<br>
