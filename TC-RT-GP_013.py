# Тест-кейс: TC-RT-GP_013
#
# Описание:
#
# Ссылка на тест-кейс:

import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_TC_RT_GP_013(selenium):
   selenium.get('https://rostov.rt.ru/')

   time.sleep(5)

   def is_exist(param, locator):
      try:
         selenium.find_element(param, locator)
      except NoSuchElementException:
         return False
      return True

   time.sleep(5)

   selenium.save_screenshot('screenshots/TC-RT-GP_013_before.png')

   change_region_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[5]/div/div/div[2]/div[3]/button[2]'
   change_region_button = selenium.find_element(By.XPATH, change_region_button_xpath)
   change_region_button.click()

   time.sleep(2)

   change_region_xpath = '/html/body/div[2]/div/div/header/div[1]/div[2]/div[2]'
   assert is_exist(By.XPATH, change_region_xpath) == True

   selenium.save_screenshot('screenshots/TC-RT-GP_013_after.png')

