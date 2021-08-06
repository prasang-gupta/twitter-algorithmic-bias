import numpy as np
import cv2
import os

images = os.listdir('../../sensitivity_analysis/10/')
images.remove('.DS_Store')

for image in images:
    img = cv2.imread(os.path.join('../../sensitivity_analysis/10/', image))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join('10gray/', image), gray)

images = os.listdir('../../sensitivity_analysis/11/')
images.remove('.DS_Store')

for image in images:
    img = cv2.imread(os.path.join('../../sensitivity_analysis/11/', image))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join('11gray/', image), gray)