
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


    
    screenshot, ellement_location , ellement_size = getScreenshotFromURL(url)
    image = Image.open(io.BytesIO(screenshot))

    crop_box = (ellement_location["x"],
            ellement_location["y"],
            ellement_location["x"] + ellement_size["width"],
            ellement_location["y"] + ellement_size["height"])
    
    
    image = image.crop(crop_box)
    image.save(image_save_path)
def getScreenshotFromURL(url:str) -> list[bytes,int,int]:
    '''
    returns a screenshot in bytes, 
    the location of the canvas ellement
    the size of the canvas ellement
    '''
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x2000")
    driver = webdriver.Chrome( options=chrome_options)
    driver.get(url)
    
    CV_ellement = driver.find_element(By.TAG_NAME, 'canvas')
    #WebDriverWait(driver, 10).until(CV_ellement)
    ellement_location = CV_ellement.location
    ellement_size = CV_ellement.size


    screenshot = driver.get_screenshot_as_png()
    driver.quit()
    
    

    return (screenshot , ellement_location, ellement_size)
