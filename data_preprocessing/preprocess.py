import pandas as pd
import requests
import time
from datetime import datetime
import csv

# #preprocess data

# #RECREATION CENTERS
# df = pd.read_csv('rec_centers_datasd.csv')
# df = df.drop(columns='fac_nm_id')
# df = df.drop(columns='sq_ft')
# df = df.drop(columns='year_built')
# df = df.drop(columns='serv_dist')
# df = df.drop(columns='lat')
# df = df.drop(columns='lng')
# df.to_csv('../testing_app/RecreationCenters.csv', index=False)

# #LIBRARIES
# df = pd.read_csv('LocalLibraryLocations.csv')
# df = df.drop(columns='Latitude')
# df = df.drop(columns='Longtitude')
# df = df.drop(columns='10.1 FSCSKey')
# df.to_csv('../testing_app/Libraries.csv', index=False)

# #PARKS
# df = pd.read_csv('parks_datasd.csv')
# df = df.drop(columns='gis_acres')
# df = df.drop(columns='owner')
# df = df.drop(columns='source_id')
# df = df.drop(columns='source')
# df = df.drop(columns='source_dt')
# df = df.drop(columns='src_notes')
# df.to_csv('../testing_app/Parks.csv', index=False)

# # def get_zip_code_from_park(park_name):
# #     api_key = 'AIzaSyBvK-9gnEPbxgcqAJTYKby_DVRrap9yr9o' 
# #     try:
# #         time.sleep(0.5)  # Sleep to avoid hitting the API rate limit
# #         response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={park_name},+San+Diego&key={api_key}')
# #         if response.status_code == 200:
# #             data = response.json()
# #             if data['results']:
# #                 for component in data['results'][0]['address_components']:
# #                     if 'postal_code' in component['types']:
# #                         return component['long_name']
# #         return None
# #     except Exception as e:
# #         print(f"Error fetching data for {park_name}: {e}")
# #         return None

# # total_parks = len(df)
# # for index, park_name in enumerate(df['name']):  # Replace 'park_name_column' with your actual column name
# #     print(f"Processing park {index + 1} of {total_parks}: {park_name}")
# #     df.at[index, 'zip'] = get_zip_code_from_park(park_name)



# #BIKE ROUTES
# df = pd.read_csv('bike_routes_datasd.csv')
# df = df.drop(columns='class')
# df = df.drop(columns='district')
# df = df.drop(columns='sapid')
# df = df.drop(columns='iamfloc')

# #extracting road names and appending zip codes
# # def get_zip_code_from_road(road):
# #      api_key = ''
# #      try:
# #          time.sleep(0.5)
# #          response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={road},+San+Diego&key={api_key}')
# #          if response.status_code == 200:
# #              data = response.json()
# #              if data['results']:
# #                  for component in data['results'][0]['address_components']:
# #                      if 'postal_code' in component['types']:
# #                          return component['long_name']
# #          return None
# #      except Exception as e:
# #          print(f"Error fetching data for {road}: {e}")
# #          return None

# # total_roads = len(df)
# # for index, road in enumerate(df['rd20full']):
# #     print(f"Processing road {index + 1} of {total_roads}: {road}")
# #     df.at[index, 'zip'] = get_zip_code_from_road(road)

# # df.to_csv('../testing_app/BikeRoutes.csv', index=False)

#USE API TO GET NEARBY RESTAURANTS--------------------------

# # Your Google API Key
# API_KEY = 'AIzaSyBvK-9gnEPbxgcqAJTYKby_DVRrap9yr9o'
# API_SEARCH_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
# API_DETAILS_URL = 'https://maps.googleapis.com/maps/api/place/details/json'

# # Set the parameters for the initial search query
# params = {
#     'location': '32.7157,-117.1611',  # Latitude and longitude for San Diego
#     'radius': 50000,  # Search radius in meters (15 km)
#     'type': 'restaurant',
#     'keyword': 'healthy',
#     'key': API_KEY
# }

# # Make the initial request to the Google Places API
# response = requests.get(API_SEARCH_URL, params=params)

# # Check if the request was successful
# if response.status_code == 200:
#     data = response.json()
#     healthy_restaurants = data.get('results', [])

#     print(f"Adding {len(healthy_restaurants)} restaurants to the file...")

#     # Create a CSV file to save the restaurant data
#     with open('healthy_restaurants_san_diego.csv', mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         # Write the header row
#         writer.writerow(['Name', 'Rating', 'Address', 'Food Keywords'])

#         # Loop through each restaurant to get more detailed information
#         for restaurant in healthy_restaurants:
#             place_id = restaurant.get('place_id')
#             name = restaurant.get('name')
#             rating = restaurant.get('rating', 'No rating available')
#             address = restaurant.get('vicinity', 'No address available')

#             # Get detailed information for each restaurant using the Place Details API
#             details_params = {
#                 'place_id': place_id,
#                 'fields': 'types',
#                 'key': API_KEY
#             }
#             details_response = requests.get(API_DETAILS_URL, params=details_params)
#             if details_response.status_code == 200:
#                 details_data = details_response.json()
#                 food_keywords = ', '.join(details_data.get('result', {}).get('types', []))
#             else:
#                 food_keywords = 'No food keywords available'

#             # Write the restaurant data to the CSV file
#             writer.writerow([name, rating, address, food_keywords])

#     print("Data successfully saved to healthy_restaurants_san_diego.csv")
# else:
#     print(f"Error: Unable to fetch data from Google Places API (Status Code: {response.status_code})")

#END RESTAURANT DATA--------------------


#PREPROCESS EVENTS DATA----------------------------
# Your Eventbrite API Key
API_KEY = 'RBDE3E4J5R4CDLRVVT45'
API_URL = 'https://www.eventbriteapi.com/v3/events/search/'

# Parameters for the Eventbrite API query
params = {
    'location.address': 'San Diego, CA',
    'location.within': '25km',
    'categories': '109',  # Category 109 typically includes "Outdoors & Recreation" events
    'start_date.range_start': datetime.now().isoformat(),  # Start from today's date
    'start_date.range_end': '2024-11-30T23:59:59',  # Up to the end of November
    'token': API_KEY
}

import requests
import csv
from datetime import datetime

# # Your Eventbrite API Key
# API_KEY =   # Replace with your actual API key
# API_URL = 'https://www.eventbriteapi.com/v3/events/search/'

# # Parameters for the Eventbrite API query
# params = {
#     'location.address': 'San Diego, CA',
#     'location.within': '25km',
#     'start_date.range_start': datetime.now().isoformat() + 'Z',  # Ensure correct format
#     'start_date.range_end': '2024-11-30T23:59:59Z',  # End of November
# }

# # Set headers with API key
# headers = {
#     'Authorization': f'Bearer {API_KEY}',
# }

# # Make the request to the Eventbrite API
# response = requests.get(API_URL, params=params, headers=headers)

# # Check if the request was successful
# if response.status_code == 200:
#     data = response.json()
#     outdoor_events = data.get('events', [])

#     print(f"Adding {len(outdoor_events)} outdoor events to the file...")

#     # Create a CSV file to save the event data
#     with open('outdoor_events_san_diego.csv', mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         # Write the header row
#         writer.writerow(['Event Name', 'Start Date', 'End Date', 'Venue', 'Address'])

#         # Write the event data to the CSV file
#         for event in outdoor_events:
#             event_name = event.get('name', {}).get('text', 'No event name available')
#             start_date = event.get('start', {}).get('local', 'No start date available')
#             end_date = event.get('end', {}).get('local', 'No end date available')
#             venue = event.get('venue', {}).get('name', 'No venue information available')
#             address = event.get('venue', {}).get('address', {}).get('localized_address_display', 'No address available')

#             writer.writerow([event_name, start_date, end_date, venue, address])

#     print("Data successfully saved to outdoor_events_san_diego.csv")
# else:
#     # Output the error details for debugging
#     print(f"Error: Unable to fetch data from Eventbrite API (Status Code: {response.status_code})")
#     print(response.json())  # Print the response content for more details


    # Your Eventbrite API Key
API_KEY = 'your_eventbrite_api_key'  # Replace with your actual API key
API_URL = 'https://www.eventbriteapi.com/v3/events/search/'

# Parameters for the Eventbrite API query (simplified)
params = {
    'location.address': 'San Diego',
    'token': API_KEY
}

# Set headers with API key
headers = {
    'Authorization': f'Bearer {API_KEY}',
}

# Make the request to the Eventbrite API
response = requests.get(API_URL, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    outdoor_events = data.get('events', [])
    print(f"Found {len(outdoor_events)} outdoor events.")
else:
    # Output the error details for debugging
    print(f"Error: Unable to fetch data from Eventbrite API (Status Code: {response.status_code})")
    print(response.json())  # Print the response content for more details
