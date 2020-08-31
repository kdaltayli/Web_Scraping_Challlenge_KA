
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
import time


def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


def scrape_info():
    browser=init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # time.sleep(2)
    iterable_list=soup.find('li',class_='slide')
    print(iterable_list)
    time.sleep(2)
    # collect the latest News Title and Paragraph Text.
    # Assign the text to variables that you can reference later
    news = iterable_list.find('div', class_='content_title').get_text()
    print(news)
    time.sleep(3)

    paragraph=iterable_list.find('div', class_="article_teaser_body").get_text()
    print(paragraph)
    # close the browser
    # browser.quit()

    # return [news,paragraph]

    # # JPL Mars Space Images - Featured Image
# def space_image():
#     browser=init_browser()

    # Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
    featured_image_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(featured_image_url)

    click_but=browser.find_by_id('full_image')
    click_but.click()

    links_found = browser.links.find_by_partial_text('more info')
    links_found.click()

    html=browser.html
    soup=BeautifulSoup(html,'html.parser')

    image=soup.find('img', class_="main_image").get('src')

    mars_featured_image_url= f'https://www.jpl.nasa.gov/{image}'

    # close the browser
    # browser.quit()
    # return image_url

    # # MARS FACTS
# def mars_fact():

    # Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and 
    facts_url='https://space-facts.com/mars/'

    tables=pd.read_html(facts_url)
    df2=tables[0]
    # print(df1)
    # print(df2)
    df2.columns=['Diameter','Units']

    # use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    df2

    # Use Pandas to convert the data to a HTML table string.
    html_table = df2.to_html()
    html_table


    df2.to_html('table.html')

    result_table=df2.to_dict('records')
    # get_ipython().system('open table.html')

    # return result_table


# def space_image():
#     browser=init_browser()

    hemisphere_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # Retrieve page with the requests module
    browser.visit(hemisphere_url)

    hemisphere_image_url=[]

    for row in range(4):
        browser.find_by_tag('h3')[row].click()
        
        html=browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        images=soup.find('img',class_='wide-image')['src']
        image_url=f'https://astrogeology.usgs.gov/{images}'
        
    # Append the dictionary with the image url string and the hemisphere title to a list. 
    # This list will contain one dictionary for each hemisphere  
        title=soup.find('h2').text
        browser.back()
        hemisphere_image_url.append({"title": title, "img_url":image_url})
        
        mars_data={"news":news,
                    "paragraph":paragraph,
                    "image_url":mars_featured_image_url,
                    "result_table":html_table,
                    "hemisphere_image":hemisphere_image_url
        }
    # browser.quit()

    return mars_data
# scrape()