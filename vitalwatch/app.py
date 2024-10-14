from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

if __name__ == '__main__':
    app.run(debug=True)
