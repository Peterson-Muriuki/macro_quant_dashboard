import openeo

def get_satellite_metadata(aoi_coords):
    """
    Connects to Copernicus Data Space. 
    Requires a free account at dataspace.copernicus.eu
    """
    try:
        conn = openeo.connect("https://openeo.dataspace.copernicus.eu")
        # Example: Search for Sentinel-2 cloud-free images over AOI
        return "Connection Successful: Ready to process Sentinel-2"
    except:
        return "Satellite API Offline: Check Credentials"