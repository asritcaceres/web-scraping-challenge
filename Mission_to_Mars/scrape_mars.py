from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    executable_path = {"executable_path":"Mission_to_Mars/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)

def scrape():
    browser = init_browser()
    
    #vist the site
    url = "https://mars.nasa.gov/news/"

    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    #find titles
    titles= soup.find_all('div', class_="content_title")

    #find paragraphs in titles
    paragraphs = soup.find_all('div', class_="article_teaser_body")

    #find first title
    news_title = titles[1].text

    #find paragraph for title
    news_p= paragraphs[0].text   

    #Featured Image
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html_2 = browser.html
    img_soup = BeautifulSoup(html_2, 'html.parser')

    
    
    #find image
    image = img_soup.find('div', class_="carousel_items").find('a').get('data-fancybox-href')
    main_url =  "https://jpl.nasa.gov" 
    featured_img_url =  main_url  + image
    #featured_img_url


    #Mars Facts
    url_3 = "https://space-facts.com/mars/"

    #reading url
    mars_table = pd.read_html(url_3)
        
    #Creating the DataFrame
    df=mars_table[0]
    df.columns=["", "Value"]
    df.set_index("", inplace=True)

    #converting to HTML
    mars_table_html = df.to_html()
    #mars_table_html.replace('\n', '')

    # Mars Hemisphere
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)
   
    html_3 = browser.html
    hem_soup = BeautifulSoup(html_3, 'html.parser')

    results = hem_soup.find_all('div', class_="item")
    hemisphere_image_urls =[]

    for result in results:
        info_dict= {}
        titles = result.find('h3').text
        link_small = result.find('a', class_="itemLink product-item")['href']
        full_link = "https://astrogeology.usgs.gov/" + link_small
        browser.visit(full_link)
        html_4 = browser.html
        links_soup = BeautifulSoup(html_4, 'html.parser')
        
        img_class = links_soup.find('div', class_='downloads')
        full_image_url = img_class.find('a')["href"]
        print(titles)
        print(full_image_url)
        info_dict['title']= titles
        info_dict['image_url']= full_image_url
        hemisphere_image_urls.append(info_dict)     
#store in dict
    mars_data = {
        "news_title": news_title,
        "news_p":news_p,
        "featured_image":featured_img_url,
        "mars_table":mars_table_html,
        "hemispheres": hemisphere_image_urls
    }
   

    # Closing Browser
    browser.quit()

    # Return results
    return mars_data

    

