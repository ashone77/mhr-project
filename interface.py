import tkinter.filedialog as filedialog
import tkinter as tk
from tkinter import *
import os, glob
from PIL import Image, ImageTk
from checkout import segmentWords
from main import characterSegmentation
import time


master = tk.Tk()
master.title("Malayalam Handwriting Recognition")

appName = tk.Label(text="Malayalam Handwriting Recognition", font=("Helvetica", 20))
appName.pack()

#  filetypes = [("jpeg files", "*.jepg"),("jpg files","*.jpeg")]

def input():
    global input_path
    input_path = StringVar()
    input_path = tk.filedialog.askopenfilename( initialdir = os.getcwd() ,
                 title = "select a file")
    input_entry.delete(1, tk.END)  
    input_entry.insert(0, input_path)  


def output():
    path = tk.filedialog.askopenfilename()
    input_entry.delete(1, tk.END)  
    input_entry.insert(0, path)  

def wordseg():
    filepath = input_path
    print(filepath)

def viewImage():
    filepath = input_path
    img = Image.open(filepath,'r')
    img.show()

def segment():
    segmentWords(input_path)
    print("Segment Successsful -- Segmented words are saved to Folders 'segmented_words' and 'segmented_words_border' and can be used for Character Segmentation.")
    time.sleep(3)
    getEachWord()

def getEachWord():    
    # folder_dir = "segmented_words_border"
    # for images in os.listdir(folder_dir):
    #     global word_path
    # # check if the image ends with jpeg
    #     if (images.endswith(".jpeg")):
    #         word_path = "./segmented_words_border/"+images
    #         print(word_path)
    characterSegmentation()

# def segmentCharacters(word_path):
    



    



top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Input File Path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)
# openCamera = tk.Button(top_frame, text="Open Camera")

output_path = tk.Label(bottom_frame, text="Output File Path:")
output_entry = tk.Entry(bottom_frame, text="", width=40)
browse2 = tk.Button(bottom_frame, text="Browse", command=output)

begin_button = tk.Button(bottom_frame, text='View Image',command=viewImage)

Segment = tk.Button(bottom_frame, text='Start',command=segment)

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)
# openCamera.pack(pady=5)                                                                                               

output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)

begin_button.pack(pady=20, fill=tk.X)
Segment.pack(pady=20)


master.mainloop()