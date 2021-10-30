#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify, render_template,redirect, url_for, request,json
from werkzeug.utils import secure_filename
import os

from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras import utils
from PIL import Image
import numpy as np

model = load_model("paintings.h5")
model.make_predict_function()
categories = ["VanGohg" , "Not"]

def preprocess(img):
  img = np.asarray(img)
  img = utils.normalize(img, axis=1)
  return img

def predict(location):
  img = load_img(location,target_size=(400, 400))
  img = preprocess(img)
  pred = model.predict(img)
  predictedClass = np.argmax(pred[0])
  if predicted_class == 0:
    pred_made = categories[0]
  else:
    pre_made = categories[1]
  return pred_made

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predictPlaigrism', methods = ['GET','POST'])
def process_image():
    if request.method == 'POST':
        f = request.files['file']
        location = "static/img/upload/"+f.filename
        f.save(os.path.join('static/img/upload', secure_filename(f.filename)))
        output=predict(location)
        data = {'location': location, 'predict': output}
        return jsonify(data), 200
    return None

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)


# In[ ]:




