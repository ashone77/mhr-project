import argparse
import cv2

import numpy as np
from numpy import genfromtxt
import operator
from keras.models import load_model

from functions import clean, read_transparent_png


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image to be scanned")
args = vars(ap.parse_args())



model = load_model("model.h5")

image = cv2.imread(args["image"], cv2.IMREAD_UNCHANGED)
if image.shape[2] == 4:
    image = read_transparent_png(args["image"])
image = clean(image)
cv2.imshow('gray', image)
cv2.waitKey(0)

def predict(img):
    image_data = img
    dataset = np.asarray(image_data)
    dataset = dataset.reshape((-1, 32, 32, 1)).astype(np.float32)
    print(dataset.shape)
    a = model.predict(dataset)[0]

    classes = np.genfromtxt('classes.csv', delimiter=',')[:, 1].astype(int)

    print(classes)
    new = dict(zip(classes, a))
    res = sorted(new.items(), key=operator.itemgetter(1), reverse=True)

    print("#########***#########")
    print("Imagefile = ", args['image'])
    print("Character = ", int(res[0][0]))
    print("Confidence = ", res[0][1] * 100, "%")
    if res[0][1] < 1:
        print("Other predictions")
        for newtemp in res:
            print("Character = ", newtemp[0])
            print("Confidence = ", newtemp[1] * 100, "%")
    
    global rec_char
    rec_char = res[0][0]

def printChar(rec_char):
    alphabet_list = {
        "3333":"അ",
        "3334":"ആ",
        "3335":"ഇ",
        "3337":"ഉ",
        "3342":"എ",
        "3343":"ഏ",
        "3346":"ഒ",
        "3349":"ക",
        "3350":"ഖ",
        "3351":"ഗ",
        "3352":"ഘ",
        "3353":"ങ",
        "3354":"ച",
        "3355":"ഛ",
        "3356":"ജ",
        "3357":"ഝ",
        "3358":"ഞ",
        "3359":"ട",
        "3360":"ഠ",
        "3361":"ഡ",
        "3362":"ഢ",
        "3363":"ണ",
        "3364":"ത",
        "3365":"ഥ",
        "3366":"ദ",
        "3367":"ധ",
        "3368":"ന",
        "3370":"പ",
        "3371":"ഫ",
        "3372":"ബ",
        "3373":"ഭ",
        "3374":"മ",
        "3375":"യ",
        "3376":"ര",
        "3377":"റ",
        "3378":"ല",
        "3379":"ള",
        "3380":"ഴ",
        "3381":"വ",
        "3382":"ശ",
        "3383":"ഷ",
        "3384":"സ",
        "3385":"ഹ",
        "3452":"൪",
        "3451":"൯",
        "3450":"ൺ",
        "3453":"ൽ",
        "3454":"ൾ",
    }

    character = str(rec_char)

    if character in alphabet_list:
        print(alphabet_list[character])

    with open("output.txt", "a") as file_object:
        file_object.write(alphabet_list[character])


predict(image)

printChar(rec_char)