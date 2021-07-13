import rawpy 
import matplotlib.pyplot as plt
import fastbook 
from fastai import * 
from PIL import Image 

def load_model(path):
    model = load_model(path)
    return model 

def predict(img):
    image = Image.open(img)
    model = load_model('./Models/first_model.pkl')
    prediction = model.predict(image)
    return prediction[0]