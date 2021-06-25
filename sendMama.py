import requests
import json

#get your mama jokes from API
def get_mama():
  response = requests.get("https://api.yomomma.info")
  json_data = json.loads(response.text)
  quote = json_data['joke']
  return quote