from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)


@app.route("/")
def create_story():
  """Creates story from user input"""
  return render_template("base.html", prompts = story.prompts)

@app.route("/story")
def show_story():
  """Shows story on page"""
  story_text = story.generate(request.args)

  return story_text
