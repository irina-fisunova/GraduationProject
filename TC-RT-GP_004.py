# Тест-кейс: TC-RT-GP_004
#
# Описание: Проверить, что при вводе клиентом корректного адреса электнонной
# почты, система отправляет код по указанному адресу. Открывается окно для ввода кода.
# После введения кода система система аутенфицирует клиента.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=158308005
#
# Примечание: Автотест предполагает открытие окна для ввода кода как успешный результат, т.к. ввести полученный код
# на электронную почту не представляется возможным.

import time
from selenium.webdriver.common.by import By
from settings import valid_email, close_confirm_and_cookies

def test_TC_RT_GP_004(selenium):
   selenium.get('https://rostov.rt.ru/')

   close_confirm_and_cookies(selenium)

   burger_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[4]/div/div/div/div/div/a/span'
   burger_button = selenium.find_element('xpath', burger_button_xpath)
   burger_button.click()

   time.sleep(10)

   h1_class = 'card-container__title'
   h1 = selenium.find_element(By.CLASS_NAME, h1_class)
   if h1.text == 'Авторизация':
      temporary_code_button_name = 'back_to_otp_btn'
      temporary_code_button = selenium.find_element('name', temporary_code_button_name)
      temporary_code_button.click()

   time.sleep(5)

   h1_class = 'card-container__title'
   h1 = selenium.find_element(By.CLASS_NAME, h1_class)
   assert h1.text == 'Авторизация по коду'

   time.sleep(2)

   input_field_id = 'address'
   input_field = selenium.find_element('id', input_field_id)
   input_field.send_keys(valid_email)

   time.sleep(5)

   get_code_button_name = 'otp_get_code'
   get_code_button = selenium.find_element('name', get_code_button_name)
   get_code_button.submit()

   time.sleep(20)

   h1_class = 'card-container__title'
   h1 = selenium.find_element(By.CLASS_NAME, h1_class)
   assert h1.text == 'Код подтверждения отправлен'

   selenium.save_screenshot('screenshots/TC-RT-GP_004.png')

   time.sleep(5)