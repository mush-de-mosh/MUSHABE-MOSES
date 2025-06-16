#import required libraries
#Numpy
#tesaflow
#matplotlib
import os
import numpy as np # type: ignore
import tensorflow as tf # type: ignore #building and training deep learning module
from tensorflow import keras  # type: ignore #high level API for neural networks
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # type: ignore #Augumentation
from tensorflow.keras.models import Sequential  # Linear stack of neural network layers
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout  # CNN layers
from tensorflow.keras.optimizers import Adam  # Optimizer for training
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping  # Training callbacks
import matplotlib.pyplot as plt  # For visualization

#set random seeds for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

#Define the constant value
IMAGE_SIZE = (256,256)
BATCH_SIZE = 32 # number of images process in a batch
EPOCHUS = 20 # number of full passes throughout the dataset
NUM_CLASSES = 2 #Number of output classes for crops (diseases, healthy)
ANIMAL_CLASSES = 3 #number of animal class

#Define the dataset director and the model save paths
DATASET_DIR = "Machine_learning" #directory conatining training dataset
MODEL_PATH = "mush_model.h5"
