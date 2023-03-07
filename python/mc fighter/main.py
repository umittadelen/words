import time
import random
import numpy as np
import cv2
from grabscreen import grab_screen
from directkeys import PressKey, ReleaseKey, W, A, S, D

class MinecraftFighter:
    def __init__(self):
        self.last_time = time.time()
        self.training_data = []
        self.training_data_save_threshold = 1000
        self.model_file_name = "minecraft_fighter_model.npy"
        self.model = self.load_model()
        
    def load_model(self):
        try:
            return np.load(self.model_file_name)
        except:
            return None
        
    def save_model(self):
        if len(self.training_data) >= self.training_data_save_threshold:
            np.save(self.model_file_name, self.model)
            self.training_data = []
    
    def jump(self):
        PressKey(W)
        time.sleep(0.1)
        ReleaseKey(W)
    
    def duck(self):
        PressKey(S)
        time.sleep(0.1)
        ReleaseKey(S)
    
    def left(self):
        PressKey(A)
        time.sleep(0.1)
        ReleaseKey(A)
    
    def right(self):
        PressKey(D)
        time.sleep(0.1)
        ReleaseKey(D)
        
    def process_image(self, image):
        processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
        return processed_image
        
    def get_keys(self):
        keys = []
        if random.random() < 0.5:
            keys.append("left")
        else:
            keys.append("right")
        if random.random() < 0.5:
            keys.append("jump")
        else:
            keys.append("duck")
        return keys
        
    def train(self):
        while(True):
            screen = grab_screen(region=(0,40,800,640))
            last_time = time.time()
            processed_screen = self.process_image(screen)
            keys = self.get_keys()
            self.training_data.append([processed_screen, keys])
            if len(self.training_data) >= self.training_data_save_threshold:
                self.model = self.train_model()
                self.save_model()
            print("Frame took {} seconds".format(time.time()-last_time))
            cv2.imshow('window', processed_screen)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
                
    def train_model(self):
        X = np.array([i[0] for i in self.training_data]).reshape(-1, 160, 120, 1)
        y = np.array([i[1] for i in self.training_data])
        model = create_model()
        model.fit(X, y, epochs=5)
        return model
    
    def create_model(self):
        model = Sequential()
        model.add(Conv2D(32, (3, 3), input_shape=(160, 120, 1)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Flatten())
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(2))
        model.add(Activation('softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model
    
    def play(self):
        while(True):
            screen = grab_screen(region=(0,40,800,640))
            processed_screen = self.process_image(screen)
            if self.model is not None:
                prediction = self.model.predict(processed_screen.reshape(-1, 160, 120, 1))[0]
                if np.argmax(prediction) == 0:
                    self.left()
                else:
                    self.right()
                if prediction[1] > 0.7:
                    self.jump()
                elif prediction[0] > 0.7:
                    self.duck()
                print("Frame took {} seconds".format(time.time()-self.last_time))
                self.last_time = time.time()
                cv2.imshow('window', processed_screen)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
