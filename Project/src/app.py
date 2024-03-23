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
    if target_weight < current_weight:
        if exercise_type == 'core':
            plan = """Goal = Weight Loss: 
            3 repeats (3 sets/12 reps crunches, 3 sets/12 reps bicycle kicks, 3 set/12 reps flutter kick)
            1 min rest between sets 5 min between repeats"""
        elif exercise_type == 'legs':
            plan = """Goal = Weight Loss:
            3 repeats of (3 sets of 15 lightweight squats|3 sets of 30 walking lunges|3 sets of 10 bulgarian split squats|0.5 mile run)
            2 minute rest between sets 5 minute rest between repeats"""
        else:  # upper-body
            plan = """Goal = Weight Loss:
            3 repeats of (3 sets of 5 pullups|3 sets of 12 light bench press|3 sets of 8 pushups|2 sets till failure light tricep extension)
            1 minute rest inbetween sets 5 inbetween repeats"""
    elif target_weight > current_weight:
        if exercise_type == 'core':
            plan = """Goal = Weight Gain: 
            1x(2 sets/5 reps weighted crunches|2 sets/30 reps hanging leg raises|2 sets/12 reps medicine ball throw)
            3 minute rest between all sets"""
        elif exercise_type == 'legs':
            plan = """Goal = Weight Gain:
            1x(2 sets of 5 heavy squat|2 sets of 12 heavy leg press|2 sets of bulgarian split squats till failure)
            3-5 minute rest inbetween sets"""
        else:  # upper-body
            plan = """Goal = Weight Gain:
            1x(2 sets of 5 heavy bench|2 sets of 12 heavy incline bench press|2 sets of 5 pullups|1 set until failure heavy dips)
            3 minute rest between sets"""

    return jsonify({
        'exercise_type': exercise_type,
        'current_weight': current_weight,
        'target_weight': target_weight,
        'plan': plan
    })

if __name__ == '__main__':
    app.run(debug=True)
