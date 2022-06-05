"""
For Testing purposes
    Take image from user, crop the background and transform perspective
    from the perspective detect the word and return the array of word's
    bounding boxes
"""

import page
import words
from PIL import Image, ImageOps
import cv2
import os
from os import listdir

# if __name__ == "__checkout__":

# ----- code for GUI -----------
def segmentWords(fileInput):
# ------------------------------

    # correct code below --------------
    # # get the path/directory
    # folder_dir = "sample"
    # for images in os.listdir(folder_dir):

    #     # check if the image ends with png
    #     if (images.endswith(".jpeg")):
    #         input_file = str(images)

    # # print(input_file)
    # input_image = "sample/"+input_file

    # # User input page image 
    # image = cv2.cvtColor(cv2.imread(input_image), cv2.COLOR_BGR2RGB)
    # # image = cv2.imread('test.jpg')
    # ----------------------------------------

    # ---------------image input from GUI---------------
    image = cv2.cvtColor(cv2.imread(fileInput), cv2.COLOR_BGR2RGB)

    # Crop image and get bounding boxes
    crop = page.detection(image)
    boxes = words.detection(crop)
    lines = words.sort_words(boxes)

    # Saving the bounded words from the page image in sorted way
    i = 0
    for line in lines:
        text = crop.copy()
        for (x1, y1, x2, y2) in line:
            # roi = text[y1:y2, x1:x2]
            save = Image.fromarray(text[y1:y2, x1:x2])
            # print(i)
            save.save("segmented_words/segment" + str(i) + ".jpeg")
            ImageOps.expand(Image.open("segmented_words/segment" + str(i) + ".jpeg"),border=300,fill='white').save("segmented_words_border/segment" + str(i) + ".jpeg")
            i += 1



