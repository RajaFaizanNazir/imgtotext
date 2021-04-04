import shutil

from PIL import Image
import pytesseract as pt
import os
import pandas as pd

folder = "Will Smith"

# path for the folder for getting the raw images
path = r"C:/Users/RFaiz/Desktop/erwincuijperscc/Imagetotext/Pictures/" + folder
path, dirs, files = next(os.walk(path))
file_count = len(files)

# link to the file in which output needs to be kept
fullTempPath = r"C:/Users/RFaiz/Desktop/erwincuijperscc/Imagetotext/Pictures/" + folder + " Done/OUTPUT/outputFile.txt"
fullNameTempPath = r"C:/Users/RFaiz/Desktop/erwincuijperscc/Imagetotext/Pictures/" + folder + " Done/OUTPUT/outputName.txt"

i = 0
# iterating the images inside the folder
for imageName in os.listdir(path):
    inputPath = os.path.join(path, imageName)
    img = Image.open(inputPath)
    pt.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    # applying ocr using pytesseract for python
    text = pt.image_to_string(img, lang="eng")

    # saving the  text for appending it to the output.txt file
    # a + parameter used for creating the file if not present
    # and if present then append the text content
    file1 = open(fullTempPath, "a+", encoding="utf-8")
    file2 = open(fullNameTempPath, "a+", encoding="utf-8")
    # providing the name of the image
    file2.write(imageName + "\n")

    # providing the content in the image
    file1.write(text + "\n")
    file1.write("_______________________________________________________\n")
    # print(text)
    # print("_______________________________________________________")

    file1.close()
    file2.close()
    shutil.move('C:/Users/RFaiz/Desktop/erwincuijperscc/Imagetotext/Pictures/' + folder + '/' + imageName,
                'C:/Users/RFaiz/Desktop/erwincuijperscc/Imagetotext/Pictures/' + folder + ' Done/DONEIMG/' + imageName)
    print("Loading :" + str((i / file_count) * 100) + " %")
    i = i + 1
    # for printing the output file
# file2 = open(fullTempPath, 'r')
# print(file2.read())
# file2.close()
