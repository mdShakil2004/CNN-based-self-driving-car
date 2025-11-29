import argparse
import base64
from datetime import datetime
import os
import shutil

import numpy as np
import socketio
import eventlet
import eventlet.wsgi
from PIL import Image
from flask import Flask
from io import BytesIO
import h5py

from keras.models import load_model
import utils

# Initialize SocketIO server
sio = socketio.Server(async_mode='eventlet')
app = Flask(__name__)
app = socketio.WSGIApp(sio, app)

# Globals
model = None
speed_limit = 15  # default
MAX_SPEED = 25
MIN_SPEED = 10


@sio.on('telemetry')
def telemetry(sid, data):
    if data:
        speed = float(data["speed"])
        image = Image.open(BytesIO(base64.b64decode(data["image"])))

        # Save frame if folder enabled
        if args.image_folder != '':
            timestamp = datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S_%f')[:-3]
            image_filename = os.path.join(args.image_folder, timestamp)
            image.save('{}.jpg'.format(image_filename))

        # Preprocess
        image = np.asarray(image)
        image = utils.preprocess(image)
        image = np.expand_dims(image, axis=0)

        # Predict steering
        steering_angle = float(model.predict(image, batch_size=1))

        # Dynamic throttle control
        global speed_limit
        if speed > speed_limit:
            speed_limit = MIN_SPEED
        else:
            speed_limit = MAX_SPEED

        throttle = 1.0 - steering_angle**2 - (speed / speed_limit) ** 2

        print(f"{steering_angle} {throttle} {speed}")
        send_control(steering_angle, throttle)

    else:
        sio.emit('manual', data={}, skip_sid=True)


@sio.on('connect')
def connect(sid, environ):
    print("Connected:", sid)
    send_control(0, 0)


def send_control(steering_angle, throttle):
    sio.emit(
        "steer",
        data={
            'steering_angle': str(steering_angle),
            'throttle': str(throttle)
        },
        skip_sid=True
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remote Driving")
    parser.add_argument(
        "model",
        type=str,
        help="Path to model.h5 file."
    )
    parser.add_argument(
        "image_folder",
        type=str,
        nargs="?",
        default="",
        help="Folder to save images."
    )

    args = parser.parse_args()

    print("Loading model:", args.model)
    model = load_model(args.model, compile=False)   # IMPORTANT FIX

    if args.image_folder != "":
        if not os.path.exists(args.image_folder):
            os.makedirs(args.image_folder)
        else:
            shutil.rmtree(args.image_folder)
            os.makedirs(args.image_folder)
        print("Recording enabled.")
    else:
        print("Recording disabled.")

    # Run server
    eventlet.wsgi.server(eventlet.listen(("", 4567)), app)
