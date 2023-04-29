# Тест-кейс: TC-RT-GP_001_2N
#
# Описание: Проверить, что при вводе клиентом верного номера
# телефона и неверного пароля система выдает сообщение: "Неверный логин или пароль".
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=373917989
#
# Примечание: Автотест предполагает открытие окна Авторизации для ввода номера
# телефона и пароля  ранее зарегистрированного клиента, с последующей
# авторизацией клинта.

import time
from selenium.webdriver.common.by import By

def test_TC_RT_GP_001_2N(selenium):
   selenium.get('https://rostov.rt.ru/')

   time.sleep(5)

   burger_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[1]'
   burger_button = selenium.find_element('xpath', burger_button_xpath)
   burger_button.click()

   time.sleep(10)

   login_link_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[4]/div/div/div/div/div/a'
   login_link =  selenium.find_element('xpath', login_link_xpath)
   login_link.click()

   time.sleep(2)

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

   time.sleep(5)