import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets,layers,models

# get and prepare data
(training_img, training_lable), (testing_img, testing_lable) = datasets.cifar10.load_data()
training_img, testing_img = training_img/255, testing_img/255

class_name = ['Plane','Car','Bird','Cat','Deer','Dog','Frog','Horse','Ship','Truck']

training_img = training_img[:20000] # reducing data. More data -> better result
training_lable = training_lable[:20000]
testing_img = testing_img[:4000]
testing_lable = testing_lable[:4000]

model = models.load_model('image_classifier.model')

img = cv.imread('horse.jpeg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img, cmap=plt.cm.binary)

prediction = model.predict(np.array([img]) / 255)

index = np.argmax(prediction)
print(f'Prediction is {class_name[index]}')
plt.show()
