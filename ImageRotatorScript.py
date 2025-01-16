from PIL import Image, ImageOps
import os

path = input('Please type in the name\nof the image folder you want to work with: ')
path = './' + path

angle = int(input('Is the "top" of the image facing left or right?\nEnter (1) for left\nEnter (2) for right\n'))

while angle != 1 and angle != 2:
    angle = int(input('Please, either (1) for left or (2) for right:'))

pathOut = input('Enter the name of the output folder\n(If one does not exist, one will be created for you): ')
pathOut = './' + pathOut

print('Thank you. One moment please.')

for filename in os.listdir(path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        image = Image.open(f'{path}/{filename}')
        image = ImageOps.exif_transpose(image)
        bareName = os.path.splitext(filename)[0]

        if angle == 1:
            rotation = image.rotate(270, expand=True)
        else:
            rotation = image.rotate(90, expand=True)
        
        try:
            rotation.save(f'.{pathOut}/{bareName}_rotated.JPG')
        except Exception:
            os.mkdir(f'.{pathOut}')
            rotation.save(f'.{pathOut}/{bareName}_rotated.JPG')

        print(bareName, 'done!')

print('And we are done, please check the destination folder')