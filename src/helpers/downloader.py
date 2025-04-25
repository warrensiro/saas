import requests
from pathlib import Path

def download_to_local(url: str, out_path:Path, parent_mkdir:bool=True) -> None:
    if not isinstance(out_path, Path):
        raise TypeError("out_path must be a Path object")
    if parent_mkdir:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses
        out_path.write_bytes(response.content) # Save the content to the file
        return True
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    
