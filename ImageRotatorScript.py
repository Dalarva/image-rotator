from PIL import Image, ImageOps
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

fldrnmbr = int(input('How many folders are we working with today?: '))

for i in range(fldrnmbr):
    fldrfound = 0
    while fldrfound == 0:
        path = input('Please type in the name\nof the image folder you want to work with: ')
        path = './' + path
        try:
            os.listdir(path)
            break
        except Exception:
            print('Oops! Looks like that folder does not exist.')

    angle = int(input(('Is the "top" of the image facing left, right, or is the image upside-down?\n'
                       'Enter (1) for left\nEnter (2) for right\nEnter (3) for upside-down\n')))

    while angle != 1 and angle != 2 and angle != 3:
        angle = int(input('Please, either (1)-left or (2)-right or (3)-upside-down:'))

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
            elif angle == 2:
                rotation = image.rotate(90, expand=True)
            else:
                rotation = image.rotate(180, expand=True)
            
            try:
                rotation.save(f'{pathOut}/{bareName}_rotated.JPG')
            except Exception:
                os.makedirs(pathOut, exist_ok=True)
                rotation.save(f'{pathOut}/{bareName}_rotated.JPG')

            print(bareName, 'done!')

    print('And we are done, please check the destination folder')