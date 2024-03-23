import os
from flask import Flask, request, jsonify, render_template

# Define the base directory
basedir = os.path.abspath(os.path.dirname(__file__) + '/..')

app = Flask(__name__,
            static_folder=os.path.join(basedir, 'static'),
            template_folder=os.path.join(basedir, 'templates'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    exercise_type = request.form['exercise-type']
    current_weight = request.form['current-weight']
    target_weight = request.form['target-weight']

    if exercise_type == 'core':
        plan = 'Do 30 minutes of core exercises daily.'
    elif exercise_type == 'legs':
        plan = 'Do 40 minutes of leg exercises daily.'
    else:  # upper-body
        plan = 'Do 35 minutes of upper body exercises daily.'

    return jsonify({
        'exercise_type': exercise_type,
        'current_weight': current_weight,
        'target_weight': target_weight,
        'plan': plan
    })

if __name__ == '__main__':
    app.run(debug=True)
