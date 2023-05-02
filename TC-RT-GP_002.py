# Тест-кейс: TC-RT-GP_002
#
# Описание: Проверить, что при вводе клиентом корректных
# данных: электронной почты и пароля система переходит к
# следующему шагу - авторизации клиента.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=107134494
#
# Примечание: Автотест предполагает открытие окна Авторизации для ввода
# электронной почты и пароля ранее зарегистрированного клиента, с последующей
# авторизацией клинта.

import time
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password, close_confirm_and_cookies

def test_TC_RT_GP_002(selenium):
   selenium.get('https://rostov.rt.ru/')

   close_confirm_and_cookies(selenium)

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

   password_email_id = 't-btn-tab-mail'
   password_email = selenium.find_element('id', password_email_id)
   password_email.click()

   time.sleep(2)

   input_email_id = 'username'
   input_email = selenium.find_element('id', input_email_id)
   input_email.send_keys(valid_email)

   time.sleep(2)

   input_password_id = 'password'
   input_password = selenium.find_element('id', input_password_id)
   input_password.send_keys(valid_password)

   time.sleep(2)

   get_password_button_name = 'login'
   get_password_button = selenium.find_element('name', get_password_button_name)
   get_password_button.submit()

   time.sleep(10)

   selenium.get('https://rostov.rt.ru/')

   time.sleep(5)

   burger_2_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[1]/div[2]'
   burger_2_button = selenium.find_element('xpath', burger_2_button_xpath)
   burger_2_button.click()

   time.sleep(5)

   selenium.save_screenshot('screenshots/TC-RT-GP_002.png')

   h1_personal_account_class = 'rtk-user-panel__link'
   h1_personal_account = selenium.find_element(By.CLASS_NAME, h1_personal_account_class)
   assert h1_personal_account.text == 'Личный кабинет'

   time.sleep(5)