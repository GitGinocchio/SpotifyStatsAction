from argparse import ArgumentParser, Namespace
from jinja2 import Environment, FileSystemLoader
from auth import get_spotify
from utils import *
import re

env = Environment(loader=FileSystemLoader('templates/svgs'))

spotify = get_spotify()

def validate_args(args : Namespace):
    pass


def main(args: Namespace) -> None:
    #items = spotify.current_user_recently_played(1)['items']

    #images = items[0]['track']['album']['images']
    #print(images)

    from PIL import Image
    import base64

    # Open the image file using Pillow (PIL)
    img = Image.open('updated/images/ab67616d0000b273b9c4979446c4d39bc08e9503.png')

    # Convert the image to a BytesIO object
    with open('updated/images/ab67616d0000b273b9c4979446c4d39bc08e9503.png', 'rb') as f:
        img_bytes = f.read()

    # Encode the image bytes to Base64
    base64_img = base64.b64encode(img_bytes)

    # Print or use the Base64-encoded string as needed
    print(base64_img.decode())


if __name__ == '__main__':
    parser = ArgumentParser()



    args = parser.parse_args()

    # Args Validations
    validate_args(args)

    # Update READMEs
    main(args)