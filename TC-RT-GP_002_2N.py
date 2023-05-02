# Тест-кейс: TC-RT-GP_002_2N
#
# Описание: Проверить, что при вводе клиентом верного адреса электронной почты
# и неверного пароля система выдает сообщение: "Неверный логин или пароль".
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=1327519283
#
# Примечание: Автотест предполагает открытие окна Авторизации для ввода
# электронной почты и пароля ранее зарегистрированного клиента, с последующей
# авторизацией клинта.

import time
from selenium.webdriver.common.by import By

def test_TC_RT_GP_002_2N(selenium):
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

   time.sleep(5)

   password_email_id = 't-btn-tab-mail'
   password_email = selenium.find_element('id', password_email_id)
   password_email.click()

   time.sleep(2)

   input_email_id = 'username'
   input_email = selenium.find_element('id', input_email_id)
   input_email.send_keys('sf.gp.rt.2023@gmail.com')

   time.sleep(2)

   input_password_id = 'password'
   input_password = selenium.find_element('id', input_password_id)
   input_password.send_keys('SFGpRT2022')

   time.sleep(2)

   get_password_button_name = 'login'
   get_password_button = selenium.find_element('name', get_password_button_name)
   get_password_button.submit()

   time.sleep(5)

   h_error_login_password_id = 'form-error-message'
   h_error_login_password = selenium.find_element('id', h_error_login_password_id)
   assert h_error_login_password.text == 'Неверный логин или пароль'

   selenium.save_screenshot('screenshots/TC-RT-GP_002_1N.png')

   time.sleep(2)