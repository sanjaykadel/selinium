
import os
#os.system('cls')

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils
u = fun_utils


def run(**k):
    u.dfn()


    # logout
    driver = k.get('driver')
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "logout")))
    link = driver.find_element(By.CLASS_NAME, "logout")
    link.click()
    u.dsleep()



    u.dfn()

    


    
    

