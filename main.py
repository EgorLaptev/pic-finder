import json
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup


def load_names(file_path):
    """Load product names from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return [name.strip() for name in f]


def fetch_image_link(name):
    """Fetch the first image link from Google Images search for a given product name."""
    url = f'https://www.google.com/search?q={name}&tbm=isch'  # Исправил ${name} на {name}
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'lxml')
    images = soup.findAll('img')
    return images[1].get('src') if len(images) > 1 else ""


def save_links(links, directory):
    """Save the list of image links to a file."""
    timestamp = datetime.now().strftime('%Y-%m-%d-%H%M%S')
    output_path = f'{directory}/links-{timestamp}.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(links))
    return output_path


def main(input_file, output_directory):
    names = load_names(input_file)
    links = []
    counter = 0
    success = 0

    print(f'🌀 Start searching')
    start_time = time.time()

    for name in names:
        counter += 1
        link = fetch_image_link(name)
        links.append(link)

        if link:
            success += 1
            print(f'[{counter}/{len(names)}] 🟢 {name}: {link}')
        else:
            print(f'[{counter}/{len(names)}] 🔴 {name}')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'\n✅ [{success}/{len(names)}] Finished processing in {elapsed_time:.2f} seconds')

    output_file = save_links(links, output_directory)
    print(f'📄 Links saved to: {output_file}')


if __name__ == "__main__":
    main('data.txt', 'data')
