import tensorflow as tf
import tensorflow_hub as hub
import cv2
from tqdm import tqdm
import shutil

detector = hub.load("https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1").signatures['default']

images = os.listdir('images/')
images.remove('.DS_Store')
len(images)

images_with_no_person = []

for image in tqdm(images):
    found = False

    img = cv2.imread(os.path.join('images/', image))
    img = img / 255
    img_tensor = tf.convert_to_tensor(img, dtype=tf.float32)
    img_tensor = tf.expand_dims(img_tensor, axis=0)

    detector_output = detector(img_tensor)

    scores = detector_output['detection_scores'].numpy()
    classes = detector_output['detection_class_entities'].numpy()

    for i in range(len(scores)):
        score = scores[i]
        if score < 0.2:
            continue
        label = classes[i].decode('UTF-8')
        if label in ['Man', 'Woman', 'Person']:
            found = True

    if not found:
        images_with_no_person.append(image)

for image in tqdm(images_with_no_person):
    shutil.copyfile(f'images/{image}', f'nonathlete_images/{image}')

print('These images do not have any athletes : ', images_with_no_person)