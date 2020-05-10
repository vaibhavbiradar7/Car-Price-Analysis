#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list = ['https://www.autolist.com/listings#page=1&latitude=28.1147&location=Tampa%2C+FL&longitude=-82.3678', 
        'https://www.autolist.com/listings#page=1&latitude=33.7489954&location=Atlanta%2C+GA&longitude=-84.3879824',
        'https://www.autolist.com/listings#page=1&latitude=34.0522342&location=Los+Angeles%2C+CA&longitude=-118.2436849',
        'https://www.autolist.com/listings#page=1&latitude=40.826489&location=Rutherford%2C+NJ&longitude=-74.10680909999999',
        'https://www.autolist.com/listings#page=1&latitude=42.3600825&location=Boston%2C+MA&longitude=-71.0588801',
        'https://www.autolist.com/listings#page=1&latitude=29.7604267&location=Houston%2C+TX&longitude=-95.3698028',
        'https://www.autolist.com/listings#page=1&latitude=41.408969&location=Scranton%2C+PA&longitude=-75.66241219999999&radius=50',
        'https://www.autolist.com/listings#page=1&latitude=40.44062479999999&location=Pittsburgh%2C+PA&longitude=-79.9958864&radius=50',
        'https://www.autolist.com/listings#page=1&latitude=44.76339429999999&location=Carver%2C+MN&longitude=-93.6254404&radius=50',
        'https://www.autolist.com/listings#page=1&latitude=38.6358808&location=Xenia%2C+IL&longitude=-88.6347744&radius=50',
        'https://www.autolist.com/listings#page=1&latitude=37.568694&location=Berea%2C+KY&longitude=-84.2963223&radius=50',
        'https://www.autolist.com/listings#page=1&radius=50&latitude=44.6522362&location=Mio%2C+MI&longitude=-84.1297276',
        'https://www.autolist.com/listings#page=1&radius=50&latitude=32.6926512&location=Yuma%2C+AZ&longitude=-114.6276916',
        'https://www.autolist.com/listings#page=1&radius=50&latitude=33.4483771&location=Phoenix%2C+AZ&longitude=-112.0740373',
        'https://www.autolist.com/listings#page=1&radius=50&latitude=25.7616798&location=Miami%2C+FL&longitude=-80.1917902',
        'https://www.autolist.com/listings#page=1&radius=50&latitude=40.813616&location=Lincoln%2C+NE&longitude=-96.7025955',
        'https://www.autolist.com/listings#page=1&radius=50&latitude=32.3792233&location=Montgomery%2C+AL&longitude=-86.3077368',
        'https://www.autolist.com/listings#page=1&latitude=36.1699412&location=Las+Vegas%2C+NV&longitude=-115.1398296',
        'https://www.autolist.com/listings#page=1&latitude=39.4703246&location=Alaska%2C+IN&longitude=-86.6413912',
        'https://www.autolist.com/listings#page=1&latitude=37.8806341&location=Nicholasville%2C+KY&longitude=-84.5729961',
        'https://www.autolist.com/listings#page=1&latitude=45.3375&location=Wyoming%2C+MN&longitude=-92.9980556']

   
# getting length of list 
length = len(list) 
   
# Iterating the index 
# same as 'for i in range(len(list))' 
for i in range(length): 

    print('screen_shot'+ str(i) +'.png')


# In[ ]:


from selenium import webdriver
from PIL import Image
from selenium.webdriver.chrome.options import Options
import time

#urls = ['https://www.autolist.com/listings#page=1&latitude=28.1147&location=Tampa%2C+FL&longitude=-82.3678', 'https://www.autolist.com/listings#page=1&latitude=33.7489954&location=Atlanta%2C+GA&longitude=-84.3879824','https://www.autolist.com/listings#page=1&latitude=34.0522342&location=Los+Angeles%2C+CA&longitude=-118.2436849','https://www.autolist.com/listings#page=1&latitude=40.826489&location=Rutherford%2C+NJ&longitude=-74.10680909999999']
length = len(list)
for i in range(length): 
     
    url = list[i]

    #run first time to get scrollHeight
    driver = webdriver.Chrome()
    driver.get(url)
    #pause 3 second to let page load
    time.sleep(3)
    #get scroll Height
    height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
    print(height)
    #close browser
    driver.close()

    #Open another headless browser with height extracted above
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"--window-size=1920,{height}")
    chrome_options.add_argument("--hide-scrollbars")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    #pause 3 second to let page loads
    time.sleep(3)
    #save screenshot
    driver.save_screenshot(r'C:\Users\srira\OneDrive\Desktop\dump\screen_shot'+ str(i) +'.png')
    driver.close()

