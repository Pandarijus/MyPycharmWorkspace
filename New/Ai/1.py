from matplotlib import pyplot as plt
import tensorflow as tf
import numpy as np
import os


model = tf.keras.models.load_model('mnist_model.h5')
model.e