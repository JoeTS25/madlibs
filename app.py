from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def choose_options():
    prompts = story.prompts
    return render_template("mad-libs-home.html", prompts = prompts)

@app.route('/results')
def madlibs_results():
    text = story.generate(request.args)    
    return render_template("mad-libs-results.html", text = text)