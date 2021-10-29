{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 381
    },
    "id": "kcxlK9uXImcj",
    "outputId": "fad05cb4-d388-4840-dad8-c986c7175ee5"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on all addresses.\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      " * Running on http://192.168.0.6:80/ (Press CTRL+C to quit)\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET / HTTP/1.1\" 200 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/css/main.css HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/jquery.min.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/jquery.scrollex.min.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/jquery.scrolly.min.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/browser.min.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/breakpoints.min.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/util.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/main.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/jquery.min.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/jquery.scrollex.min.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/jquery.scrolly.min.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/browser.min.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/breakpoints.min.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/util.js HTTP/1.1\" 404 -\n",
      "192.168.0.6 - - [28/Oct/2021 11:39:37] \"GET /assets/js/main.js HTTP/1.1\" 404 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify, render_template,redirect, url_for, request,json\n",
    "from werkzeug.utils import secure_filename\n",
    "import os\n",
    "\n",
    "from tensorflow import keras\n",
    "from tensorflow.keras.models import load_model\n",
    "from tensorflow.keras.preprocessing.image import load_img\n",
    "from tensorflow.keras import utils\n",
    "from PIL import Image\n",
    "import numpy as np\n",
    "\n",
    "model = load_model(\"paintings.h5\")\n",
    "model.make_predict_function()\n",
    "categories = [\"VanGohg\" , \"Not\"]\n",
    "\n",
    "def preprocess(img):\n",
    "  img = np.asarray(img)\n",
    "  img = utils.normalize(img, axis=1)\n",
    "  return img\n",
    "\n",
    "def predict(location):\n",
    "  img = load_img(location,target_size=(400, 400))\n",
    "  img = preprocess(img)\n",
    "  pred = model.predict(img)\n",
    "  predictedClass = np.argmax(pred[0])\n",
    "  if predicted_class == 0:\n",
    "    pred_made = categories[0]\n",
    "  else:\n",
    "    pre_made = categories[1]\n",
    "  return pred_made\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/predictPlaigrism', methods = ['GET','POST'])\n",
    "def process_image():\n",
    "    if request.method == 'POST':\n",
    "        f = request.files['file']\n",
    "        location = \"static/img/upload/\"+f.filename\n",
    "        f.save(os.path.join('static/img/upload', secure_filename(f.filename)))\n",
    "        output=predict(location)\n",
    "        data = {'location': location, 'predict': output}\n",
    "        return jsonify(data), 200\n",
    "    return None\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(host='0.0.0.0',port=80)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "name": "Flaskapi.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
