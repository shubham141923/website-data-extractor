import requests
from bs4 import BeautifulSoup
import urllib.request
import os

def extract_website_data(url):
    # Fetch the HTML content of the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract images data
    images = []
    for img in soup.find_all('img'):
        images.append({
            'rc': img.get('src'),
            'alt': img.get('alt')
        })
     # Save images to files
    for i, image_url in enumerate(images):
        imageName = image_url['alt']
        folder_name = 'images'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        filename = os.path.join(folder_name, f'{imageName}.jpg')
        response = requests.get(image_url['src'], stream=True)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)


    # Extract font families
    font_families = set()
    for element in soup.find_all():
        font_family = element.get('style')
        if font_family:
            for font in font_family.split(';'):
                if 'font-family' in font:
                    font_families.add(font.split(':')[1].strip())

    # Extract color tags
    color_tags = set()
    for element in soup.find_all():
        color = element.get('style')
        if color:
            for c in color.split(';'):
                if 'color' in c:
                    color_tags.add(c.split(':')[1].strip())

    # Extract heading tags info
    heading_tags = {}
    for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        heading_tags[heading.name] = heading.text

    return {
        'images': images,
        'font_families': list(font_families),
        'color_tags': list(color_tags),
        'heading_tags': heading_tags
    }

# Example usage
url = 'www.example.com'
website_data = extract_website_data(url)

# Print the extracted data
print('Images:', website_data['images'])
print('Font families:', website_data['font_families'])
print('Color tags:', website_data['color_tags'])
print('Heading tags:', website_data['heading_tags'])
