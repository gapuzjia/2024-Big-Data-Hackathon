from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  # Get the JSON data from the request
    name = data.get('name')  # Extract the 'name' field

    if not name:
        return jsonify({'message': 'Please provide a name!'}), 400  # Return JSON error response if name is missing

    message = f"Hello, {name}! This response is from Python Flask."
    return jsonify({'message': message})  # Return JSON response

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
