{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Import Dependencies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Dependencies\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "import time\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 90.0.4430\n",
      "Get LATEST driver version for 90.0.4430\n",
      "Driver [C:\\Users\\cperr\\.wdm\\drivers\\chromedriver\\win32\\90.0.4430.24\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    " # Set up Splinter\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit urls\n",
    "url_news = \"https://mars.nasa.gov/news/8942/nasas-ingenuity-mars-helicopter-completes-first-one-way-trip/\"\n",
    "browser.visit(url_news)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape page into Soup\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Scrape title and paragraph\n",
    "news_title = soup.find('h1').text\n",
    "news_p = soup.find('i').text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "NASA's Ingenuity Mars Helicopter Completes First One-Way Trip  \n",
      "\n",
      "------------------------------------------------------------------------------------------------------------------\n",
      "The Red Planet rotorcraft headed south in support of furthering research into the potential use of aerial scouts on Mars in the future.\n"
     ]
    }
   ],
   "source": [
    "# Print results\n",
    "print(news_title)\n",
    "print(\"------------------------------------------------------------------------------------------------------------------\")\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# news_title = \"NASA's Ingenuity Mars Helicopter Completes First One-Way Trip   – NASA’s Mars Exploration Program\"\n",
    "# news_p = \"The Red Planet rotorcraft headed south in support of furthering research into the potential use of aerial scouts on Mars in the future\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# # Close the browser after scraping\n",
    "# browser.quit()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit urls\n",
    "url_image = \"https://www.jpl.nasa.gov/images/ingenuitys-successful-fifth-flight\"\n",
    "browser.visit(url_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape page into Soup\n",
    "image_html = browser.html\n",
    "image_soup = bs(image_html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create featured_image variable to then use with featured_image_url variable\n",
    "featured_image = image_soup.find_all('img')[2][\"src\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "JPL Mars Space Image\n",
      "------------------------------------------------------------------------------------------------------------------\n",
      "https://www.jpl.nasa.govhttps://d2pn8kiwq2w21t.cloudfront.net/images/jpegPIA24647.width-1024.jpg\n"
     ]
    }
   ],
   "source": [
    "#Save full size image and print url \n",
    "featured_image_url = f\"https://www.jpl.nasa.gov{featured_image}\"\n",
    "print(\"JPL Mars Space Image\")\n",
    "print(\"------------------------------------------------------------------------------------------------------------------\")\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# # Close the browser after scraping\n",
    "# browser.quit()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit urls\n",
    "url_facts = \"https://space-facts.com/mars/\"\n",
    "browser.visit(url_facts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# # Scrape page into Soup(not necessary)\n",
    "# facts_html = browser.html\n",
    "# facts_soup = bs(facts_html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                      0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers,\n",
       "   Mars - Earth Comparison             Mars            Earth\n",
       " 0               Diameter:         6,779 km        12,742 km\n",
       " 1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 2                  Moons:                2                1\n",
       " 3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 4         Length of Year:   687 Earth days      365.24 days\n",
       " 5            Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use pandas to grab data from url link\n",
    "mars_facts = pd.read_html(url_facts)\n",
    "mars_facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Fact Value</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fact</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Equatorial Diameter:</th>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Period:</th>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Surface Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>First Record:</th>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Recorded By:</th>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                         Fact Value\n",
       "Fact                                               \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.39 × 10^23 kg (0.11 Earths)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.38 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                   -87 to -5 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Transform mars_facts into dataframe\n",
    "facts_df = mars_facts[0]\n",
    "# print(facts_df)\n",
    "\n",
    "# Add column header to make it look pretty\n",
    "facts_df.columns = [\"Fact\", \"Fact Value\"]\n",
    "\n",
    "# Set Fact as indes\n",
    "facts_df.set_index(\"Fact\", inplace=True)\n",
    "\n",
    "# Print results\n",
    "facts_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save html code\n",
    "html_table = facts_df.to_html()\n",
    "# print(html_table)\n",
    "\n",
    "# Clean up table to make it look pretty\n",
    "html_table.replace(\"\\n\", '')\n",
    "# print(html_table)\n",
    "\n",
    "# Save html code to folder\n",
    "facts_df.to_html(\"facts_about_mars.html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "# # Close the browser after scraping\n",
    "# browser.quit()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 90.0.4430\n",
      "Get LATEST driver version for 90.0.4430\n",
      "Driver [C:\\Users\\cperr\\.wdm\\drivers\\chromedriver\\win32\\90.0.4430.24\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    " # Set up Splinter, visit url\n",
    "hemisphere_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "time.sleep(1)\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "browser.visit(hemisphere_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape page into Soup\n",
    "hemisphere_html = browser.html\n",
    "soup = bs(hemisphere_html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\cperr\\anaconda3\\lib\\site-packages\\splinter\\driver\\webdriver\\__init__.py:490: FutureWarning: browser.find_link_by_partial_text is deprecated. Use browser.links.find_by_partial_text instead.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<h3>Cerberus Hemisphere Enhanced</h3>, <h3>Schiaparelli Hemisphere Enhanced</h3>, <h3>Syrtis Major Hemisphere Enhanced</h3>, <h3>Valles Marineris Hemisphere Enhanced</h3>]\n"
     ]
    }
   ],
   "source": [
    "# Identify name of images and loop through it to grab teh name of the titles\n",
    "names = soup.find_all(\"h3\")\n",
    "for name in names:\n",
    "    #Clicks in a link by looking for partial content of href attribute\n",
    "    browser.click_link_by_partial_text(\"Hemisphere\")\n",
    "#Test result        \n",
    "print(names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Loop through data for each Mars Hemisphere and grab the necessary elements/objects\n",
    "hemispheres = soup.find_all(\"div\", class_=\"description\")\n",
    "hemisphere_dict={}\n",
    "hemisphere_image_urls=[]\n",
    "for i in hemispheres:\n",
    "    link = i.find('a')\n",
    "    href = link['href']\n",
    "    title = link.find('h3').text\n",
    "    main_url = \"https://astrogeology.usgs.gov\" + href\n",
    "    browser.visit(main_url)\n",
    "    html = browser.html\n",
    "    soup = bs(html, 'html.parser')\n",
    "    pic = soup.find(\"a\", target=\"_blank\")\n",
    "    pic_href = pic['href']\n",
    "    hemisphere_image_urls.append({\"title\":title,\"img_url\":pic_href})\n",
    "#Test results\n",
    "    #print(hemisphere_image_urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://www.usgs.gov/centers/astrogeo-sc'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://www.usgs.gov/centers/astrogeo-sc'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://www.usgs.gov/centers/astrogeo-sc'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://www.usgs.gov/centers/astrogeo-sc'}]"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Final product\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Close the browser after scraping\n",
    "browser.quit()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:root] *",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
