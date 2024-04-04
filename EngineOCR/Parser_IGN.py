import re
import cv2
import numpy as np
import pytesseract


class ParseStatsScreenShot(object):
    def __init__(self, image_path):
        print('loading image:', image_path)
        print()
        self.image = cv2.imread(image_path)

    def parse(self):
        ign, stats = self.crop_image()
        self.parse_stats(stats)
        self.parse_ign(ign)

    def filter_ign(self,parsed_text):
        print('Parsing player names...\n')
        pattern = r"\b\w{4,}\b"
        player_names = re.findall(pattern, parsed_text)
        print(player_names)
        return player_names

    def parse_ign(self,image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply thresholding to separate text from background
        _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        extracted_text = pytesseract.image_to_string(threshold)
        self.filter_ign(extracted_text)



    def crop_image(self):
        print('Preparing images for pre-processing...\n')
        # Read the image

        # Get the height of the image
        height = self.image.shape[0]

        # Define the height (Y-coordinate) at which you want to crop the image
        crop_height = 100  # Example height, adjust as needed

        # Crop the image at the specified height
        ign_portion = self.image[:crop_height, :]
        stats_portion = self.image[crop_height:, :]

        cv2.imwrite('temp/ignPortions.png', ign_portion)
        cv2.imwrite('temp/stats_portions.png', stats_portion)

        return ign_portion, stats_portion


    def parse_stats(self,image):
        # Add padding with the color of the top left pixel
        pad_color = image[0, 0, :]
        padded_img = np.full((image.shape[0] + 10, image.shape[1] + 10, 3), pad_color, np.uint8)
        padded_img[5:-5, 5:-5, :] = image

        cv2.floodFill(padded_img, None, (0, 0), (255, 100, 100), loDiff=(10, 10, 10), upDiff=(10, 10, 10))
        #cv2.imwrite('result7.png', padded_img)

        # Convert from BGR to HSV color space, and extract the saturation channel.
        hsv = cv2.cvtColor(padded_img, cv2.COLOR_BGR2HSV)
        s = hsv[:, :, 1]
        #cv2.imwrite('result8.png', s)

        # Apply thresholding (use `cv2.THRESH_OTSU` for automatic thresholding)
        thresh = cv2.threshold(s, 0, 255, cv2.THRESH_OTSU)[1]
        #cv2.imwrite('result9.png', thresh)

        # Pass preprocessed image to PyTesseract
        text = pytesseract.image_to_string(thresh, config="--psm 6")
        print("Parsed stats " + text)



obj = ParseStatsScreenShot('temp/Demo.png')
obj.parse()
