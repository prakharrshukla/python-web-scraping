import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import os

# 👇 apna page URL yaha daal
url = "https://keithgalli.github.io/web-scraping/webpage.html"

# folder to save images
save_folder = "downloaded_images"
os.makedirs(save_folder, exist_ok=True)

# request page
r = requests.get(url)
soup = bs(r.content, "html.parser")

# find all img tags
images = soup.find_all("img")
print(f"Found {len(images)} images.")

if len(images) == 0:
    print("⚠️ No images found on this page. Check if images are loaded by JavaScript.")
else:
    for i, img in enumerate(images):
        img_src = img.get("src")
        if not img_src:
            continue

        # join base url with relative link
        full_img_url = urljoin(url, img_src)
        print(f"[{i}] Downloading:", full_img_url)

        # fetch image
        img_data = requests.get(full_img_url).content

        # save image with index name
        filename = os.path.join(save_folder, f"image_{i}.jpg")
        with open(filename, "wb") as f:
            f.write(img_data)

    print("✅ All images downloaded!")

