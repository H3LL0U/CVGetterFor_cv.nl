import technical_functions
# URL of the website

if __name__ == "__main__":
    url = input("Typ uw CV view link:")
    technical_functions.createCVImageFromURL(url=url)
    print(f"file has been saved to output_image.png")
    #print("Image saved as output_image.png")




