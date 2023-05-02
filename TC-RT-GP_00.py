# Тест-кейс: TC-RT-GP_001
#
# Описание: Проверить, что при вводе клиентом корректных
# данных: номера телефона и пароля система переходит к
# следующему шагу - авторизации клиента.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=363686659
#
# Примечание: Автотест предполагает открытие окна Авторизации для ввода номера
# телефона и пароля  ранее зарегистрированного клиента, с последующей
# авторизацией клинта.

import time

from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_TC_RT_GP_0001(selenium):
   selenium.get('https://rostov.rt.ru/')

   time.sleep(5)

   confirm_region_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[5]/div/div/div[2]/div[3]/button[1]'
   confirm_region_button = selenium.find_element(By.XPATH, confirm_region_button_xpath)
   confirm_region_button.click()

   time.sleep(1)

   cookies_button_xpath = '/html/body/div[2]/div/div/div[1]/div[13]/div/div/div/div/div/div/div[2]/button'
   cookies_button = selenium.find_element('xpath', cookies_button_xpath)
   cookies_button.click()

   time.sleep(1)

   burger_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[4]/div/div/div/div/div/a/span'
   burger_button = selenium.find_element('xpath', burger_button_xpath)
   burger_button.click()

   time.sleep(10)

   h1_class = 'card-container__title'
   h1 = selenium.find_element(By.CLASS_NAME, h1_class)
   if h1.text == 'Авторизация по коду':
      password_button_name = 'standard_auth_btn'
      password_button = selenium.find_element('name', password_button_name)
      password_button.click()

   time.sleep(5)

   h1_class = 'card-container__title'
   h1 = selenium.find_element(By.CLASS_NAME, h1_class)
   assert h1.text == 'Авторизация'

   time.sleep(2)

   password_phone_id = 't-btn-tab-phone'
   password_phone = selenium.find_element('id', password_phone_id)
   password_phone.click()

   time.sleep(2)

   input_phone_id = 'username'
   input_phone = selenium.find_element('id', input_phone_id)
   input_phone.send_keys('+79188505515')

   input_password_id = 'password'
   input_password = selenium.find_element('id', input_password_id)
   input_password.send_keys('SFGpRT2023')

   get_password_button_name = 'login'
   get_password_button = selenium.find_element('name', get_password_button_name)
   get_password_button.submit()

   time.sleep(10)

   h1_personal_account_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[4]/div/div/div/div/a'
   h1_personal_account = selenium.find_element('xpath', h1_personal_account_xpath)
   assert h1_personal_account.text == 'Личный кабинет'

   selenium.save_screenshot('screenshots/TC-RT-GP_001.png')


   time.sleep(2)

   input_remember_me_class = 'rt-checkbox__input'
   input_remember_me = selenium.find_element(By.CLASS_NAME, input_remember_me_class)
   input_remember_me.execute_script("arguments[0].click();", input_remember_me)
