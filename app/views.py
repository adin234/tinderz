from flask import render_template, redirect, request, jsonify, json
from app import app


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')
