from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0')


driver.maximize_window()
time.sleep(1)
    
job_search= driver.find_elements(By.CLASS_NAME, "aside-section-container mb-4 similar-searches")
# print(job_search.text)

# job_names = []
# company_names = []
# locations = []   

# for item in job_search:
job_name = driver.find_element(By.CLASS_NAME, "top-card-layout__title").text
company_name = driver.find_element(By.CLASS_NAME, "topcard__flavor").text 
location = driver.find_element(By.CLASS_NAME, "topcard__flavor-row").text
#     # job_names.append(job_name)
#     company_names.append(company_name)
#     locations.append(location)
         
# # my_dict = {'job_name': job_names, 'company_name': company_names, 'location': locations}
# # df_head = pd.DataFrame(my_dict)
# # df_head.to_csv('head.csv')

# driver.quit()   


    

