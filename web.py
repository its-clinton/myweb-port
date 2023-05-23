from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = 'https://medium.com/@clintonmongare6/the-internet-of-things-iot-is-transforming-the-world-f1761c32aaf2'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#get all the headings
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
for heading in headings:
    
        # print only heading 1
        if heading.name == 'h1':
            title2 = heading.text.strip()
            print(title2)
            break
            

# get all paragraphs related to the blog post heading 1
content_elements = soup.find_all('p', class_='pw-post-body-paragraph')
for content_element in content_elements:
    content = content_element.text.strip()
    print(content)
    break

html = ['<div class="qp l g"><p class="be b dw z bj">Published on May 20, 2023 </p></div>', '<div class="oi l g"><p class="be b do z bj">Published on May 20, 2023 </p></div>']


soup1 = BeautifulSoup(html[0], 'html.parser')
soup2 = BeautifulSoup(html[1], 'html.parser')

paragraph_element1 = soup1.find('p', class_='be b dw z bj')
if paragraph_element1:
        published_date_str1 = paragraph_element1.text.strip().replace('Published on', '').strip()
        published_date1 = datetime.strptime(published_date_str1, "%B %d, %Y")
        current_date = datetime.now()
        elapsed_time1 = current_date - published_date1
        

        if elapsed_time1.days >= 365:
            elapsed_unit = "year"
            elapsed_value = elapsed_time1.days // 365
        elif elapsed_time1.days >= 30:
            elapsed_unit = "month"
            elapsed_value = elapsed_time1.days // 30
        elif elapsed_time1.days >= 7:
            elapsed_unit = "week"
            elapsed_value = elapsed_time1.days // 7
        elif elapsed_time1.days > 0:
            elapsed_unit = "day"
            elapsed_value = elapsed_time1.days
        else:
            elapsed_unit = "hour"
            elapsed_value = elapsed_time1.seconds // 3600

        if elapsed_value > 1:
            elapsed_unit += "s"

        time_since_posted = f"{elapsed_value} {elapsed_unit} ago"
else:
        time_since_posted = 'Time since posted not found.'
      
    # elapsed time 2 
paragraph_element2 = soup2.find('p', class_='be b do z bj')
if paragraph_element2:
        published_date_str2 = paragraph_element1.text.strip().replace('Published on', '').strip()
        published_date2 = datetime.strptime(published_date_str2, "%B %d, %Y")
        current_date = datetime.now()
        elapsed_time2 = current_date - published_date2 

        if elapsed_time2.days >= 365:
            elapsed_unit = "year"
            elapsed_value = elapsed_time2.days // 365
        elif elapsed_time2.days >= 30:
            elapsed_unit = "month"
            elapsed_value = elapsed_time2.days // 30
        elif elapsed_time2.days >= 7:
            elapsed_unit = "week"
            elapsed_value = elapsed_time2.days // 7
        elif elapsed_time2.days > 0:
            elapsed_unit = "day"
            elapsed_value = elapsed_time2.days
        else:
            elapsed_unit = "hour"
            elapsed_value = elapsed_time2.seconds // 3600

        if elapsed_value > 1:
            elapsed_unit += "s"

        time_since_posted2 = f"{elapsed_value} {elapsed_unit} ago"
        
else:
        time_since_posted2 = 'Time since posted not found.'

print(time_since_posted)
print("time2", time_since_posted2)