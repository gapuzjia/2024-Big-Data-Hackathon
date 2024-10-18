from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Load all datasets into a dictionary
datasets = {
    'dataset1': pd.read_csv('datasets/BikeRoutes.csv'),
    'dataset2': pd.read_csv('datasets/Parks.csv'),
    'dataset3': pd.read_csv('datasets/RecreationCenters.csv')
}

# Define columns to return for each dataset
column_mapping  = {
    'dataset1': ['Road', 'Exit Street', 'Zip Code'],
    'dataset2': ['Park', 'Location', 'Zip Code'],
    'dataset3': ['Center', 'Address', 'Zip Code']
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

# Load prizes from CSV
prizes_df = pd.read_csv('datasets/Prizes.csv')  # Adjust path as necessary

# Load all datasets into a dictionary (make sure your CSV files are in the correct format)
prizes_df = pd.read_csv('datasets/Prizes.csv', encoding='ISO-8859-1')  # Specify encoding if needed
prizes = prizes_df['Prize'].tolist()  # Assuming 'Prize' is the column name

@app.route('/rewards')
def rewards():
    return render_template('rewards.html', prizes=prizes)

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/museums')
def museums():
    return render_template('museums.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html')

@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    results = {key: pd.DataFrame() for key in datasets.keys()}
    query = ""
    page = 1  # Default to the first page
    per_page = 5  # Set the number of results per page

    if request.method == 'POST':
        query = request.form.get('query')  # Get the query from the form
        page = int(request.form.get('page', 1))  # Get the page number from the form

        print(f"Query received: {query}, Page: {page}")  # Debug output

        try:
            # Convert the query to an integer (assuming it's a valid zip code)
            zip_code = int(query)

            for dataset_name, df in datasets.items():
                # First, search for rows that contain the query in any column
                search_results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]

                # Now filter to find rows where any numeric column is within ±2 of the zip code
                numeric_cols = df.select_dtypes(include='number').columns  # Get numeric columns

                if not numeric_cols.empty:  # Proceed if there are numeric columns
                    range_results = pd.DataFrame()  # Initialize an empty DataFrame

                    for col in numeric_cols:
                        within_range = df[df[col].between(zip_code - 9, zip_code + 9)]
                        range_results = pd.concat([range_results, within_range], ignore_index=True)

                    range_results = range_results.drop_duplicates()
                    search_results = pd.concat([search_results, range_results], ignore_index=True).drop_duplicates()

                results[dataset_name] = search_results

        except ValueError:
            print("Invalid zip code format. Please enter a numeric zip code.")

    # Pagination logic
    paginated_results = {}
    has_more = {}

    for dataset_name, df in results.items():
        total_results = len(df)
        # Get the results for the current page
        paginated_results[dataset_name] = df.iloc[(page - 1) * per_page:page * per_page]
        has_more[dataset_name] = total_results > page * per_page  # Check if there are more results

    # Pass paginated results and column mapping to the template
    return render_template('search.html', results=paginated_results, query=query, column_mapping=column_mapping, has_more=has_more, page=page)



if __name__ == '__main__':
    app.run(debug=True)
