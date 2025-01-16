from PIL import Image
import os

path = input('Please type in the name of the image\nfolder you want to work with: ')
path = './' + path

angle = int(input('Is the "top" of the image facing left or right?\nEnter (1) for left\nEnter (2) for right\n'))

while angle != 1 and angle != 2:
    angle = int(input('Please, either (1) for left or (2) for right:'))

pathOut = input('Enter the name of the output folder\n(If one does not exist, one will be created for you): ')
pathOut = './' + pathOut

print('Thank you. One moment please.')

if angle == 1: #Rotates the images clockwise by 90 degrees
    for filename in os.listdir(path):
        image = Image.open(f"{path}/{filename}")

        rotation = image.transpose(Image.Transpose.ROTATE_270)
        bareName = os.path.splitext(filename)[0]
        print(bareName, 'rotated!')

        try:
            rotation.save(f'.{pathOut}/{bareName}_rotated.JPG')
        except Exception:
            os.mkdir(f'.{pathOut}')
            rotation.save(f'.{pathOut}/{bareName}_rotated.JPG')
#    rangle = 'ROTATE_90'
for filename in os.listdir(path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        image = Image.open(f'{path}/{filename}')
        bareName = os.path.splitext(filename)[0]

        if angle == 1:
            rotation = image.rotate(270)
        else:
            rotation = image.rotate(90)
        
        try:
            rotation.save(f'.{pathOut}/{bareName}_rotated.JPG')
        except Exception:
            os.mkdir(f'.{pathOut}')
            rotation.save(f'.{pathOut}/{bareName}_rotated.JPG')

        print(bareName, 'done!')

else: #Rotates the images counter-clockwise by 90 degrees
    for filename in os.listdir(path):
        image = Image.open(f"{path}/{filename}")

        rotation = image.transpose(Image.Transpose.ROTATE_90)
        bareName = os.path.splitext(filename)[0]
        print(bareName, 'rotated!')

        try:
            rotation.save(f'.{pathOut}/{bareName}_rotated.JPG')
        except Exception:
            os.mkdir(f'.{pathOut}')
            rotation.save(f'.{pathOut}/{bareName}_rotated.JPG')
#    rangle = 'ROTATE_270'

print('And we are done, please check the destination folder')