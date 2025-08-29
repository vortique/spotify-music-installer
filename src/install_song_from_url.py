import requests
from pathlib import Path
import os

from src.spotify.access_token import return_access_token
from src.utils.yaml_utils import load
from src.utils.fetch_url import fetch_url
from src.yt_dlp.installers import install_from_name

def install_from_url(url: str):
    api_yaml_path: str = os.path.join(Path(__file__).parents[1], "api.yaml")

    yaml_data: dict[str, str] = load(api_yaml_path)

    track_id: str = fetch_url(url)

    track_id_token = "{track_id}"

    access_token = ""
    
    try:
        access_token: str = return_access_token()
    except requests.HTTPError:
        print("Can not request the access token.")

        return

    spotify_api_url: str = yaml_data["spotify-api-url"]
    get_track_endpoint: str = yaml_data["api-endpoints"]["get-track"].replace(track_id_token, track_id)

    url = f"{spotify_api_url}{get_track_endpoint}?market=US"

    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.get(url, headers=headers)

    if (response.status_code == 200):
        response_data = response.json()

        track_name = response_data["album"]["name"]
        track_artists = ""

        for artist in response_data["artists"]:
            track_artists += artist["name"] + " "

        print(f"Found track: {track_name}")

        install_from_name(track_name + " " +track_artists)

        print("Installed.")
    else:
        print(f"ERROR {response.status_code}")