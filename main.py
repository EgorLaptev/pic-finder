import os
import json
import time
import requests
from config import *
from datetime import datetime
from bs4 import BeautifulSoup
from validator import check_background


def load_names(file_path):
    """Load product names from a file in either text or JSON format."""
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.json':
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("data", [])
    else:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [name.strip() for name in f]


def fetch_image_link(query):
    """Fetch the first image link from Google Images search for a given product name."""
    url = f'https://www.google.com/search?q={query}&tbm=isch'
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'lxml')
    images = soup.findAll('img')

    links = []

    saved_count = 0

    # validate images
    for image in images[1:]:
        link = image.get('src')
        if saved_count < LIMIT and check_background(link, BACKGROUND_COLOR, BORDER_RATIO, THRESHOLD):
            links.append(link)
            saved_count += 1

    return links


def save_links(links, directory, output_format="txt"):
    """Save the list of image links to a file in either text or JSON format."""
    timestamp = datetime.now().strftime('%Y-%m-%d-%H%M%S')
    output_path = f'{directory}/links-{timestamp}.{output_format}'

    if output_format == "json":
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({"links": links}, f, ensure_ascii=False, indent=4)
    else:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(['\n'.join(link) for link in links]))

    return output_path


def main(input_file, output_directory, output_format="txt"):
    names = load_names(input_file)
    links = []
    counter = 0
    success = 0

    print(f'🌀 Start searching')
    start_time = time.time()

    for name in names:
        counter += 1
        resp = fetch_image_link(name)
        links.append(resp)

        if len(resp):
            success += 1
            print(f'[{counter}/{len(names)}] 🟢 {name}:\n{'\n'.join(resp)}')
        else:
            print(f'[{counter}/{len(names)}] 🔴 {name}')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'\n✅ [{success}/{len(names)}] Finished processing in {elapsed_time:.2f} seconds')

    output_file = save_links(links, output_directory, output_format)
    print(f'📄 Links saved to: {output_file}')


if __name__ == "__main__":
    main(DATA_FILE_PATH, OUTPUT_DIRECTORY, OUTPUT_FORMAT)
