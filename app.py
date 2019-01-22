from blinkstick import blinkstick
from flask import Flask
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": ["http://localhost:4200", "https://pomodor.herokuapp.com/"]}})

all_blink_sticks = blinkstick.find_all()


@app.route('/')
# Health check
def index():
    return "USB Light API is up and running."


@app.route('/light/<color>')
# Takes a hex color
def color(color):

    if len(all_blink_sticks) > 0:
        for bstick in all_blink_sticks:
            bstick.set_color(hex="#" + color)
            return jsonify('Success')
    else:
        print("No BlinkSticks found...")
        return jsonify("No BlinkSticks found...")


if __name__ == '__main__':
    app.run(port=5033)
