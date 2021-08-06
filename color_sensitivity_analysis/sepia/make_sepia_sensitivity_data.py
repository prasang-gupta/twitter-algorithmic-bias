import numpy as np
import cv2
import os

images = os.listdir('../../sensitivity_analysis/10/')
images.remove('.DS_Store')

for image in images:
    img = cv2.imread(os.path.join('../../sensitivity_analysis/10/', image))
    img = np.array(img, dtype=np.float64) # converting to float to prevent loss
    img = cv2.transform(img, np.matrix([[0.272, 0.534, 0.131],
                                        [0.349, 0.686, 0.168],
                                        [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
    img[np.where(img > 255)] = 255 # normalizing values greater than 255 to 255
    img = np.array(img, dtype=np.uint8) # converting back to int
    cv2.imwrite(os.path.join('10sepia/', image), img)

images = os.listdir('../../sensitivity_analysis/11/')
images.remove('.DS_Store')

for image in images:
    img = cv2.imread(os.path.join('../../sensitivity_analysis/11/', image))
    img = np.array(img, dtype=np.float64) # converting to float to prevent loss
    img = cv2.transform(img, np.matrix([[0.272, 0.534, 0.131],
                                        [0.349, 0.686, 0.168],
                                        [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
    img[np.where(img > 255)] = 255 # normalizing values greater than 255 to 255
    img = np.array(img, dtype=np.uint8) # converting back to int
    cv2.imwrite(os.path.join('11sepia/', image), img)