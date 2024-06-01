import pytest
from selenium.webdriver.remote.webelement import WebElement
from src.technical_functions import getScreenshotFromURL
from src.technical_functions import createCVImageFromURL
import unittest.mock as mock
from PIL import Image
import os
import io

@pytest.mark.parametrize("initial_location, initial_size",[({"x": 100, "y": 200},{"width": 300, "height": 400})])
def test_getScreenshotFromURL(initial_location, initial_size):
    
    mock_element = mock.MagicMock()
    mock_element.location = initial_location
    mock_element.size = initial_size
    
    
    with mock.patch('selenium.webdriver.Chrome') as MockWebDriver:
        mock_driver = MockWebDriver.return_value
        mock_driver.find_element.return_value = mock_element
        mock_driver.get_screenshot_as_png.return_value = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xff\xa6\x00\x00\x00\x19tEXtSoftware\x00Adobe ImageReadyq\xc9e<\x00\x00\x00\x18IDATx\xdab\xfc\xff\xff?\x03\x05\x00\x00\x0b\x00\x01p\xfc*\n\x00\x00\x00\x00IEND\xaeB`\x82'
        
        
        screenshot, location, size = getScreenshotFromURL("http://example.com")
        
        
        assert type(screenshot) == bytes 
        assert location == initial_location
        assert size == initial_size

@pytest.mark.parametrize("whole_width, whole_height, width, height, x, y",  [(300,300,16,16,0,0),(30,30,5,5,1,2),(30,30,30,30,40,40), (3,3,1,1,1,3)])
def test_createCVImageFromURL(whole_width,  whole_height,  width, height, x, y, tmp_path):
    # Mock the return values of getScreenshotFromURL
    mock_screenshot = Image.new('RGBA', size=(whole_width,whole_height), color=(256,0,0))
    with io.BytesIO() as output:
        mock_screenshot.save(output, format="PNG")
        mock_screenshot =  output.getvalue()
    mock_location = {"x": x, "y": y}
    mock_size = {"width": width, "height": height}
    
    with mock.patch('src.technical_functions.getScreenshotFromURL', return_value=(mock_screenshot, mock_location, mock_size)):
        # Call the function to test
        createCVImageFromURL("http://example.com",   "test_output_image.png")
        
        # Verify the output image
        output_image = Image.open(  "test_output_image.png")
        assert output_image.size == (mock_size["width"], mock_size["height"])


