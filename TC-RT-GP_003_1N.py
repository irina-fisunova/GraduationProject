# Тест-кейс: TC-RT-GP_003_1N
#
# Описание: Проверить, что при вводе клиентом некорректного номера
# телефона система выдает сообщение "Введите телефон в формате +7ХХХХХХХХХХ
# или +375XXXXXXXXX,или email в формате example@email.ru"
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=171164967


import time
from selenium.webdriver.common.by import By
from settings import invalid_number_phone, close_confirm_and_cookies

def test_TC_RT_GP_003_1N(selenium):
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
   input_field.send_keys(invalid_number_phone)

   selenium.save_screenshot('screenshots/TC-RT-GP_003_1N_input.png')

   time.sleep(5)

   get_code_button_name = 'otp_get_code'
   get_code_button = selenium.find_element('name', get_code_button_name)
   get_code_button.submit()

   time.sleep(5)

   selenium.save_screenshot('screenshots/TC-RT-GP_003_1N_result.png')

   h_number_error_class = 'rt-input-container__meta rt-input-container__meta--error'
   h_number_error = selenium.find_element(By.CLASS_NAME, h_number_error_class)
   assert h_number_error.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

   time.sleep(5)