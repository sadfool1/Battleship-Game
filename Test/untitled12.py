import os
from PIL import Image, ImageTk
import tkinter

# Sizes in pixels
BUTTON_HEIGHT = 40
BUTTON_WIDTH = 40

root = tkinter.Tk()

script_dir = os.path.dirname(__file__)
rel_path = "explode.png"

image = Image.open(os.path.join(script_dir, rel_path))
image = image.resize((BUTTON_WIDTH,BUTTON_HEIGHT))
imtk = ImageTk.PhotoImage(image)

# Using a void image for other buttons so that the size is given in pixels too
void_imtk = tkinter.PhotoImage(width=BUTTON_WIDTH, height=BUTTON_HEIGHT)


def create_button(row, column, im):
    new_button = tkinter.Button(root,
                                height = BUTTON_HEIGHT,
                                width = BUTTON_WIDTH,
                                image=im)
    new_button.grid(row = row, column = column)


create_button(0,0, imtk)
create_button(1,1, imtk)


root.mainloop()
