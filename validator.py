from PIL import Image
import requests
from io import BytesIO


def check_background(image_url, border_ratio=0.1, threshold=0.9):
    """
    Checks whether the background of the image is predominantly white or transparent

    Parameters:
    - border_ratio: the proportion of the width and height of the border for analysis (for example, 0.1 for 10% of the outskirts).
    - threshold: the minimum proportion of white or transparent pixels on the border to confirm the background (for example, 0.9 for 90%).
    """
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content)).convert("RGBA")

        width, height = img.size
        pixels = img.load()

        border_width = int(width * border_ratio)
        border_height = int(height * border_ratio)

        total_border_pixels = 0
        white_or_transparent_pixels = 0

        for x in range(width):
            for y in range(height):
                if x < border_width or x >= width - border_width or y < border_height or y >= height - border_height:
                    total_border_pixels += 1
                    r, g, b, a = pixels[x, y]

                    if a == 0 or (r > 240 and g > 240 and b > 240):
                        white_or_transparent_pixels += 1

        border_coverage = white_or_transparent_pixels / total_border_pixels

        return border_coverage > threshold

    except Exception as e:
        return False
