import spacy
import pandas as pd

# Load in the data from JSON file
data    = pd.read_json('./data/restaurant.json')
print(data.head(10))

# Data preprocessing
columns = data.columns
print(columns)
data     = data[['text','stars']]

print(data.head(5))

data_sorted = data.sort_values(by='stars', ascending=False) 


print(data_sorted)


