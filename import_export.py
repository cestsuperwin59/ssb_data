import requests
import pandas as pd
import json

# url for the SSB API
url = "https://data.ssb.no/api/v0/en/table/08792" # Example table ID for External trade in goods

# # JSON query to fetch data for 2023 and 2024

query = {
 "query": [
    {
      "code": "HovedVareStrommer",
      "selection": {
        "filter": "item",
        "values": [
          "Itot",
          "Itotuskip",
          "Itotuso",
          "Itotusor",
          "Etot",
          "Etotueski",
          "Etotuskip",
          "Etotuso",
          "Hbtot"

        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "VerdiUjustert"
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
          "2023M05",
          "2024M01",
          "2024M02",
          "2024M03",
          "2024M04",
          "2024M05"
        ]
      }
    }
  ],
  "response": {
    "format": "csv"
  }
}

# Make the API call and get the CSV content
response = requests.post(url, json=query)
csv_content = response.content.decode('utf-8')

# Save the CSV content to a file
csv_file_path = 'import_export.csv'
with open(csv_file_path, 'w', encoding='utf-8') as file:
    file.write(csv_content)

print(f"Data saved to {csv_file_path}")

