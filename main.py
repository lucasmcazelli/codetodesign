from flask import Flask, render_template, send_file

import numpy as np
from PIL import Image
import io


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/page/')
def page():
    return render_template("page.html")

@app.route('/personal_user/')
def personal_user():
    return render_template("personal_user.html")



@app.route('/api/b')
def array():
    '''
    generate image from numpy.array using PIL.Image
    and send without saving on disk using io.BytesIO'''

    arr = np.array([
        [255, 255,   0,   0,   0,   0,   0,   0, 255, 255],
        [255,   0, 255, 255, 255, 255, 255, 255,   0, 255],
        [  0, 255, 255, 255, 255, 255, 255, 255, 255,   0],
        [  0, 255, 255,   0, 255, 255,   0, 255, 255,   0],
        [  0, 255, 255, 255, 255, 255, 255, 255, 255,   0],
        [  0, 255, 255, 255, 255, 255, 255, 255, 255,   0],
        [  0, 255,   0, 255, 255, 255, 255,   0, 255,   0],
        [  0, 255, 255,   0,   0,   0,   0, 255, 255,   0],
        [255,   0, 255, 255, 255, 255, 255, 255,   0, 255],
        [255, 255,   0,   0,   0,   0,   0,   0, 255, 255],
    ])

    img = Image.fromarray(arr.astype('uint8')) # convert arr to image

    file_object = io.BytesIO()   # create file in memory 
    img.save(file_object, 'PNG') # save as PNG in file in memory
    file_object.seek(0)          # move to beginning of file
                                 # so send_file() will read data from beginning of file

    return send_file(file_object,  mimetype='image/png')








app.run(host='0.0.0.0', port=8080)
app.run()

if __name__ == '__main__':
    app.run(debug=True)