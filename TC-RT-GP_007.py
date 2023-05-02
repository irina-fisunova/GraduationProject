# Тест-кейс: TC-RT-GP_007
#
# Описание: Проверить, что при при первоначальной загрузке страницы отображается правильный город по умолчанию.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=853069936

import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def test_TC_RT_GP_007(selenium):
   selenium.get('https://rostov.rt.ru/')

   time.sleep(5)

   try:
      region_xpath = '/html/body/div[3]/div/div/header/div[1]/div[3]/div/div[2]/div/div/div/a/span'
      region_element = selenium.find_element(By.XPATH, region_xpath)
      DEFAULT_CITY_NAME = 'Ростов-на-Дону'
      assert region_element.text == DEFAULT_CITY_NAME
   except NoSuchElementException as e:
      print(e.msg)
   finally:
      print("Element: region_element")

   time.sleep(5)

   selenium.save_screenshot('screenshots/TC-RT-GP_007.png')