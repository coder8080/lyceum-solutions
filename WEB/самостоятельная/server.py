from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
        "whirlpool": [
            -9,
            99,
            35,
            6,
            57,
            30
        ],
        "foam": [
            37,
            95,
            97,
            30
        ],
        "wave": [
            0,
            -7,
            44,
            23,
            28,
            -3,
            18
        ],
        "depression": [
            82,
            67,
            31,
            74,
            49,
            73
        ],
        "shape": [
            -12,
            -5,
            60,
            68,
            75
        ]
    })


app.run(port=5000, host='127.0.0.1')
