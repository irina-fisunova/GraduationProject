# Тест-кейс: TC-RT-GP_006
#
# Описание: Проверить, что при вводе клиентом корректного,  но ошибочного
# адреса электронной ночты, из формы "Код подтверждения отправлен", нажав
# кнопку "Изменить почту", система откроет форму "Авторизация".

#Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=228646860

import time
from selenium.webdriver.common.by import By
from settings import wrong_email, close_confirm_and_cookies

def test_TC_RT_GP_006(selenium):
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
   input_field.send_keys(wrong_email)

   time.sleep(10)

   get_code_button_name = 'otp_get_code'
   get_code_button = selenium.find_element('name', get_code_button_name)
   get_code_button.submit()

   time.sleep(10)

   h1_class = 'card-container__title'
   h1 = selenium.find_element(By.CLASS_NAME, h1_class)
   assert h1.text == 'Код подтверждения отправлен'

   selenium.save_screenshot('screenshots/TC-RT-GP_006_before.png')

   time.sleep(1)

   change_email_name = 'otp_back_phone'
   change_email = selenium.find_element('name', change_email_name)
   change_email.click()

   time.sleep(5)

   selenium.save_screenshot('screenshots/TC-RT-GP_006_after.png')

   h2_class = 'card-container__title'
   h2 = selenium.find_element(By.CLASS_NAME, h2_class)
   assert h2.text == 'Авторизация по коду'

   time.sleep(5)