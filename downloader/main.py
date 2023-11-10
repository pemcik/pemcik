import requests
from tqdm import tqdm

def download_file(url, destination):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

    with open(destination, 'wb') as file, progress_bar:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()

if __name__ == "__main__":
    file_url = input("Please input link to file: ")
    destination_path = input("write destination folder and file name: ")

    print(f"Downloading {file_url} to {destination_path}")
    download_file(file_url, destination_path)
    print("Download complete!")
