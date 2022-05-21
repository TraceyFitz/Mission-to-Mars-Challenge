# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

def scrape_all():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    
    
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)


    # In[4]:


    # With the following line, browser.is_element_present_by_css('div.list_text', wait_time=1), we are accomplishing two things.
    # One is that we're searching for elements with a specific combination of tag (div) and attribute (list_text). As an example, ul.item_list would be found in HTML as <ul class="item_list">.
    # Secondly, we're also telling our browser to wait one second before searching for components. The optional delay is useful because sometimes dynamic pages take a little while to load, especially if they are image-heavy.


    # In[5]:


    #set up the HTML parser:
    html = browser.html
    news_soup = soup(html, 'html.parser')
    slide_elem = news_soup.select_one('div.list_text')


    # In[6]:


    #we've assigned slide_elem as the variable to look for the <div /> tag and its descendent 
    #(the other tags within the <div /> element)? This is our parent element. 
    #This means that this element holds all of the other elements within it, 
    #and we'll reference it when we want to filter search results even further. 
    #The . is used for selecting classes, such as list_text, so the code 'div.list_text' pinpoints the <div /> tag with the class of list_text. 
    # CSS works from right to left, such as returning the last item on the list instead of the first. 
    # Because of this, when using select_one, the first matching element returned will be a <li /> element with a class of slide and all nested elements within it.


    # In[7]:


    #assign the title and summary text to variables we'll reference later.
    slide_elem.find('div', class_='content_title')


    # In[8]:


    #use the parent element to find the first 'a' tage and save it as 'news_title'
    news_title = slide_elem.find('div', class_='content_title').get_text()
    news_title


    # In[9]:


    #We've added something new to our .find() method here: .get_text(). 
    #When this new method is chained onto .find(), only the text of the element is returned. 
    #The code above, for example, would return only the title of the news article and not any of the HTML tags or elements.


    # In[10]:


    #if we were to use .find_all() instead of .find() when pulling the summary, we would retrieve all of the summaries on the page instead of just the first one.
    #use the parent element to find the paragraph text
    news_paragraph = slide_elem.find('div', class_='article_teaser_body').get_text()
    news_paragraph


    # ### Featured Images in Markdown 

    # In[11]:


    # visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)


    # In[12]:


    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()


    # In[13]:


    #Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')


    # In[14]:


    # Find the relative image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    img_url_rel


    # In[15]:


    # Use the base URL to create an absolute URL
    featured_image = 'https://spaceimages-mars.com/'+ img_url_rel
    featured_image
 

    # In[16]:


    #Convert webspage scaped table to a dataframe
    df = pd.read_html('https://galaxyfacts-mars.com')[0]
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    df


    # In[17]:


    mars_facts = df.to_html


    # In[18]:


    #end browser session
    # browser.quit()


    # In[21]:
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'

    browser.visit(url)
    #set up the HTML parser:
    html = browser.html
    news_soup = soup(html, 'html.parser')


    # In[22]:


    # display(news_soup)


    # In[23]:


    image_list = news_soup.find_all('div', class_='item')
    image_list


    # In[24]:


    len(image_list)


    # In[25]:


    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    for image in image_list:
        url = image.find('a')['href']
        title = image.find('div', class_='description').find('a').find('h3').text
        full_url = 'https://marshemispheres.com/'+ url 
        browser.visit(full_url)
        html = browser.html
        news_soup = soup(html, 'html.parser')
        full_image = news_soup.find('div', class_='downloads').find('ul').find('li').find('a')['href']
        hemisphere_image_urls.append({'title':title, 'full_image':full_image})
    hemisphere_image_urls
    
    
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image,
        "facts": mars_facts,
        "title": title,
        "img_url": full_image    
    }
    return data
print (scrape_all)

    # In[ ]:





    # In[ ]:




