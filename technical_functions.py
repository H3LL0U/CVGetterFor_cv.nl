
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import io
import time


def createCVImageFromURL(url, image_save_path= "output_image.png"):


    

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x2000")
    driver = webdriver.Chrome( options=chrome_options)
    driver.get(url)
    try:
        CV_ellement = driver.find_element(By.TAG_NAME, 'canvas')
        #WebDriverWait(driver, 10).until(CV_ellement)
        ellement_location = CV_ellement.location
        ellement_size = CV_ellement.size
    except Exception as e:
        raise e

    screenshot = driver.get_screenshot_as_png()
    driver.quit()
    image = Image.open(io.BytesIO(screenshot))

    crop_box = (ellement_location["x"]+1,
            ellement_location["y"]+1,
            ellement_location["x"] + ellement_size["width"]+1,
            ellement_location["y"] + ellement_size["height"]+1)
    
    print(crop_box)
    image = image.crop(crop_box)
    image.save(image_save_path)
