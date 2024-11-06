import requests
from datetime import datetime

API_KEY = '3KG7fWCONVWVuydafgYetjESeRYhPH5XSAnGZyNg'
API_URL = "https://api.nasa.gov/planetary/apod"


def get_apod(date=None):
    """Fetch the Astronomy Picture of the Day (APOD) data."""
    params = {
        'api_key': API_KEY,
    }
    if date:
        params['date'] = date

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def validate_date(date_str):
    """Validate if the date is within the valid range."""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if date_obj < datetime(1995, 6, 16) or date_obj > datetime.today():
            return False
        return True
    except ValueError:
        return False
