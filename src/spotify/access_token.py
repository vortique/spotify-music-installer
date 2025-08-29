import requests
import base64
import os
from pathlib import Path
from datetime import datetime, timedelta

from src.utils.yaml_utils import load, dump

def request_access_token(client_id: str, client_secret: str):
    
    yaml_path = os.path.join(Path(__file__).parents[2], "api.yaml")

    yaml_data = load(yaml_path)

    url = yaml_data["access-token"]["requesting-url"]

    auth_str = f"{client_id}:{client_secret}"

    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {b64_auth_str}"
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers=headers, data=data)

    print(response.status_code)

    if response.status_code == 200:
        expiring_date = datetime.now() + timedelta(hours=1)

        yaml_data["access-token"]["access-token"] = response.json()["access_token"]
        yaml_data["access-token"]["expiring-date"] = expiring_date.isoformat()

        dump(yaml_path, yaml_data)

        return response.status_code
    else:
        return response.status_code


def return_access_token():
    yaml_data = load(os.path.join(Path(__file__).parents[2], "api.yaml"))

    if (yaml_data["access-token"]["access-token"] == ""):
        print("Access token not avaible. Requesting new...")

        if request_access_token(yaml_data["client-id"], yaml_data["client-secret"]) == 200:
            print("New access token successfully granted.")
            yaml_data = load(os.path.join(Path(__file__).parents[2], "api.yaml"))

            return yaml_data["access-token"]["access-token"]
        else:
            raise requests.HTTPError
    elif datetime.fromisoformat(yaml_data["access-token"]["expiring-date"]) < datetime.now():
        print("Access token expired. Requesting new...")

        if request_access_token(yaml_data["client-id"], yaml_data["client-secret"]) == 200:
            print("New access token successfully granted.")
            yaml_data = load(os.path.join(Path(__file__).parents[2], "api.yaml"))

            return yaml_data["access-token"]["access-token"]
        else:
            raise requests.HTTPError
    else:
        print("Access token availble.")

        return yaml_data["access-token"]["access-token"]