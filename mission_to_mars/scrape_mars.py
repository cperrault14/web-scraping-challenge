#!/usr/bin/env python
# coding: utf-8

# ## Import Dependencies

# In[1]:
# Import Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager

# Browser
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()

# Visit urls
    url_news = "https://mars.nasa.gov/news/8942/nasas-ingenuity-mars-helicopter-completes-first-one-way-trip/"
    browser.visit(url_news)


# In[5]:


# Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

#Scrape title and paragraph
    news_title = soup.find('h1').text
    news_p = soup.find('i').text

## JPL Mars Space Images - Featured Image

# Visit urls
    url_image = "https://www.jpl.nasa.gov/images/ingenuitys-successful-fifth-flight"
    browser.visit(url_image)


# Scrape page into Soup
    image_html = browser.html
    image_soup = bs(image_html, "html.parser")

#Create featured_image variable to then use with featured_image_url variable
    featured_image = image_soup.find_all('img')[2]["src"]


#Save full size image and print url 
    featured_image_url = f"https://www.jpl.nasa.gov{featured_image}"

# ## Mars Facts

# Visit urls
    url_facts = "https://space-facts.com/mars/"
    browser.visit(url_facts)

# Use pandas to grab data from url link
    mars_facts = pd.read_html(url_facts)
    mars_facts

#Transform mars_facts into dataframe
    facts_df = mars_facts[0]

# Add column header to make it look pretty
    facts_df.columns = ["Fact", "Fact Value"]

# Set Fact as indes
    facts_df.set_index("Fact", inplace=True)

# Print results
    facts_df

# Save html code
    html_table = facts_df.to_html()
# print(html_table)

# Clean up table to make it look pretty
    html_table.replace("\n", '')

# ## Mars Hemispheres

# Set up Splinter, visit url
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    executable_path = {'executable_path': ChromeDriverManager().install()}
    time.sleep(1)
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(hemisphere_url)

# Scrape page into Soup
    hemisphere_html = browser.html
    soup = bs(hemisphere_html, 'html.parser')

# Identify name of images and loop through it to grab teh name of the titles
    names = soup.find_all("h3")
    for name in names:
    #Clicks in a link by looking for partial content of href attribute
        browser.click_link_by_partial_text("Hemisphere")
#Test result        
    print(names)

#Loop through data for each Mars Hemisphere and grab the necessary elements/objects
    hemispheres = soup.find_all("div", class_="description")
    hemisphere_dict={}
    hemisphere_image_urls=[]
    for i in hemispheres:
        link = i.find('a')
        href = link['href']
        title = link.find('h3').text
        main_url = "https://astrogeology.usgs.gov" + href
        browser.visit(main_url)
        html = browser.html
        soup = bs(html, 'html.parser')
        pic = soup.find("a", target="_blank")
        pic_href = pic['href']
        hemisphere_image_urls.append({"title":title,"img_url":pic_href})


    mars_info_dict = {"news_title":news_title,"news_p":news_p,"featured_image_url":featured_image_url,
    "mars_facts":html_table,"hemisphere_img":hemisphere_image_urls}

    print(mars_info_dict)

    # browser.quit()

    # return mars_info_dict
