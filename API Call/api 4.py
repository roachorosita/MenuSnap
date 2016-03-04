#Python 2.7.6
#RestfulClient.py

import requests
from requests.auth import HTTPDigestAuth
import json

# Replace with the correct URL
url = "https://api.locu.com/v1_0/venue/search/?api_key=77ca60baa8056bc0c1aa6f422bc525a56ed1443e&location=34.056286,-117.81601&radius=1600&category=restaurant"
url2 = "https://api.locu.com/v1_0/menu_item/search/?api_key=77ca60baa8056bc0c1aa6f422bc525a56ed1443e&name=burrito"
url3 = "https://api.locu.com/v2/venue/search/"
# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
myResponse = requests.get(url3)
#print (myResponse.status_code)

# For successful API call, response code will be 200 (OK)
if(myResponse.ok):

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)

    print("The response contains {0} properties".format(len(jData)))
    print(jData)
    for key in jData:
        print key + " : " + jData[key]
else:
  # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()