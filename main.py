import os
from flask import Flask, render_template, send_file, request
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename

from evaluate import ffwd_to_img

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

# webapp
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/style_transfer', methods=["POST"])
def style_transfer():
    """
        Take the input image and style transfer it
    """
    # check if the post request has the file part
    if 'file' not in request.files:
        return BadRequest("File not present in request")
    file = request.files['file']
    if file.filename == '':
        return BadRequest("File name is not present in request")
    if not allowed_file(file.filename):
        return BadRequest("Invalid file type")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_filepath = os.path.join('./in_images/', filename)
        output_filepath = os.path.join('./out_images/', filename)
        file.save(input_filepath)

        # Get checkpoint filename from la_muse
        checkpoint = request.form.get("checkpoint") or "la_muse.ckpt"
        ffwd_to_img(input_filepath, output_filepath, './input/' + checkpoint, '/gpu:0')
        return send_file(output_filepath, mimetype='image/jpg')
        # return send_file(input_filepath, mimetype='image/jpg')


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run()
