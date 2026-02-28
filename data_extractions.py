import requests
import json
import os 

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("YOUTUBE_API")
chanel_handle = "MrBeast"

BASE_URL = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={chanel_handle}&key={api_key}"


def get_playlist_id(url):
    """
    Function to parse JSON and get Playlist Id for further data exctracion
    """
    try: 
        response = requests.get(url)
        #Check if request return 200 status code
        response.raise_for_status()
        
        data = response.json()
        playlist_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
            
        return playlist_id
    
    except requests.exceptions.HTTPError as e:
        raise e

if __name__ == "__main__":
    pass 