import os  # pathlib.Path.walk not available in Python <3.12
import matplotlib.pyplot as plt

import scienceplots
from .styles_discovery import read_styles_in_folders

# register the bundled stylesheets in the matplotlib style library
scienceplots_path = scienceplots.__path__[0]
styles_path = os.path.join(scienceplots_path, "styles")

# Reads styles in /styles folder and all subfolders
stylesheets = read_styles_in_folders(styles_path)

# Update dictionary of styles - plt.style.library
for name, style in stylesheets.items():
    plt.style.library.setdefault(name, {}).update(style)

plt.style.available[:] = sorted(plt.style.library.keys())
