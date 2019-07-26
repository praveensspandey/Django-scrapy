# Django-scrapy
This project scraps the top rated movies from IMDb using Scrapy.
This also connect Scrapy and Django together
the scraped data is added to the python model and saved into data base.

# Requirements
Inoder to run this project install
Django and scrapy 

# To run 
First Go to Scraper project director 
eg.

\webscraping\Webscraper\webscraping\scraper\

run command 

**scrapy crawl crawler**

This will pull all the data from the IMDb site

Then run Django runserver command
Change to 

\webscraping\Webscraper\webscraping\

and run 

**python manage.py runserver**
