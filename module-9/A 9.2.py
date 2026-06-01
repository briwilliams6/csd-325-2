import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
#comment this one out for formatting, but is the original format
print(response.json())

import json
def jprint(obj):
    text=json.dumps(obj, sort_keys=True, indent=4)
    print(text)
jprint(response.json())