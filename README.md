# Web Scraping - Mission to Mars

## Background 

Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, being only larger than Mercury. In English, Mars carries the name of the Roman god of war and is often referred to as the "Red Planet".

In this Project, I build a web application that scrapes various websites for data related to the Mission to Mars and displayed the information in a single HTML page.

![mission_to_mars](Images/mission_to_mars.png)

## Step 1 - Scraping

The initial scraping is conducted by using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter, and a Jupyter Notebook file called [mssion_to_mars.ipynb](Missions_to_Mars/mssion_to_mars.ipynb) is used to complete all the scraping and analysis tasks.

### NASA Mars News

* I scraped the [NASA Mars News Site](https://redplanetscience.com/)and collected the latest News Title and Paragraph Text. The result looks as follows:


### JPL Mars Space Images - Featured Image

* I Visited the url for Featured Space Image (https://spaceimages-mars.com/), and used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* The image url is setuped to the full size `.jpg` image, and saved a complete url string for this image.
The output looks as follows:

### Mars Facts

* I Visited the Mars Facts webpage (https://galaxyfacts-mars.com/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc and converted the data to a HTML table string.


### Mars Hemispheres

* I visited the USGS Astrogeology site [here](https://marshemispheres.com/), and  obtained high resolution images for each of Mar's hemispheres.

* I clicked each of the links to the hemispheres in order to find the image url to the full resolution image. Then, I saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name, and stored in the a Python dictionary by using the keys `img_url` and `title`.

## Step 2 - MongoDB and Flask Application

I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs. Then after, I converted the Jupyter notebook into a Python script called [mssion_to_mars.ipynb](Missions_to_Mars/mssion_to_mars.ipynb) with a function called `scrape` that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, I created a route called `/scrape` that will import [scrape_mars.py](Missions_to_Mars/scrape_mars.py) script and call `scrape` function.


