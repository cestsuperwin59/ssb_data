# Labour force, employment, unemployment and man-weeks worked, by sex, age and type of adjustment. Break adjusted figures 2006M01 - 2024M04

import requests
import pandas as pd
import io

# URL for the SSB API
url = "https://data.ssb.no/api/v0/en/table/13760"  # Example table ID for unemployment

# JSON query to fetch data for 2023 and 2024
query = {
  "query": [
    {
      "code": "Kjonn",
      "selection": {
        "filter": "item",
        "values": ["0"]             # Total, both sexes
      }
    },
    {
      "code": "Alder",
      "selection": {
        "filter": "item",
         "values": [
          "15-74"                   # Age group 15-74
        ]
      }
    },
    {
      "code": "Justering",
      "selection": {
        "filter": "item",
        "values": [
          "T"                       # Seasonally adjusted
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "SysselProsBefolkn", "ArbledProsArbstyrk" 
        ]           #employment rate and unemployment rate
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "item",
        "values": ["2023M01", "2023M02", "2023M03", "2023M04", "2023M05",
                    "2024M01", "2024M02", "2024M03", "2024M04"]
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

# Read the CSV content into a DataFrame
df = pd.read_csv(io.StringIO(csv_content))


# Transpose the DataFrame
transposed_df = df.transpose()

# Save the transposed DataFrame to a new CSV file
transposed_csv_file_path = 'transposed_unemploy.csv'
transposed_df.to_csv(transposed_csv_file_path, header=False)

print(f"Transposed data saved to {transposed_csv_file_path}")


