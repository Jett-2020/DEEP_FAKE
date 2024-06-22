import numpy as np
import cv2
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D, BatchNormalization, Dropout, LeakyReLU
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Model
from tensorflow.keras import backend as K

# Model configuration
image_dimensions = {'height': 256, 'width': 256, 'channels': 3}

class Classifier:
    def __init__(self):
        self.model = 0
    
    def predict(self, x):
        return self.model.predict(x)
    
    def fit(self, x, y):
        return self.model.train_on_batch(x, y)
    
    def get_accuracy(self, x, y):
        return self.model.test_on_batch(x, y)
    
    def load(self, path):
        self.model.load_weights(path)

class model(Classifier):
    def __init__(self, learning_rate=0.001):
        self.model = self.init_model()
        optimizer = Adam(learning_rate=0.001)
        self.model.compile(optimizer=optimizer,
                           loss='mean_squared_error',
                           metrics=['accuracy'])
    
    def init_model(self): 
        x = Input(shape=(image_dimensions['height'],
                         image_dimensions['width'],
                         image_dimensions['channels']))
        
        x1 = Conv2D(8, (3, 3), padding='same', activation='relu', name='conv2d')(x)
        x1 = BatchNormalization(name='batch_normalization')(x1)
        x1 = MaxPooling2D(pool_size=(2, 2), padding='same', name='max_pooling2d')(x1)
        
        x2 = Conv2D(8, (5, 5), padding='same', activation='relu', name='conv2d_1')(x1)
        x2 = BatchNormalization(name='batch_normalization_1')(x2)
        x2 = MaxPooling2D(pool_size=(2, 2), padding='same', name='max_pooling2d_1')(x2)
        
        x3 = Conv2D(16, (5, 5), padding='same', activation='relu', name='conv2d_2')(x2)
        x3 = BatchNormalization(name='batch_normalization_2')(x3)
        x3 = MaxPooling2D(pool_size=(2, 2), padding='same', name='max_pooling2d_2')(x3)
        
        x4 = Conv2D(16, (5, 5), padding='same', activation='relu', name='conv2d_3')(x3)
        x4 = BatchNormalization(name='batch_normalization_3')(x4)
        x4 = MaxPooling2D(pool_size=(4, 4), padding='same', name='max_pooling2d_3')(x4)
        
        y = Flatten(name='flatten')(x4)
        y = Dropout(0.5, name='dropout')(y)
        y = Dense(16, name='dense')(y)
        y = LeakyReLU(alpha=0.1, name='leaky_re_lu')(y)
        y = Dropout(0.5, name='dropout_1')(y)
        y = Dense(1, activation='sigmoid', name='dense_1')(y)

        return Model(inputs=x, outputs=y)

# Initialize and load the model
df_model = model()
df_model.load('weights/Meso4_DF.h5')

def preprocess_frame(frame):
    frame = cv2.resize(frame, (image_dimensions['height'], image_dimensions['width']))
    frame = frame.astype('float32') / 255.0
    frame = np.expand_dims(frame, axis=0)
    return frame

def analyze_video(video_path, model, threshold=0.5):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    deepfake_score_sum = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        processed_frame = preprocess_frame(frame)
        prediction = model.predict(processed_frame)[0][0]
        deepfake_score_sum += prediction
        frame_count += 1

    cap.release()
    
    if frame_count == 0:
        raise ValueError("No frames to analyze in the video.")

    average_score = deepfake_score_sum / frame_count
    #print(f"Average Deepfake Score: {average_score:.2f}")

    if average_score > threshold:
        return "The video is likely a deepfake."
    else:
        return "The video is likely real."

# Example usage
video_path = 'fake.mp4'

#def send():
#    analyze_video(video_path, df_model)

def send():
    try:
        result_message = analyze_video(video_path, df_model)
        return result_message
    except Exception as e:
        return str(e)
