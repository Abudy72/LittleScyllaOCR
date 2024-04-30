import re
import cv2
import numpy as np
import pytesseract


def initial_crop(image):
    print('Pre-processing Images...\n')
    height = image.shape[0]

    crop_height = 90  # Example height, adjust as needed

    ign_portion = image[:crop_height, :]
    stats_portion = image[crop_height:, :]

    cv2.imwrite('temp/ignPortions.png', ign_portion)
    cv2.imwrite('temp/stats_portions.png', stats_portion)

    return ign_portion, stats_portion


def ocr_image(cropped_image, flag):
    pad_color = cropped_image[0, 0, :]
    padded_img = np.full((cropped_image.shape[0] + 10, cropped_image.shape[1] + 10, 3), pad_color, np.uint8)
    padded_img[5:-5, 5:-5, :] = cropped_image
    cv2.floodFill(padded_img, None, (0, 0), (255, 100, 100), loDiff=(10, 10, 10), upDiff=(10, 10, 10))
    hsv = cv2.cvtColor(padded_img, cv2.COLOR_BGR2HSV)
    s = hsv[:, :, 1]

    thresh = cv2.threshold(s, 0, 255, cv2.THRESH_OTSU)[1]
    # Pass preprocessed image to PyTesseract
    if flag:
        text = pytesseract.image_to_string(s, lang='eng_best', config="--psm 6")
    else:
        text = pytesseract.image_to_string(thresh, lang='digits',
                                           config="--psm 6 -c tessedit_char_whitelist=0123456789")

    if text == '': text = '0'

    print(sanitize_result(text.strip()), end=' ')


def sanitize_result(text):
    # Define the regex pattern
    pattern = r'[^0-9/]|C|o|O'
    # Replace matches with an empty string
    processed_text = re.sub(r'o+', lambda x: '0' * len(x.group()), text)
    processed_text = re.sub(pattern, '', processed_text)
    return processed_text


def recursive_crop(segment, start_height, start_width):
    # Crop the image based on the specified dimensions
    crop_height = 40
    crop_width = 125
    return segment[start_height:start_height + crop_height, start_width:start_width + crop_width]


def process_image(image):
    currHeight, currWidth = 0, 0
    while currHeight <= 400 and currWidth <= 1125:
        #print('\nCurr Height: {}, Curr Width: {}'.format(currHeight, currWidth) + '\n')
        cropped_image = recursive_crop(image, currHeight, currWidth)  #400,200

        if currHeight == 40:
            ocr_image(cropped_image, True)
        else:
            ocr_image(crop_segment(cropped_image), False)

        if currWidth >= 1125:
            currHeight += 40
            currWidth = 0
            print()
        else:
            currWidth += 125


def crop_segment(segmented_image):
    # Crop the image based on the specified dimensions
    crop_height = 40
    crop_width = 510
    cropped_image = segmented_image[10:crop_height, -crop_width:]
    return cropped_image


def resize_image(image):
    resized_image = cv2.resize(image, (1265, 534), interpolation=cv2.INTER_AREA)
    return resized_image


def start_OCR(image):
    rimage = resize_image(image)
    ign_portions, stats_portion = initial_crop(rimage)
    process_image(stats_portion)


def debug_ocr(pathToImage):
    image = cv2.imread(pathToImage)
    image = resize_image(image)

    def save_debug_image(processed_image, image_name):
        cv2.imwrite('temp/debug/{}'.format(image_name), processed_image)

    def debug(stats_p):
        currHeight, currWidth, cell_number = 0, 0, 0
        while currHeight <= 400 and currWidth <= 1125:
            cropped_image = recursive_crop(stats_p, currHeight, currWidth)  # 400,200
            save_debug_image(crop_segment(cropped_image), 'Cell: {}.png'.format(cell_number))

            if currHeight == 40:
                ocr_image(cropped_image, True)
            else:
                ocr_image(crop_segment(cropped_image), False)
            if currWidth >= 1125:
                currHeight += 40
                currWidth = 0
                print()
            else:
                currWidth += 125
            cell_number += 1

    ign_portions, stats_portion = initial_crop(image)
    save_debug_image(ign_portions, 'ignPortions.png')
    save_debug_image(stats_portion, 'statsPortion.png')
    debug(stats_portion)


start_OCR(cv2.imread('/home/abdella/Pictures/Screenshots/R.png'))
#debug_ocr('/home/abdella/Pictures/Screenshots/Crete_G1_S3.png')
