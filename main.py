from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# example task list
tasks = [
    {
        'id': 1,
        'task': 'do chem tutorial',
        'completed': False
    },
    {
        'id': 2,
        'task': 'Do math homework',
        'completed': False
    },
    {
        'id': 3,
        'task': 'watch econs lecture',
        'completed': False
    }
]

# home route to display the task list
@app.route('/')
def home():
    return render_template('home.html', tasks=tasks)

# route to handle adding a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    task = {
        'id': len(tasks) + 1,
        'task': request.form['task'],
        'completed': False
    }
    tasks.append(task)
    return redirect(url_for('home'))

# route to handle completing a task
@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
    return redirect(url_for('home'))

# route to handle deleting a task
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('home'))

# route to handle deleting completed tasks
@app.route('/delete_completed_tasks', methods=['POST'])
def delete_completed_tasks():
    global tasks
    tasks = [task for task in tasks if not task['completed']]
    return redirect(url_for('home'))

@app.route('/study_timer', methods=['GET', 'POST'])
def study_timer():
    if request.method == 'POST':
        subject = request.form['subject']
        time = request.form['time']
        
        # easter egg
        if subject.lower() == 'tristan':
            return "<script>alert('hey how did you get here?');</script>"
    
  
        return redirect(url_for('timer', subject=subject, time=time))
    return render_template('study_timer.html')

@app.route('/timer/<subject>/<int:time>')
def timer(subject, time):
    return render_template('timer.html', subject=subject, time=time)

@app.route('/good_study_methods')
def good_study_methods():
    return render_template('good_study_methods.html')

@app.route('/submit_suggestion', methods=['POST'])
def submit_suggestion():
    helpful = request.form['helpful']
    suggestion = request.form['suggestion']
    
    with open('suggestions.txt', 'a') as f:
        f.write(f'{helpful}: {suggestion}\n')
    
    return "thank you for your suggestion!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)







#app.run(host='0.0.0.0', port=81)


app.run(host='0.0.0.0', port=81)


