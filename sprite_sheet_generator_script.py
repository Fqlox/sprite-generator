'''
Script générant la spritesheet

utilisable tel quel

possible déclinaison en CLI

'''


from PIL import Image
from pathlib import Path
import math

URL = ""

NUMBER_OF_COLUMNS = 6

images_path = Path(URL)

list_img = list(images_path.glob('*png'))

SIZE_IMAGE = ()

sprite_image = None

for index, image in enumerate(list_img):
    number_of_rows = math.ceil(len(list_img) / NUMBER_OF_COLUMNS)
    img = Image.open(image)
    if(SIZE_IMAGE != img.size):
        # Initialisation de l'image de la sprite
        sprite_image = Image.new('RGBA', (img.width * NUMBER_OF_COLUMNS, img.height* number_of_rows))

        # si l'index n'est pas égal à zéro et que l'image est différentes alors
        if(index != 0):
            print(f"{image.name} is not the same size as previous image")
            break # fin de la boucle
    SIZE_IMAGE  = img.size

    posX = (index % NUMBER_OF_COLUMNS)  * img.width
    posY = math.floor( index / NUMBER_OF_COLUMNS ) * img.height

    print(posX, posY)

    sprite_image.paste(img, (posX, posY))


sprite_image.show()



