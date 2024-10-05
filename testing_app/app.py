from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV data into a DataFrame
data = pd.read_csv('mock_data.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    if not name:
        return jsonify({'message': 'Please provide a name!'}), 400
    message = f"Hello, {name}! This response is from Python Flask."
    return jsonify({'message': message})

@app.route('/search', methods=['POST'])
def search():
    try:
        data_json = request.json  # Get JSON data from the request
        search_term = data_json.get('searchTerm', '').lower()  # Get the search term and convert to lowercase

        if not search_term:
            return jsonify({'result': 'Please provide a search term!'}), 400

        # Apply filtering: search term should match any column (case-insensitive)
        filtered_data = data.applymap(str).apply(lambda row: row.str.lower().str.contains(search_term).any(), axis=1)

        results = data[filtered_data]

        if results.empty:
            return jsonify({'result': 'No results found!'}), 404

        # Convert filtered DataFrame to JSON format for response
        result = results.to_dict(orient='records')
        return jsonify({'result': result})  # Return the search result in JSON

    except Exception as e:
        return jsonify({'result': f'Error occurred: {str(e)}'}), 500

@app.route('/save_checklist', methods=['POST'])
def save_checklist():
    data = request.json
    checklist = data.get('checklist')
    return jsonify({'message': 'Checklist saved successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
