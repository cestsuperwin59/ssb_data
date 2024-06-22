import requests
import pandas as pd
import json

# URL for the SSB API
url = "https://data.ssb.no/api/v0/en/table/14172"

# JSON query
query = {
  "query": [
    {
      "code": "Region",
      "selection": {
        "filter": "item",
        "values": [
          "0N"
        ]
      }
    },
    {
      "code": "InnKvartering1",
      "selection": {
        "filter": "item",
        "values": [
          "01",
          "02+03+04"
        ]
      }
    },
    {
      "code": "Landkoder2",
      "selection": {
        "filter": "item",
        "values": [
          "00000"
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "Overnattinger"
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "item",
        "values": [
          "2023M01",
          "2023M02",
          "2023M03",
          "2023M04",
          "2024M01",
          "2024M02",
          "2024M03",
          "2024M04"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}


# Make the API call
response = requests.post(url, json=query)
data = response.json()

# Print the JSON response to inspect its structure
print(json.dumps(data, indent=4))

# Extracting dimension labels
time_labels = data['dimension']['Tid']['category']['label']
region_label = data['dimension']['Region']['category']['label']['0N']
accommodation_labels = data['dimension']['InnKvartering1']['category']['label']
country_label = data['dimension']['Landkoder2']['category']['label']['00000']

# Extract values
values = data['value']

# Calculate number of values per time period (assuming each period has the same number of values)
num_accommodations = len(accommodation_labels)
num_periods = len(time_labels)

# Create a dictionary to store the summed values for each month
summed_values = {time_labels[key]: 0 for key in time_labels.keys()}

# Sum the values for each month across the two accommodation types
for i in range(num_periods):
    for j in range(num_accommodations):
        index = i * num_accommodations + j
        if index < len(values):
            month_label = time_labels[list(time_labels.keys())[i]]
            summed_values[month_label] += values[index]

# Convert the summed values dictionary to a DataFrame
df = pd.DataFrame(list(summed_values.items()), columns=['Month', 'Total Guest Nights'])

# Save DataFrame to CSV
df.to_csv('summed_guest_nights_data.csv', index=False)
print("Data saved to summed_guest_nights_data.csv")
