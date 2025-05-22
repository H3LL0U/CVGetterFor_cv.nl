
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
import os


def createCVImagesFromURL(url, image_save_path= "output_image.png",max_pages = 30)-> list[str] | str:
    '''
    return: list[str] #with paths
    if it succeeded in creating images

    return: message:str
    if it did not succeed 
    '''

    try:
        screenshots, ellement_locations , ellement_sizes = getScreenshotsFromURL(url)
        all_images_paths = []
        if screenshots is None:
            return "A link you provided doesn't seem to be right"
        for screenshot, ellement_location , ellement_size in zip(screenshots, ellement_locations, ellement_sizes):


            crop_box = (ellement_location["x"],
                    ellement_location["y"],
                    ellement_location["x"] + ellement_size["width"],
                    ellement_location["y"] + ellement_size["height"])
        
        
            image = screenshot.crop(crop_box)
            tmp_counter = 0
            tmp_image_save_path = image_save_path
            while tmp_counter<max_pages:

                if not os.path.exists(tmp_image_save_path):
                    all_images_paths.append(tmp_image_save_path)
                    image.save(tmp_image_save_path)
                    break
                else:
                    if not tmp_counter:
                        base_image_path ,extension = os.path.splitext(tmp_image_save_path)

                    #image_save_path, extension = os.path.splitext(image_save_path)
                    tmp_counter+=1
                    tmp_image_save_path = f"{base_image_path}{tmp_counter}{extension}"
                    
            
    except KeyboardInterrupt:
        quit()
    except Exception as e:
        
        return "An error accured when trying to save the image"
    return all_images_paths
def getScreenshotsFromURL(url:str) -> list[list[PIL.PngImagePlugin.PngImageFile,int,int]] | None:
    '''
    returns a screenshot in bytes, 
    the location of the canvas ellement
    the size of the canvas ellement
    '''
    if not controlTheLink(url):
        return (None,None,None)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome( options=chrome_options)

    driver.set_window_size(3840, 4000)
    try:
        driver.get(url)
        driver.add_cookie({
        "name": "CookieConsent",
        "value": "{stamp:'ECu1yvx/8AxLKY3UwA2LFyvjNpuHJ23dsVNAfKWaHdOI5A0D2iqLwQ==',necessary:true,preferences:false,statistics:false,marketing:false,method:'explicit',ver:1,utc:1747932302144,region:'nl'}"
    })
    except KeyboardInterrupt:
        quit()
    except Exception as e:
        return (None,None,None)
    driver.refresh()
    time.sleep(1)
    CV_ellements = driver.find_elements(By.TAG_NAME, 'canvas')
    
    ellement_locations = []
    ellement_sizes = []
    screenshots = []
    for ellement in CV_ellements:
        ellement_locations.append(ellement.location)
        ellement_sizes.append( ellement.size)
        print(ellement.size)

        screenshots.append(Image.open(io.BytesIO(driver.get_screenshot_as_png())))
    
    
    
    
    
    
    

    return (screenshots , ellement_locations, ellement_sizes)

def controlTheLink(link:str):
    if ("cv.nl/d/"in link ) and link.endswith("/view"):
        return True
    return False