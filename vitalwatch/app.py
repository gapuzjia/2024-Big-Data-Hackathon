from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Load all datasets into a dictionary
datasets = {
    'dataset1': pd.read_csv('datasets/BikeRoutes.csv'),
    'dataset2': pd.read_csv('datasets/Libraries.csv'),
    'dataset3': pd.read_csv('datasets/Parks.csv'),
    'dataset4': pd.read_csv('datasets/RecreationCenters.csv')
}

# Define columns to return for each dataset
columns_to_return = {
    'dataset1': ['rd20full', 'xstrt1', 'rd20full', 'zip'],
    'dataset2': ['location', '10.6 Street Address', '10.7 City', '10.8 Zip Code'],
    'dataset3': ['name', 'location'],
    'dataset4': ['rec_bldg', 'address', 'zip']
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    results = {key: pd.DataFrame() for key in datasets.keys()}
    query = ""

    if request.method == 'POST':
        query = request.form.get('query')  # Get the query from the form
        print(f"Query received: {query}")  # Debug output

        for dataset_name, df in datasets.items():
            search_results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
            results[dataset_name] = search_results

    return render_template('search.html', results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)
