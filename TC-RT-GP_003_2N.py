# Тест-кейс: TC-RT-GP_003_2N
#
# Описание: Проверить, что при вводе клиентом мобильного номера
# телефона система отправляет код на введеный номер. Открывается окно для ввода кода.
# Введен не верный код.
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=1226354536


import time
from selenium.webdriver.common.by import By
from settings import valid_number_phone

def test_TC_RT_GP_003_2N(selenium):
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
   input_field.send_keys(valid_number_phone)

   time.sleep(5)

   get_code_button_name = 'otp_get_code'
   get_code_button = selenium.find_element('name', get_code_button_name)
   get_code_button.submit()

   time.sleep(5)

   h1_class = 'card-container__title'
   h1 = selenium.find_element(By.CLASS_NAME, h1_class)
   assert h1.text == 'Код подтверждения отправлен'

   code_0_id = 'rt-code-0'
   code_0 = selenium.find_element('id', code_0_id)
   code_0.send_keys('1')

   code_1_id = 'rt-code-1'
   code_1 = selenium.find_element('id', code_1_id)
   code_1.send_keys('1')

   code_2_id = 'rt-code-2'
   code_2 = selenium.find_element('id', code_2_id)
   code_2.send_keys('1')

   code_3_id = 'rt-code-3'
   code_3 = selenium.find_element('id', code_3_id)
   code_3.send_keys('1')

   code_4_id = 'rt-code-4'
   code_4 = selenium.find_element('id', code_4_id)
   code_4.send_keys('1')

   code_5_id = 'rt-code-5'
   code_5 = selenium.find_element('id', code_5_id)
   code_5.send_keys('1')

   time.sleep(30)

   h_error_class = 'code-input-container__error'
   h_error = selenium.find_element(By.CLASS_NAME, h_error_class)
   assert h_error.text == 'Неверный код. Повторите попытку'

   selenium.save_screenshot('screenshots/TC-RT-GP_003_2N.png')

   time.sleep(2)