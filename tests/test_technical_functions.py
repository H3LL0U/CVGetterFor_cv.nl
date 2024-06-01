import pytest
from selenium.webdriver.remote.webelement import WebElement
from src.technical_functions import getScreenshotFromURL
from src.technical_functions import createCVImageFromURL
import unittest.mock as mock
from PIL import Image
import PIL.PngImagePlugin
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
        with io.BytesIO() as output:
            Image.new("RGBA", size = tuple(initial_size.values()), color=(256,0,0)).save(output, format="PNG")
            mock_screenshot =  output.getvalue()
        mock_driver.get_screenshot_as_png.return_value = mock_screenshot
        
        
        screenshot, location, size = getScreenshotFromURL("https://www.cv.nl/d/view")
        
        
        assert type(screenshot) is PIL.PngImagePlugin.PngImageFile
        assert location == initial_location
        assert size == initial_size

@pytest.mark.parametrize("whole_width, whole_height, width, height, x, y",  [(300,300,16,16,0,0),(30,30,5,5,1,2),(30,30,30,30,40,40), (3,3,1,1,1,3)])
def test_createCVImageFromURL(whole_width,  whole_height,  width, height, x, y, tmp_path):
    # Mock the return values of getScreenshotFromURL
    mock_screenshot = Image.new('RGBA', size=(whole_width,whole_height), color=(256,0,0))
    #with io.BytesIO() as output:
        #mock_screenshot.save(output, format="PNG")
        #mock_screenshot =  output.getvalue()
    mock_location = {"x": x, "y": y}
    mock_size = {"width": width, "height": height}
    
    with mock.patch('src.technical_functions.getScreenshotFromURL', return_value=(mock_screenshot, mock_location, mock_size)):
        # Call the function to test
        returned = createCVImageFromURL("https://www.cv.nl/d/view",  tmp_path / "test_output_image.png")
        
        # Verify the output image
        output_image = Image.open(tmp_path / "test_output_image.png")
        assert output_image.size == (mock_size["width"], mock_size["height"])
        assert returned


