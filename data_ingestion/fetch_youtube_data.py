import requests

API_KEY = 'YOUR_YOUTUBE_API_KEY'
CHANNEL_ID = 'YOUR_CHANNEL_ID'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/channels'

def fetch_youtube_data():
    url = f"{YOUTUBE_API_URL}?part=statistics&id={CHANNEL_ID}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data
