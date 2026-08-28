import urllib.request
import os
import ssl



# Fix SSL certificate issue
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

base_url = "https://opendata.dwd.de/weather/radar/composite/hg/"
output_dir = "C:/Users/marga/projects/DWD-radar/hg_files"
os.makedirs(output_dir, exist_ok=True)

files = [
    "HG2608211220_000.bz2",                               
    "HG2608211225_000.bz2",                                              
    "HG2608211230_000.bz2",                                            
    "HG2608211235_000.bz2",                              
    "HG2608211240_000.bz2",                                             
    "HG2608211245_000.bz2",                              
    "HG2608211250_000.bz2",                              
    "HG2608211255_000.bz2",                               
    "HG2608211300_000.bz2",                               
    "HG2608211305_000.bz2",          
]

for filename in files:
    url = base_url + filename
    outpath = os.path.join(output_dir, filename)
    print(f"Downloading {filename}...")
    opener = urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=ssl_context)
    )
    with opener.open(url) as response:
        with open(outpath, 'wb') as f:
            f.write(response.read())
    print(f"Done")

print("All file downloaded")


    