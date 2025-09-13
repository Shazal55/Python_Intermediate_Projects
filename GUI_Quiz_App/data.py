import requests
response = requests.get("https://opentdb.com/api.php?amount=10&category=19&type=boolean")
response.raise_for_status()
response=response.json()
question_data = response['results']

