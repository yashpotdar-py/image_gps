from exif_data import exif_data


class coordinates:

    try:

        # Get Latitude, Longitude and Directions(Ref)
        lat = exif_data.gps_info['GPSLatitude']
        long = exif_data.gps_info['GPSLongitude']
        lat_ref = exif_data.gps_info['GPSLatitudeRef']
        long_ref = exif_data.gps_info['GPSLongitudeRef']

        # Latitude:

        # in degrees
        lat_deg = lat[0]
        lat_deg = lat_deg[0]

        # in minutes
        lat_min = lat[1]
        lat_min = lat_min[0] / 60

        # in seconds
        lat_sec = lat[2]
        lat_sec = lat_sec[0] / 360000

        # Final Calculation
        latitude = lat_deg + lat_min + lat_sec

        # Longitude:

        # in degrees
        long_deg = long[0]
        long_deg = long_deg[0]
        
        # in minutes
        long_min = long[1]
        long_min = long_min[0] / 60

        # in seconds
        long_sec = long[2]
        long_sec = long_sec[0] / 360000

        # Final Calculation
        longitude = long_deg + long_min + long_sec

        # Negative if LatitudeRef:S or LongitudeRef:W
        if exif_data.gps_info['GPSLatitudeRef'] == 'S':
            lat = -lat

        if exif_data.gps_info['GPSLongitudeRef'] == 'W':
            long = -long

        print("*" * 10)
        coordinate = f"{latitude} {lat_ref}, {longitude} {long_ref}"
        print(f"The Coordinates Are: {coordinate}")
        print("*" * 10)

    except (AttributeError, KeyError, FileNotFoundError):
        pass
