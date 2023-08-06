import cv2
from PIL import Image
import pytesseract
import requests
from bs4 import BeautifulSoup
import time
import base64
from io import BytesIO


headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}

def pictureSearch(link):
    starter = link.find(',')
    image_data = link[starter+1:]
    image_data = bytes(image_data, encoding="ascii")
    im = Image.open(BytesIO(base64.b64decode(image_data)))
    im.save('image.jpg')
    get_picture()

def ocr_core(img):
    text = pytesseract.image_to_string(img, lang='eng')
    return text

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def get_picture():
        try:
            returnImg = cv2.imread('image.jpg')
            img = get_grayscale(returnImg)
            img = remove_noise(img)
            img = thresholding(img)
            global kilometers
            km_string = (ocr_core(img))
            km_string = km_string.split('Range', 1)[1]
            km_string = km_string.split('km', 1)[0]
            km_string = km_string.strip()
            km_string = int(km_string)
            kilometers = km_string
            print(kilometers)
        except:
            print('Picture did not render, please take another picture.')
    




