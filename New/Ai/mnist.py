import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
shouldTrain = False

tf.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

if shouldTrain:
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.softmax))
    model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=5)
    print(model.evaluate(x_test, y_test))
    model.save('mnist.h5')
else:
    model = tf.keras.models.load_model('mnist.h5')
    #print(model.evaluate(x_test, y_test))
    plt.imshow(x_test[0], cmap='gray')
    plt.show()
#    print(model.predict(x_test[0:1]))
    print(np.argmax(model.predict(x_test[0:1])))
