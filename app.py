from flask import Flask, jsonify
from powClass import PoWClass
import os

app = Flask(__name__)

@app.route('/pow')
def get_pow_key():  # put application's code here
    powInit = PoWClass()
    powKey = powInit.createPoWAddress(0x80000000000, 0xfffffffffff) # this will be a subrange for Proof of Work
    return jsonify(powKey)

@app.route('/range')
def get_ranges():  # put application's code here
    powInit = PoWClass()
    splitRange = powInit.splitRangeForWork(0x80000000000, 0xfffffffffff, 64)
    return jsonify(splitRange)


if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = os.urandom(64)
    app.run()
