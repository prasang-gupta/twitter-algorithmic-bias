import selenium
import time
import io
import requests
import hashlib
from PIL import Image
from selenium import webdriver

import requests
from bs4 import BeautifulSoup
import urllib.request

required_count = 500

urls = {
    "archery" : "https://www.gettyimages.in/photos/archery-tokyo-2020?phrase=archery%20tokyo%202020&sort=mostpopular",
    "badminton" : "https://www.gettyimages.in/photos/badminton-tokyo-2020?phrase=badminton%20tokyo%202020&sort=mostpopular",
    "basketball" : "https://www.gettyimages.in/photos/basketball-tokyo-2020?phrase=basketball%20tokyo%202020&sort=mostpopular",
    "boxing" : "https://www.gettyimages.in/photos/boxing-tokyo-2020?phrase=boxing%20tokyo%202020&sort=mostpopular",
    "gymnastics" : "https://www.gettyimages.in/photos/gymnastics-tokyo-2020?phrase=gymnastics%20tokyo%202020&sort=mostpopular",
    "hockey" : "https://www.gettyimages.in/photos/hockey-tokyo-2020?phrase=hockey%20tokyo%202020&sort=mostpopular",
    "swimming" : "https://www.gettyimages.in/photos/swimming-tokyo-2020?phrase=swimming%20tokyo%202020&sort=mostpopular",
    "tennis" : "https://www.gettyimages.in/photos/tennis-tokyo-2020?phrase=tennis%20tokyo%202020&sort=mostpopular",
    "tt" : "https://www.gettyimages.in/photos/table-tennis-tokyo-2020?phrase=table%20tennis%20tokyo%202020&sort=mostpopular",
    "volleyball" : "https://www.gettyimages.in/photos/volleyball-tokyo-2020?phrase=volleyball%20tokyo%202020&sort=mostpopular"
}

for sport in urls.keys():
    print("Currently downloading :", sport)
    page = 0
    count = 0

    while True:
        get_soup = requests.get(
            urls[sport] + f"&page={page}")
        soup = BeautifulSoup(get_soup.text, "html.parser")
        pics = soup.findAll("img", {"class": "gallery-asset__thumb gallery-mosaic-asset__thumb"})
        print(f'Found {len(pics)} pics ...')
        for pic in pics:
            try:
                urllib.request.urlretrieve(pic.get("src"), f"images/{sport}_{count:03d}.jpg")
                count += 1
            except:
                pass
            if count >= required_count:
                break
        if count >= required_count:
            break
        page +=1