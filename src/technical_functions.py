
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import io
import time
import PIL.PngImagePlugin


def createCVImageFromURL(url, image_save_path= "output_image.png")-> bool | str:
    '''
    return: True 
    if it succeeded in creating an image

    return: message:str
    if it did not succeed 
    '''

    try:
        screenshot, ellement_location , ellement_size = getScreenshotFromURL(url)
        if not getScreenshotFromURL:
            return "A link you provided doesn't seem to be right"

        crop_box = (ellement_location["x"],
                ellement_location["y"],
                ellement_location["x"] + ellement_size["width"],
                ellement_location["y"] + ellement_size["height"])
    
    
        image = screenshot.crop(crop_box)
        image.save(image_save_path)
    except KeyboardInterrupt:
        quit()
    except Exception:
        return "An error accured when trying to save the image"
    return True
def getScreenshotFromURL(url:str) -> list[PIL.PngImagePlugin.PngImageFile,int,int] | None:
    '''
    returns a screenshot in bytes, 
    the location of the canvas ellement
    the size of the canvas ellement
    '''
    if not controlTheLink(url):
        return None
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x2000")
    driver = webdriver.Chrome( options=chrome_options)

    try:
        driver.get(url)
    except KeyboardInterrupt:
        quit()
    except Exception as e:
        return None
        
    CV_ellement = driver.find_element(By.TAG_NAME, 'canvas')
    
    ellement_location = CV_ellement.location
    ellement_size = CV_ellement.size


    screenshot = driver.get_screenshot_as_png()
    screenshot = Image.open(io.BytesIO(screenshot))
    
    
    
    

    return (screenshot , ellement_location, ellement_size)

def controlTheLink(link:str):
    if ("cv.nl/d/"in link ) and link.endswith("/view"):
        return True
    return False