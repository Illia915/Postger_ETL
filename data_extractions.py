import requests
import json
import os 

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("YOUTUBE_API")
chanel_handle = "MrBeast"
BASE_URL_PLAYLISTS_LIST = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={chanel_handle}&key={api_key}"
max_results = 50 
def get_playlist_id(url: str):
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

 

def get_video_ids(playlist_id, max_result):
    
    video_ids = []
    pageToken = None
    BASE_URL_VIDEO_LIST = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=ContentDetails&maxResults={max_result}&playlistId={playlist_id}&key={api_key}"

    try : 
        while True:
            url = BASE_URL_VIDEO_LIST
            
            if pageToken:
                url += f"&pageToken={pageToken}"
                
            response = requests.get(url)
            
            response.raise_for_status()
            
            data = response.json()
            
            for item in data.get('items', []):
                video_id = item['contentDetails']['videoId']
                video_ids.append(video_id)
                
            pageToken = data.get('nextPageToken')
            
            if not pageToken:
                break
            
        return video_ids
            
            
    except requests.exceptions.HTTPError as e:
        raise e
    


if __name__ == "__main__":
    playlist_id = get_playlist_id(BASE_URL_PLAYLISTS_LIST)
    get_video_ids(playlist_id,max_results)
    