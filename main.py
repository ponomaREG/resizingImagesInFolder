from PIL import Image
import os

#images

path_to_images = 'images'
path_to_images_resized = 'images_resized'
try:
    os.mkdir(path_to_images_resized)
except:
    print("DIR ALREADY EXISTS")

files = os.listdir(path_to_images)
for file in files:
    image = Image.open(os.path.join(os.getcwd(),path_to_images,file))
    new_image = image.resize((1080,1920))
    new_image.save(os.path.join(os.getcwd(),path_to_images_resized,"resized___"+file))
    new_image.close()
    image.close()
