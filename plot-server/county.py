import requests
import pandas as pd

def get_c19_data_county(county):
  url = 'https://services1.arcgis.com/CY1LXxl9zlJeBuRZ/ArcGIS/rest/services/Florida_COVID19_Case_Line_Data/FeatureServer/0/query'
  parameters = {
    "where": f"lower(County)='{county}'",
    "outFields": "EventDate",
    "orderByFields": "EventDate",
    "f": "pjson"
  }

  done = False
  count = 0
  dataset = []
  while not done:
    response = requests.get(url, parameters)
    print(response.url)

    if response.status_code == 200:
      json = response.json()
      if 'exceededTransferLimit' in json:
        done=False
        count += 2000
        parameters['resultOffset'] = count
      else:
        done=True

      if 'features' in json:
        dataset = dataset + list(item['attributes'] for item in json['features'])
      else:
        return None
    else:
      return None

  df = pd.DataFrame.from_records(dataset)
  df['EventDate'] = pd.to_datetime(df['EventDate'], unit='ms')
  df = df.set_index('EventDate').sort_index()
  df = df[df.index > '2020-02-24']
  df['Count'] = 1
  return df
