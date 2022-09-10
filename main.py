import time
from tqdm import tqdm
import requests
import webbrowser
from coordinates_calc import coordinates


class main:

    try:

        new = 2
        timeout = 10

        url = "https://www.google.com/maps/place/" + coordinates.coordinate
        request = requests.get(url, timeout=timeout)

        print("Internet Connection Established")

        print("Opening Web Browser...")
        time.sleep(0.5)

        print("Searching For Coordinates....")

        for i in tqdm(range(100), desc="Processing...", ascii=False, ncols=75):
            time.sleep(0.5)

        webbrowser.open(url, new=new)

    except (requests.ConnectionError, requests.Timeout) as exception:

        print("\nUnable To Connect To The Internet")
        print("Cannot Search For Coordinates")

    except KeyboardInterrupt:
        print("*****Program Closed******")

    except AttributeError:
        pass
