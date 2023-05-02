# Тест-кейс: TC-RT-GP_008
#
# Описание: Проверить, что смена региона проходит успешно.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=1115223778

import time
from selenium.webdriver.common.by import By

def test_TC_RT_GP_008(selenium):
   selenium.get('https://rostov.rt.ru/')

   time.sleep(15)

   try:
      region_xpath = '/html/body/div[2]/div/div/header/div[1]/div[3]/div/div[2]/div/div/div/a'
      region_element = selenium.find_element(By.XPATH, region_xpath)
      region_element.click()
   finally:
      print("Element: region_element")

   time.sleep(10)

   try:
      input_city_id = 'regionSearch'
      input_city = selenium.find_element('id', input_city_id)
      NEW_CITY_NAME = 'Москва'
      input_city.send_keys(NEW_CITY_NAME)
   finally:
      print("Element: input_city")

   time.sleep(10)

   try:
      new_city_xpath = '/html/body/div[2]/div/div/header/div[1]/div[2]/div[2]/div/div/div/div/form/div/div/ul/li[1]/div/span[1]'
      new_city =  selenium.find_element(By.XPATH, new_city_xpath)
      new_city.click()
   finally:
      print("Element: new_city")

   time.sleep(10)

   try:
      city_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[4]/div/div/div/a/span'
      city_element = selenium.find_element(By.XPATH, city_xpath)
      DEFAULT_CITY_NAME = 'Москва'
      assert city_element.text == DEFAULT_CITY_NAME
   finally:
      print("Element: city_element")

   time.sleep(5)

   selenium.save_screenshot('screenshots/TC-RT-GP_008.png')