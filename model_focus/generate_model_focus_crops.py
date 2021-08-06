import logging
import shlex
import subprocess
import sys
from collections import namedtuple
from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

logging.basicConfig(level=logging.ERROR)

import platform
import os

from crop_api import ImageSaliencyModel, is_symmetric, parse_output, reservoir_sampling
from tqdm import tqdm

BIN_MAPS = {"Darwin": "mac", "Linux": "linux"}

HOME_DIR = Path("../").expanduser()

sys.path.append(str(HOME_DIR / "src"))
bin_dir = HOME_DIR / Path("./bin")
bin_path = bin_dir / BIN_MAPS[platform.system()] / "candidate_crops"
model_path = bin_dir / "fastgaze.vxm"
data_dir = HOME_DIR / Path("./data/")

model = ImageSaliencyModel(crop_binary_path=bin_path, crop_model_path=model_path)

# ---------------- For Image Files with athletes ----------------

imagefiles = os.listdir('images')
try:
    imagefiles.remove('.DS_Store')
except:
    pass
cropfiles = os.listdir('images_crops')

imagefiles = sorted(imagefiles)

count = 0
for crop in cropfiles:
    count += 1
    imagefiles.remove(crop)

print(f'Removed {count} already done crops')

for imagefile in imagefiles:
    print(f'Running {imagefile}')
    model.plot_img_crops('images/' / Path("./" + imagefile), topK=3)
    plt.savefig("images_crops/" + imagefile, bbox_inches="tight", facecolor='white')
    plt.close()

# ---------------- For Image Files without athletes ----------------

imagefiles = os.listdir('nonathlete_images')
try:
    imagefiles.remove('.DS_Store')
except:
    pass
cropfiles = os.listdir('nonathlete_crops')

imagefiles = sorted(imagefiles)

count = 0
for crop in cropfiles:
    count += 1
    imagefiles.remove(crop)

print(f'Removed {count} already done crops')

for imagefile in imagefiles:
    print(f'Running {imagefile}')
    model.plot_img_crops('nonathlete_images/' / Path("./" + imagefile), topK=3)
    plt.savefig("nonathlete_crops/" + imagefile, bbox_inches="tight", facecolor='white')
    plt.close()