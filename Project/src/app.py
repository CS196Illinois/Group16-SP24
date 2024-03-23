from flask import Flask, request, jsonify
import os

app = Flask(__name__, static_folder='../ui')

@app.route('/')
def index():
    with open(os.path.join(app.static_folder, 'index.html'), 'r') as file:
        return file.read()

@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    exercise_type = request.form['exercise-type']
    current_weight = request.form['current-weight']
    target_weight = request.form['target-weight']

    # Hard-coded logic for demonstration
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

@app.route('/ui/<path:path>')
def send_ui(path):
    return send_from_directory('ui', path)

if __name__ == '__main__':
    app.run(debug=True)
