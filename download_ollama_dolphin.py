import requests
import os

url = "https://ollama.com/library/dolphin-llama3"
filename = "ollama_run_dolphin-llama3"
filesize = 4700000000  # 4.7 GB

# Set the timeout to a large value to avoid timeouts on slow internet
timeout = 3600  # 1 hour

# Create a directory to store the downloaded file
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# Download the file
response = requests.get(url, stream=True, timeout=timeout)

# Check if the download was successful
if response.status_code == 200:
    with open(os.path.join("downloads", filename), "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
    print(f"Downloaded {filename} successfully!")
else:
    print(f"Failed to download {filename}. Status code: {response.status_code}")
