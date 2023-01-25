import tkinter as tk
from pathlib import Path
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog
import os
from PIL import Image
import math
from input_field import Lotfi

root = TkinterDnD.Tk() # TkinterDnD utilise du drag and drop
root.title(string = "spritesheet generator")


# Nombre de colone par défaut
NUMBER_OF_COLUMNS = 10


def error(txt):
    debug.config(text=txt, bg='#F40', fg='#FFF')

def create_the_spritesheet(path):
    file_path = Path(path)
    print(file_path)
    # Si le fichier spécifié n'est pas un dossier
    if(not file_path.is_dir()):
        error("Element sent was not a directory")
        return
    
    # Liste toutes les images du répertoire
    list_img = list(p.resolve() for p in Path(path).glob("*") if p.suffix in {".png", ".jpeg", ".jpg", ".gif", ".tiff"})

    print(list_img)



    SIZE_IMAGE = ()
    sprite_image = None

    # On recupère le nombre de colonnes souhaité depuis l'interface
    NUMBER_OF_COLUMNS = int(column_entry.get())


    # Si la liste est vide alors il n'y a pas d'image
    if(len(list_img) == 0):
        error("Directory does not contain image")
        return

    for index, image in enumerate(list_img):
        number_of_rows = math.ceil(len(list_img) / NUMBER_OF_COLUMNS)
        img = Image.open(image)
        if(SIZE_IMAGE != img.size):
            # Initialisation de l'image de la sprite
            sprite_image = Image.new('RGBA', (img.width * NUMBER_OF_COLUMNS, img.height* number_of_rows))

            # si l'index n'est pas égal à zéro et que l'image est différentes alors
            if(index != 0):
                error(f"{image.name} is not the same size as previous image")
                return
        SIZE_IMAGE  = img.size

        posX = (index % NUMBER_OF_COLUMNS)  * img.width
        posY = math.floor( index / NUMBER_OF_COLUMNS ) * img.height

        sprite_image.paste(img, (posX, posY))


    if(int(column_entry.get()) > len(list_img)):
        error("There are more columns than images")
        return


    sprite_image.show()

# Callback du listener du bouton
def upload_dir_button():
    dirname = filedialog.askdirectory()
    lb.insert(tk.END, Path(dirname).name)
    create_the_spritesheet(dirname)

# Callback du listener de la zone de drag & drop
def upload_dir_drag(e):
    print(type(e.data))

    # tkinterdnd2 produit parfois des URLs entourée d'accolade 
    dirname = e.data.replace('}', '').replace('{', '')

    lb.insert(tk.END, Path(dirname).name)
    print(dirname)

    create_the_spritesheet(dirname)

# Interface

debug = tk.Label(master=root, text="Info")
debug.pack(padx=10, pady=10)

lb = tk.Listbox(root)
lb.insert(1, "Drag directory here")


# register the listbox as a drop target
lb.drop_target_register(DND_FILES)
lb.dnd_bind('<<Drop>>', lambda e: upload_dir_drag(e))

lb.pack()


button = tk.Button(root, text='Open Directory', command=upload_dir_button)
button.pack()


container = tk.Frame(root)

column_info = tk.Label(master=container, text="Number of column")
column_info.pack(padx=10, pady=10, side="left")



column_entry=Lotfi(container, width=2)
column_entry.insert(0, str(NUMBER_OF_COLUMNS))
column_entry.pack(padx=10, pady=10, side="right")

container.pack()


root.mainloop()