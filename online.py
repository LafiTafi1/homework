import requests

URL = 'https://api.freecurrencyapi.com/v1/latest?apikey='
API_KEY = 'fca_live_AR6ltmuG6jDiju99Gjp935tVEJLgkC6ViNH84SFA'

def get_actual_currencies():
    response = requests.get(URL + API_KEY)
    return response.json()

