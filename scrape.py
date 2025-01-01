import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

output_dir = 'Scraped_Content'
os.makedirs(output_dir, exist_ok=True)

service = Service()
driver = webdriver.Chrome(service=service)

base_url = 'https://en.wikipedia.org/wiki/Sri_Lanka'
driver.get(base_url)
time.sleep(3)

page_content = driver.find_element(By.TAG_NAME, 'body').text
output_file_path = os.path.join(output_dir, "Sri_Lanka.txt")

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(page_content)

driver.quit()
