import pandas as pd

# #BIKE ROUTES
# df = pd.read_csv('datasets/BikeRoutes.csv')
# df['Road'] = df['Road'].str.title()
# df['Exit Street'] = df['Exit Street'].str.title()
# df.to_csv('datasets/BikeRoutes.csv', index=False)

# #LIBRARIES
# df = pd.read_csv('datasets/Libraries.csv')
# df['Location'] = df['Location'].str.title()
# df['Address'] = df['Address'].str.title()
# df.to_csv('datasets/Libraries.csv', index=False)


# #PARKS
# df = pd.read_csv('datasets/Parks.csv')
# df['Location'] = df['Location'].str.title()
# df['Park'] = df['Park'].str.title()
# df.to_csv('datasets/Parks.csv', index=False)


df = pd.read_csv('datasets/BikeRoutes.csv')
df = df.dropna()
df.to_csv('datasets/BikeRoutes.csv', index=False)

df = pd.read_csv('datasets/Parks.csv')
df = df.dropna()
df.to_csv('datasets/Parks.csv', index=False)

df = pd.read_csv('datasets/RecreationCenters.csv')
df = df.dropna()
df.to_csv('datasets/RecreationCenters.csv', index=False)