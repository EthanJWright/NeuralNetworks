# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator

EPOCHS = 20
TRAINING_IMAGES = 410
TEST_IMAGES = 102

classifier = Sequential()

classifier.add(Conv2D(32, (3,3), input_shape=(64, 64, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))
classifier.add(Flatten())
#Fully Connected Layers ( neurons that will be voting for the end result ) ;q

classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

train_datagen = ImageDataGenerator(rescale = 1./255,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory('training_set',
        target_size = (64, 64),
        batch_size = 32,
        class_mode = 'binary')

test_set = test_datagen.flow_from_directory('test_set',
        target_size = (64, 64),
        batch_size = 32,
        class_mode = 'binary')

classifier.fit_generator(training_set, 
        steps_per_epoch = TRAINING_IMAGES, 
        epochs = EPOCHS, 
        validation_data = test_set, 
        validation_steps = TEST_IMAGES)

classifier.save("small_puddles_classification.h5")

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('/home/god/other_test.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'puddles'
else:
    prediction = 'not puddles'

