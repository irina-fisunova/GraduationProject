# Тест-кейс: TC-RT-GP_011
#
# Описание: Проверить, что при нажатии на кнопку "Принять" компонент Cookies закрывается. При нажатии
# в футере страницы на компонент "Мобильное приложение" открывается модальное окно с QR-кодом.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=812537750

import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_TC_RT_GP_011(selenium):
   selenium.get('https://rostov.rt.ru/')

   time.sleep(5)

   def is_hidden(param, locator):
      return selenium.find_element(param, locator).value_of_css_property('display') == 'none'

   cookies_button_xpath = '/html/body/div[2]/div/div/div[1]/div[13]/div/div/div/div/div/div/div[2]/button'
   cookies_button = selenium.find_element('xpath', cookies_button_xpath)
   cookies_button.click()

   time.sleep(5)

   cookies_container_id = 'cookie-notification'
   assert is_hidden(By.ID, cookies_container_id) == True

   mobile_app_xpath = '/html/body/div[2]/div/div/footer/div[1]/div[3]/div/div/div/div[1]/div/div/div'
   mobile_app = selenium.find_element('xpath', mobile_app_xpath)

   actions = ActionChains(selenium)
   actions.move_to_element(mobile_app)
   actions.click(mobile_app).perform()

   time.sleep(5)

   qr_code_xpath = '/html/body/div[4]'
   assert is_hidden(By.XPATH, qr_code_xpath) == False

   selenium.save_screenshot('screenshots/TC-RT-GP_011.png')