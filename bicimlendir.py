from PIL import Image
import sys

#php dosyasındaki değişkenlere erişim
filename = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])
angle = int(sys.argv[4])
flip = sys.argv[5]
crop_top = int(sys.argv[6])
crop_bottom = int(sys.argv[7])
crop_left = int(sys.argv[8])
crop_right = int(sys.argv[9])
edited_image_path = sys.argv[10]

img = Image.open(filename)
global result

def resize_image(image_path, width, height):
    global result
    with Image.open(image_path) as img:
        result = img.resize((width, height))
        return result
        #result.save(image_path)

def crop_image(image_path, crop_coords):
    global result
    with Image.open(image_path) as img:
        result = img.crop(crop_coords)
        return result
        #result.save(image_path)

def rotate_flip_image(image_path, angle):
    global result
    with Image.open(image_path) as img:
        if(angle<0):
            result = img.rotate(-angle)
        if(angle>0):
            result = img.rotate(angle)
        return result

def flip_image(image_path, flip):
    global result
    with Image.open(image_path) as img:
        if flip == "horizontal":
            result = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif flip == "vertical":
            result = img.transpose(Image.FLIP_TOP_BOTTOM)
        #result.save(image_path)
        return result

# Adım adım işlemler
resize_image(filename, width, height)
crop_coords = (crop_left, crop_top, img.width + crop_right, img.height + crop_bottom)
crop_image(filename, crop_coords)
rotate_flip_image(filename, angle)
flip_image(filename, flip)

edited_image_path = 'uploads/edited.jpg'
result.save(edited_image_path)
