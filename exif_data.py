from PIL.ExifTags import GPSTAGS, TAGS
from tqdm import tqdm
import time
import PIL
from PIL import Image


class exif_data:
    try:

        print("Image Geolocation")
        print("Starting Program...")

        for i in tqdm(range(100), desc="Starting...", ascii=False, ncols=75):
            time.sleep(0.01)

        print("Pls Ensure That The Image/Device had location permissions")
        img_path = input("Enter Complete Path of Image: ")

        try:

            # Open Image
            img = Image.open(img_path)

            # Get EXIF Data
            exif_table = {}

            for key, values in img.getexif().items():
                tag = TAGS.get(key)
                exif_table[tag] = values
            gps_info = {}

            for key, values in exif_table['GPSInfo'].items():
                geo_tag = GPSTAGS.get(key)
                gps_info[geo_tag] = values

        except KeyError:

            print("\nThe Image Does Not Contain Any Exif Data")
            print("Try With An Image With Exif Data")

        except PIL.UnidentifiedImageError:

            print("\nEnter The Path Of An Image")
            print("Only Supported Formats Are .jpg, .jpeg, .png")

        except (AttributeError, FileNotFoundError):

            print("\nPlease Enter A Valid Path")
            print("For Example: /home/user/image.jpg")

    except KeyboardInterrupt:

        print("\n ****** Program Closed ******")
