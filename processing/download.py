import requests

def download_urls_from_file(file_path, output_directory):
    with open(file_path, 'r') as f:
        urls = f.readlines()

    urls = map(str.strip, urls)
    for url in urls:
        try:
            print(f"Attempting to download: {url}")
            response = requests.get(url)
            if response.status_code == 200:
                file_name = url.split('/')[-1]
                with open(f"{output_directory}/{file_name}", 'wb') as output_file:
                    output_file.write(response.content)
                print(f"Downloaded {file_name}")
            else:
                print(f"Failed to download {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")

if __name__ == "__main__":
    file_path = "data.txt" 
    output_directory = "in" 
    download_urls_from_file(file_path, output_directory)
