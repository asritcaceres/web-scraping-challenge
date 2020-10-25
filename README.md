# Mission to Mars

## Scraping:
Scraped the NASA Mars News Site and collect the latest News Title and Paragraph Text

Used splinter to navigate the site and find the image url on the https://www.jpl.nasa.gov site.

Visited the Mars Facts webpage and pulled the table using Pandas and then converterd it into am html table.

Visited the USGS Astrogeology site to get the full images of the hemispheres using a for loop to add to a dictionary at the end

## Flask
Used PyMongo to connect the Mondo connection, created the routes necessary to pull the data. Had to create scrape_mars to put in the syntax created in Jupyter Notebook to have that pulled into the app.py to put the information into the collection

Created the index.html page and used the variables created in the flask to pull the data into a localhost and create a webpage with the Mars facts. 