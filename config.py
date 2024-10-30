import os
from datetime import datetime

LIMIT = 1

# Configuration parameters for data loading
DATA_FILE_PATH = 'data.json'                # Path to the input file with object names
OUTPUT_DIRECTORY = 'data'                   # Directory to save output files
OUTPUT_FORMAT = 'json'                      # Output file format: 'txt' or 'json'

# Settings for image background filtering
BACKGROUND_COLOR = 'white'                  # 'none' | 'transparent' | 'white' | 'black'
BORDER_RATIO = 0.1                          # Portion of the image border for background checking
THRESHOLD = 0.3                             # Threshold for determining acceptable background
