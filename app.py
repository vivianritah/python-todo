from flask import Flask, render_template, request, redirect, url_for
#Creating instance
app= Flask(__name__, template_folder="templates")


tasks = []

@app.route("/")
def home():
    return render_template("index.html",tasks=tasks)

app.config['STATIC_FOLDER'] ='static' #replace with your actual static folder path

#Creating a new task function
@app.route('/add_task', methods=['POST'])
def create_task():
    task = request.form.get('task')
    tasks.append (task) #adding variable task to list tasks
    return redirect(url_for('index'))

@app.route('/update_task/<int:task_index>', methods=['PUT'])
def update_task(task_index):
    updated_task = request.form['updated_task']
    tasks[task_index] = updated_task
    return redirect(url_for('index'))






#enabling debug mode

if __name__ == "__main__":

    app.run(debug=True)