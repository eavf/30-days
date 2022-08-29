import os
import requests
import shutil
from download_util import download_file, download_file_slower

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")

os.makedirs(DOWNLOADS_DIR, exist_ok=True)

url = "https://previews.123rf.com/images/jackf/jackf1812/jackf181203949/113461748-woman-lying-on-back-on-sand-beach-in-front-of-sea.jpg"
url = "https://previews.123rf.com/images/imagesource/imagesource1902/imagesource190203010/117921277-pregnant-woman-s-torso-under-water.jpg"
url = "https://www.freexcafe.com/erotica/femjoy2/1qfiw0z3ffhx/img/ddda932f0abcc3f926bd7dfc85176b71-thumb160x220.jpg"
url = "https://as2.ftcdn.net/v2/jpg/00/47/82/21/1000_F_47822129_MnJ6g5iilbOU8VTuJoHCNSUifphY2eIE.jpg"

downloaded_img_path = os.path.join(DOWNLOADS_DIR, '1.jpg')

# for small item
r = requests.get(url, stream=True)
r.raise_for_status()    # 200
with open(downloaded_img_path, 'wb') as f:
    f.write(r.content)


#file_name = os.path.basename(url)
#new_file_name = os.path.join(DOWNLOADS_DIR, file_name)

#with requests.get(url, stream=True) as r:
#    with open(new_file_name, 'wb') as file_obj:
#        shutil.copyfileobj(r.raw, file_obj)


download_file(url, DOWNLOADS_DIR)