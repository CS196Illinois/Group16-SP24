function generatePlan() {
    const exerciseType = document.getElementById('exercise-type').value;
    const currentWeight = document.getElementById('current-weight').value;
    const targetWeight = document.getElementById('target-weight').value;

    fetch('/generate-plan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `exercise-type=${exerciseType}&current-weight=${currentWeight}&target-weight=${targetWeight}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `
            <div>Type of Exercise: ${data.exercise_type}</div>
            <div>Current Weight: ${data.current_weight}</div>
            <div>Target Weight: ${data.target_weight}</div>
            <div id="exercise-plan-output">${data.plan}</div>
        `;
        document.getElementById('result').style.display = 'block';
    })
    .catch(error => console.error('Error:', error));
}
