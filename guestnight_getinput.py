import requests
import pandas as pd
import json
import io

# Function to get user input for table number and Tid values
def get_user_input():
    table_number = input("Enter the table number (e.g., 14162): ")
    tid_values = input("Enter the Tid values separated by commas (e.g., 2024M01,2024M02,2024M03): ").split(',')
    return table_number.strip(), [tid.strip() for tid in tid_values]

# Get user input
table_number, tid_values = get_user_input()

# URL for the SSB API
url = f"https://data.ssb.no/api/v0/en/table/{table_number}"  # Example table ID for guestnight

# JSON query to fetch data for the specified Tid values

query = {
  "query": [
    {
      "code": "Region",
      "selection": {
        "filter": "vs:LandetNyn",
        "values": [
          "0N"              #whole country
        ]
      }
    },
    {
      "code": "InnKvartering1",
      "selection": {
        "filter": "item",
        "values": [
          "00"              # total includes hotels, campings, etc
        ]
      }
    },
    {
      "code": "Landkoder2",
      "selection": {
        "filter": "item",
        "values": [
          "00000",          # total
          "ccc",            # Foreign national, total
          "000"             # Norway
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "Overnattinger"   #guest nights
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "item",
        "values": tid_values
      }
    }
  ],
  "response": {
    "format": "csv"
  }
}
try:
    # Make the API call and get the CSV content
    response = requests.post(url, json=query)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    csv_content = response.content.decode('utf-8')

    # Save the CSV content to a file
    csv_file_path = 'guestnight.csv'
    with open(csv_file_path, 'w', encoding='utf-8') as file:
        file.write(csv_content)

    print(f"Data saved to {csv_file_path}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    input("Press Enter to exit...")  # To keep the console window open until the user presses Enter
