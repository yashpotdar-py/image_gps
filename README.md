# Image Geolocation
This code is designed to extract GPS coordinates from an image and then open the location on Google Maps in a web browser.

# Dependencies
The code requires the following libraries to be installed:

* ***'requests'***
* ***'tqdm'***
* ***'Pillow'***

# Usage

To use this code, you need to provide the path of the image file that you want to extract GPS coordinates from. You can do this by running the **'exif_data.py'** module and following the prompts:

```python exif_data.py```

If the image file contains GPS information, the latitude and longitude coordinates will be extracted and printed to the console. Otherwise, an error message will be displayed.

Next, you can use the extracted coordinates to open Google Maps in a web browser by running the **'main.py'** module:


```python main.py```

This will check for an internet connection and then open Google Maps in a new tab with the location of the image displayed. If an internet connection cannot be established or the image file does not contain GPS information, an error message will be displayed.

# Conclusion

Overall, this code provides a simple way to quickly view the location of an image on Google Maps if the image contains GPS information.
