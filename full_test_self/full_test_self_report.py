
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

    #print('kargs', k)
    # driver = k.get('driver')
    # curl=f'{u.getUrl()}/?_P_PAGE_=entity\components\BE_OISS_USERS_CUSTOM.html'
    # if driver.current_url != curl:
    #     u.err('driver.current_url != curl')
    
#     driver.get(curl)

#     WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_BE_OISS_USERS")))
#     emp_reg_submission_no = driver.execute_script('return window.localStorage.getItem("EMP_REG_SUBMISSSION_NO");')

#     form = driver.find_element(By.TAG_NAME, "form")
#     input_tag = form.find_element(By.NAME, "username")
#     input_tag.send_keys(emp_reg_submission_no)


#     input_tag = form.find_element(By.NAME, "password")
#     input_tag.send_keys(emp_reg_submission_no)


#     btn = driver.find_element(By.ID, "oiss_id_log_in")
#     btn.click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "Reports")))


    link=driver.find_element(By.CLASS_NAME,"Reports")
    print('link0',link)
    link.click()

#     link=driver.find_element(By.CLASS_NAME,"coll")
#     print('link0',link)
#     link.click()


    u.dfn()

    


    
    

