# Dependencies
import requests
import json
import pandas as pd

# base URL 
base_url = "https://api.domain.com.au/v1/properties/RF-8884-AK/priceEstimate"

# read data from URL        
data = requests.get(base_url).json()    

# print(json.dumps(data, indent=4, sort_keys=True))
# convert to dataframe
df = pd.DataFrame.from_dict(data, orient='columns')
print(df)

