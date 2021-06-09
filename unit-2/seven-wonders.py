import requests
import time

path = "https://us1.locationiq.com/v1/search.php"

LOCATIONIQ_API_KEY = 'pk.a4509de0eaad22c787770dd0849382ff'

wonders = ["Great Wall of China", "Petra", "Colosseum", "Chichen Itza", "Machu Picchu", "Taj Mahal","Christ the Redeemer"]
    
for wonder in wonders:    
    query_params = {
        "key": LOCATIONIQ_API_KEY,
        "q": wonder,
        "format": "json"
    }

    response = requests.get(path, params=query_params)
    print(wonder)
    print("Lat:", response.json()[0]["lat"])
    print("Lon:", response.json()[0]["lon"])
    print("************")
    time.sleep(0.5)