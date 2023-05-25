from flask import Flask, render_template,request,url_for
import requests
import re
from bs4 import BeautifulSoup
import requests
import datetime
from datetime import datetime

# app name
app = Flask(__name__)


def calculate_time_since_posted(html):
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

    return time_since_posted
    return time_since_posted2

# home page
@app.route('/')
def index():

    urls = ['https://medium.com/@clintonmongare6/programming-as-a-lifestyle-e04c96ead1a0', 'https://medium.com/@clintonmongare6/the-internet-of-things-iot-is-transforming-the-world-f1761c32aaf2']

    response = requests.get(urls[0])
    soup = BeautifulSoup(response.text, 'html.parser')

    # blog post title
    title = soup.find('h1').text.strip()

    content_element = soup.find('p', class_='pw-post-body-paragraph')
    if content_element:
        content = content_element.text.strip()
    else:
        content = 'Content not found.'

    response = requests.get(urls[1])
    soup = BeautifulSoup(response.text, 'html.parser')

        # blog post title
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    title2 = None
    for heading in headings:
        if heading.name == 'h1':
            title2 = heading.text.strip()
            break

    content_elements = soup.find_all('p', class_='pw-post-body-paragraph')
    if content_elements:
        content2 = content_elements[0].text.strip()
    else:
        content = 'Content not found.'

    html = ['<div class="qp l g"><p class="be b dw z bj">Published on May 20, 2023 </p></div>', '<div class="oi l g"><p class="be b do z bj">Published on May 20, 2023 </p></div>']
    time_since_posted = calculate_time_since_posted(html[0])
    time_since_posted2 = calculate_time_since_posted(html[1])
    

    return render_template('index.html',title=title, title2=title2, content=content, content2=content2, time_since_posted=time_since_posted,  time_since_posted2=time_since_posted2)

# project details
@app.route('/project_details')
def portfolio_details():
    return render_template('project_details.html')

# education details
@app.route('/education_details')
def education_details():
    return render_template('education.html')


# certifications
@app.route('/certifications')
def certifications():
     return render_template('certifications.html')

# main function
if __name__ == '__main__':
    app.run()
    
