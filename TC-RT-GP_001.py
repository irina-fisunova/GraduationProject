# Тест-кейс: TC-RT-GP_001
# Описание: Проверить, что при вводе клиентом корректных
# данных: номера телефона и пароля система переходит к
# следующему шагу - авторизации клиента.
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=363686659
# Примечание: Автотест предполагает открытие окна Авторизации для ввода номера
# телефона и пароля  ранее зарегистрированного клиента, с последующей
# авторизацией клинта.

import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_TC_RT_GP_001(selenium):
   selenium.get('https://rostov.rt.ru/')

   time.sleep(15)

   burger_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[1]'
   burger_button = selenium.find_element('xpath', burger_button_xpath)
   burger_button.click()

   time.sleep(2)

   login_link_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[4]/div/div/div/div/div/a'
   login_link =  selenium.find_element('xpath', login_link_xpath)
   login_link.click()

   time.sleep(2)

   password_button_name = 'standard_auth_btn'
   password_button = selenium.find_element('name', password_button_name)
   password_button.click()

   time.sleep(15)

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

   time.sleep(15)

   selenium.get('https://rostov.rt.ru/')

   time.sleep(15)

   try:
      burger_2_button_xpath = 'header__burger'
      burger_2_button = WebDriverWait(selenium, 10).until(
         EC.presence_of_element_located((By.CLASS_NAME, burger_2_button_xpath))
      )
      burger_2_button.click()
   except NoSuchElementException as e:
      print(e.msg)

   # burger_2_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[1]/div[2]'
   # burger_2_button = selenium.find_element('xpath', burger_2_button_xpath)
   # burger_2_button.click()

   # time.sleep(10)

   try:
      h1_personal_account_class = 'rtk-user-panel__link'
      h1_personal_account = WebDriverWait(selenium, 10).until(
         EC.presence_of_element_located((By.CLASS_NAME, h1_personal_account_class))
      )
      assert h1_personal_account.text == 'Личный кабинет'
   except NoSuchElementException as e:
      print(e.msg)