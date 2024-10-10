import pandas as pd
import requests
import time

#preprocess data

#RECREATION CENTERS
df = pd.read_csv('rec_centers_datasd.csv')
df = df.drop(columns='fac_nm_id')
df = df.drop(columns='sq_ft')
df = df.drop(columns='year_built')
df = df.drop(columns='serv_dist')
df = df.drop(columns='lat')
df = df.drop(columns='lng')
df.to_csv('../testing_app/RecreationCenters.csv', index=False)

#LIBRARIES
df = pd.read_csv('LocalLibraryLocations.csv')
df = df.drop(columns='Latitude')
df = df.drop(columns='Longtitude')
df = df.drop(columns='10.1 FSCSKey')
df.to_csv('../testing_app/Libraries.csv', index=False)

#PARKS
df = pd.read_csv('parks_datasd.csv')
df = df.drop(columns='gis_acres')
df = df.drop(columns='owner')
df = df.drop(columns='source_id')
df = df.drop(columns='source')
df = df.drop(columns='source_dt')
df = df.drop(columns='src_notes')
df.to_csv('../testing_app/Parks.csv', index=False)


#BIKE ROUTES
df = pd.read_csv('bike_routes_datasd.csv')
df = df.drop(columns='class')
df = df.drop(columns='district')
df = df.drop(columns='sapid')
df = df.drop(columns='iamfloc')

#extracting road names and appending zip codes
# def get_zip_code_from_road(road):
#      api_key = ''
#      try:
#          time.sleep(0.5)
#          response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={road},+San+Diego&key={api_key}')
#          if response.status_code == 200:
#              data = response.json()
#              if data['results']:
#                  for component in data['results'][0]['address_components']:
#                      if 'postal_code' in component['types']:
#                          return component['long_name']
#          return None
#      except Exception as e:
#          print(f"Error fetching data for {road}: {e}")
#          return None

# total_roads = len(df)
# for index, road in enumerate(df['rd20full']):
#     print(f"Processing road {index + 1} of {total_roads}: {road}")
#     df.at[index, 'zip'] = get_zip_code_from_road(road)

# df.to_csv('../testing_app/BikeRoutes.csv', index=False)

