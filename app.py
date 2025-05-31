from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample data
tasks = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'completed': False
    }
    tasks.append(task)
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(debug=True)
