from flask import Flask, request
import numpy as np
from flask_cors import CORS, cross_origin
from PIL import Image
import tensorflow as tf

global_index = 0

app = Flask(__name__)
CORS(app, support_credentials=True)
model = tf.keras.models.load_model('saved_model/my_model')

@app.route('/', methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def mentoring():
    a = []
    if request.method == "POST":
        global global_index
        for d in request.data:
            a.append(d)
        img = np.array(a)
        img = np.uint8(img)
        img = img.reshape(28, 28, 1)
        img = np.squeeze(img, axis=2)
        global_index += 1
        # print(img.shape)
        print(np.argmax(model.predict(img.reshape(1, 28, 28, 1))))
        im = Image.fromarray(abs(255 - img))
        im.save("{}.jpeg".format(global_index))
        return str(np.argmax(model.predict(img.reshape(1, 28, 28, 1))))
    return "HELLO"
    
if __name__ == '__main__':
  app.run(port=8011)