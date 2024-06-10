import os
import requests
import tempfile


def download_urls_from_file(file_path, output_directory):
    with open(file_path, 'r') as f:
        urls = f.readlines()
    
    urls = map(str.strip, urls)
    for url in urls:
        file_name = url.split('/')[-1]
        output_path = os.path.join(output_directory, file_name)
        if os.path.exists(output_path):
            print(f"Skipping {file_name}. File already downloaded.")
            continue
        try:
            print(f"Attempting to download: {url}")
            response = requests.get(url)
            if response.status_code == 200:
                with tempfile.NamedTemporaryFile(delete=False, dir=output_directory) as tmp_file:
                    temp_path = tmp_file.name
                    print(f"Downloading to {temp_path}")
                    tmp_file.write(response.content)
                os.rename(temp_path, output_path)
                # with open(f"{output_directory}/{file_name}", 'wb') as output_file:
                #     output_file.write(response.content)
                print(f"Downloaded {file_name}")
            else:
                print(f"Failed to download {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")

if __name__ == "__main__":
    file_path = "download2.txt" 
    output_directory = "/Users/cristina/maps/mapant_local_data/in" 
    download_urls_from_file(file_path, output_directory)
