from flask import Flask, render_template, request, redirect, url_for,session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def home():
    return render_template('home.html')