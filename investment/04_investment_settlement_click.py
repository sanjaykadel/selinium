
import os

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils
u = fun_utils


def run(**k):
    u.dfn()
    
    driver = k.get('driver')
        
    
   
    u.dfn()
    
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "sidebar-content")))

    form = driver.find_element(By.CLASS_NAME, "investment-settlement")
    form.click()

    u.dfn()