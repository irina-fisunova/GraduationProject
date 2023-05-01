# Тест-кейс: TC-RT-GP_010
#
# Описание: Проверить, что при нажатии на кнопку "Принять" компонент Cookies закрывается.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=914327329

import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_TC_RT_GP_010(selenium):
   selenium.get('https://rostov.rt.ru/')

   def is_hidden(param, locator):
      return selenium.find_element(param, locator).value_of_css_property('display') == 'none'

   time.sleep(5)

   selenium.save_screenshot('screenshots/TC-RT-GP_010_before.png')

   cookies_button_xpath = '/html/body/div[2]/div/div/div[1]/div[13]/div/div/div/div/div/div/div[2]/button'
   cookies_button = selenium.find_element('xpath', cookies_button_xpath)
   cookies_button.click()

   time.sleep(2)

   cookies_container_id = 'cookie-notification'
   assert is_hidden(By.ID, cookies_container_id) == True

   selenium.save_screenshot('screenshots/TC-RT-GP_010_after.png')




