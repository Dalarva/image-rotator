from PIL import Image
import os

path = input('Please input the name of the image folder: ')
path = './' + path
angle = 0
angle = int(input('Is the "top" of the image facing left or right?\nEnter (1) for left\nEnter (2) for right\n'))

if angle > 2:
    while True:
        angle = int(input('Please, either (1) for left or (2) for right:'))
        if angle == 1 or 2:
            break
        else:
            continue

elif angle < 1:
    while True:
        angle = int(input('Please, either (1) for left or (2) for right:'))
        if angle == 1 or 2:
            break
        else:
            continue

print('Thank you. One moment please.')

if angle == 1:
    rangle = 30

else:
    rangle = 180

rangle = float(rangle)

pathOut = '/rotatedImages2'

for filename in os.listdir(path):
    image = Image.open(f"{path}/{filename}")

    rotation = image.rotate(rangle)
    bareName = os.path.splitext(filename)[0]
    print(bareName, 'rotated!')

    try:
        rotation.save(f'.{pathOut}/{bareName}_rotated.JPG')
    except Exception:
        os.mkdir(f'.{pathOut}')
        rotation.save(f'.{pathOut}/{bareName}_rotated.JPG')

print('And we are done, please check the destination folder')