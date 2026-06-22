import os

import matplotlib as mpl


def read_styles_in_folders(root_path):
    """
    Reads all stylesheets in the given path and its subfolders.

    Parameters
    ----------
    root_path : str
        Path to the root folder containing the stylesheets and other subfolders
        with stylesheets.

    Returns
    -------
    stylesheets : dict
        Dictionary of stylesheets in the form of {style_name: rcParams}.
        Should be compatible with matplotlib's plt.style.library dictionary.
    """
    stylesheets = {}  # plt.style.library is a dictionary
    for folder, _, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.endswith(".mplstyle"):
                style_path = os.path.join(folder, filename)
                style_name = os.path.splitext(filename)[0]
                stylesheets[style_name] = mpl.rc_params_from_file(
                    style_path, use_default_template=False
                )
    return stylesheets
