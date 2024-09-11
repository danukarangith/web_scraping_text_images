import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter
import os

# URL of the page to scrape
url = 'https://www.geeksforgeeks.org/fundamentals-of-algorithms/'

 
image_url = 'https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191016135223/What-is-Algorithm_-1024x631.jpg'

 
image_dir = 'images'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Send a GET request to the server
response = requests.get(url)

 
data = []

 
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
     
    tags = soup.find_all('p')
    for tag in tags:
        text = tag.text.strip()
        data.append(text)
    
     
    df = pd.DataFrame(data, columns=['Text'])
    df.to_excel('scraped_data.xlsx', index=False, engine='openpyxl')

    workbook = xlsxwriter.Workbook('scrapped_data.xlsx')
    worksheet = workbook.add_worksheet()
    
    row = 0
    h2_tags = soup.find_all('h2')
    for h2 in h2_tags:
        worksheet.write(row, 0, h2.text.strip())
        ul = h2.find_next('ul')
        if ul:
            li_tags = ul.find_all('li')
            for i in range(len(li_tags)):
                worksheet.write(row + i, 1, li_tags[i].text.strip())
            if len(li_tags) > 0:
                row = row + len(li_tags)
            else:
                row = row + 1
        else:
            row = row + 1
        row = row + 1
    workbook.close()
    
   
    try:
        img_response = requests.get(image_url)
        if img_response.status_code == 200:
            img_file = os.path.join(image_dir, 'downloaded_image.jpg')
            with open(img_file, 'wb') as f:
                f.write(img_response.content)
            print(f"Image has been saved to '{img_file}'")
        else:
            print("Failed to retrieve the image.")
    except Exception as e:
        print(f"Error downloading image {image_url}: {e}")

    print("Text data has been saved to 'scraped_data.xlsx'")
else:
    print("Error fetching the page")
