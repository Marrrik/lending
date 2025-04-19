from flask import Flask, render_template, request, redirect, session, jsonify
import os
import json
import os
import uuid
import re
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('lending.html')

if __name__ == '__main__':
    app.run(debug=True)