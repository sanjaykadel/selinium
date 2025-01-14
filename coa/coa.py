import os
# os.system('cls')

from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fun_utils
u = fun_utils


def run(**k):
    u.dfn()

    driver = k.get('driver')

    curl = f'{u.getUrl()}?_P_PAGE_=entity\components\general_component\coa\ET_AC_COA_CUSTOM.html&layoutPath=base_fragment/base.html'
    if driver.current_url != curl:
        u.err('driver.current_url != curl')
        driver.get(curl)

    WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "class_oiss_gen_content_ET_AC_COA")))
    
    form = driver.find_element(
        By.CLASS_NAME, "class_oiss_gen_form_ET_AC_COA") 
   
    el = u.ufind_element(driver, form, By.NAME, "id")
    el.send_keys("1")
   
    el = u.ufind_element(driver, form, By.NAME, "acType")
    el.click()
    u.dsend_keys(el, Keys.ARROW_DOWN)
    u.dsend_keys(el, Keys.ENTER)

    el = u.ufind_element(driver, form, By.NAME, "acName")
    el.send_keys("Dinesh")
       
    el = u.ufind_element(driver, form, By.NAME, "acCode")
    el.send_keys("9672515451541")
       
    el = u.ufind_element(driver, form, By.NAME, "normalBalance")
    el.send_keys("4587561")
    u.ui_send_date(driver=driver,form=form,name="dateOpen",value="2080-04-03")
    u.ui_send_date(driver=driver,form=form,name="dateClosed",value="2080-10-03")
    
    el = form.find_element(By.CLASS_NAME, "class_oiss_gen_btn_create")
    el.send_keys(Keys.ENTER)