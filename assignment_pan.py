from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# from selenium.webdriver.support import expected_conditions as EC
import time

# with open("job_scrapper.csv", "w") as file:
#     file.write("job_search, job_location, job_name, company_name, location \n")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0')

driver.maximize_window()
time.sleep(1)
    
job_search= driver.find_element(By.ID, "job-search-bar-keywords")
job_search.send_keys("Frontend developers")
job_search.click()


job_search.send_keys(Keys.ENTER)
    

job_name = driver.find_elements(By.CLASS_NAME, "base-search-card__title")
for jobs in job_name:
    print(jobs.text)

company_name = driver.find_elements(By.CLASS_NAME, "base-search-card__subtitle") 
for i in company_name:
    print(i.text)
    
location = driver.find_elements(By.CLASS_NAME, "job-search-card__location")
for locations in location:
    print(locations.text)     
            
last_posted = driver.find_elements(By.CLASS_NAME, "core-section-container__content break-words")      
for posts in last_posted:
    print(posts.text)           
       
with open("job_scrapper.csv", "w") as file:
    for i in range(len(location)):
        file.write(job_name[i].text + "," + company_name[i].text + "," + location[i].text + "\n")

    

