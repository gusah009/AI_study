# import Flask
import tensorflow as tf
import PIL.Image as pilimg
import numpy as np
import sys

application = Flask(__name__)
my_model = tf.keras.models.load_model('./saved_model/my_model')


@application.route("/", methods=['GET'])
def get_number():
    
    im = pilimg.open( "./mentoring.jpg" )
    
    pix = np.array(im)
    # print(pix)
    pix = pix.reshape(-1, 28 * 28) / 255.0
    # 모델 구조를 확인합니다
    # print(my_model.summary())
    print(my_model.predict(pix))
    return "Hello goorm!"


if __name__ == "__main__":
    application.run()
