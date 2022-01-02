from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Survey, Question

app = Flask(__name__)
app.config['SECRET_KEY'] = "surveymachine"
debug = DebugToolbarExtension(app)

#Surveys
satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

# user session data
responses = []

@app.route('/')
def begin_survey():
    '''Initialize survey, show home page.'''
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    
    return render_template('home.html', title=title, instructions=instructions)

@app.route('/questions/<question>')
def show_next_question(question):
    '''Display current question'''
    return render_template('question.html')