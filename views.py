from flask import Flask, render_template, flash, redirect, session, url_for, request, g 
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/blog')
def blog():
	return render_template("blog.html")

@app.route('/projects')
def projects():
	return render_template("projects.html")

@app.route('/fefs_talk')
def fefs_talk():
    return render_template("fefs_talk.html")

@app.route('/slots_talk')
def slots_talk():
    return render_template("slots_talk.html")

@app.route('/cbvs_talk')
def cbvs_talk():
    return render_template("cbvs_talk.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
