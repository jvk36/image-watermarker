# BEFORE RUNNING THE FILES EXECUTE THE FOLLOWING IN THE TERMINAL FROM THE WORKING FOLDER:
pip install -r requirements.txt

## APPLICATION - INTRO

This is a desktop application built using tkinter GUI library and the pillow library for image processing:

https://docs.python.org/3/library/tkinter.html
https://pypi.org/project/Pillow/

The application is self-contained in the main.py file. The rest of the python files introduces/tests the libraries used.

## main.py APPLICATION - FUNCTION DESCRIPTION:

The application combines the functionality introduced in the following two examples into a complete functional Image Watermarker program: 

water_marking_example, and water_marking_subliminal_example 

Functional details of each of these programs are described in more detail below.

## playground.py and tkinter_intro.py - tkinter library basic intro:

NOTE: The code in both these files are exactly the same.

The self-contained program shows a basic UI with a Label, an Edit Box and a Button. Typing something into the Edit Box and Clicking the Button will result in the Label getting updated with what was typed in. 

## file_dialog_example - tkinter library's filedialog intro:

The self-contained program shows how to use the filedialog functionality in the tkinter library. The program shows a basic UI with an 'Open File' button and a Label that initially reads 'No File Selected'. Clicking the button opens tkinter's File Open Dialog that allows one to select a file from the file system. The selected file is theb displayed on the label in the main UI. 

## water_marking_example - Functional description:

The self-contained program has a basic UI with the following features:

    1. Open Image Button: Allows selecting an Image. The File name is displayed once one is selcted.
    2. Edit Box: Allows typing in a watermark text. 
    3. Add Text Watermark Button: The watermark text typed into the Edit Box is added to the image in the bottom right. The preview shows the altered image
    4. Add Logo Watermark Button: It allows opening a watermark logo which is then incoporated into the image. The preview shows the altered image
    5. Save Image: Allows saving the watermarked image into the file system.

open_image: The function uses tkinter's filedialog functionality to select an image file from the file system. A global variable original_image keeps track of the file selected. 

add_text_watermark: The function implements the text watermarking functionality using the pillow library.

add_logo_watermark: The function implements the logo watermarking functionality using the pillow library.

preview_image:The function implements displaying the processed image on the Label preview_label in the UI.

save_image: The function implements the image saving functionality using pillow and tkinter's filedialog. 

## water_marking_subliminal_example - Functional description:

The program enhances the water_marking_example by adding a new function create_subliminal_watermark to incorporate a more advanced watermarking. 

