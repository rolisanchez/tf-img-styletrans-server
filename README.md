# Tensorflow Image Style Transfer Server

As a part of a demo for Applications and Machine Learning, we will use a pre-trained model for Image Style Transfer to receive an image posted to a route on this server, modify the image to the required style and then return it to the user.

### Requirement ###

- Python >=2.7 or >=3.4
  - TensorFlow >=1.0
- Node >=6.9

### How to run ###

    $ pip install -r requirements.txt
    $ npm install
    $ export FLASK_APP=main.py
    $ flask run

### Deploy to Heroku ###

    $ heroku apps:create [NAME]
    $ heroku buildpacks:add heroku/nodejs
    $ heroku buildpacks:add heroku/python
    $ git push heroku master

## License
  Based on: https://github.com/lengstrom/fast-style-transfer
  Check his cool work for more applications like video style transfer.
  Copyright (c) 2016 Logan Engstrom.
