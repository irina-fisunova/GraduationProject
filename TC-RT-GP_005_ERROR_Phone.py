import time
from selenium.webdriver.common.by import By

def test_TC_RT_GP_005(selenium):
   selenium.get('https://rostov.rt.ru/')
   burger_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[1]'
   burger_button = selenium.find_element('xpath', burger_button_xpath)
   burger_button.click()

   time.sleep(5)

   login_link_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[4]/div/div/div/div/div/a'
   login_link = selenium.find_element('xpath', login_link_xpath)
   login_link.click()

   time.sleep(5)

   input_field_id = 'address'
   input_field = selenium.find_element('id', input_field_id)
   input_field.send_keys('1')

   time.sleep(5)

   get_code_button_name = 'otp_get_code'
   get_code_button = selenium.find_element('name', get_code_button_name)
   get_code_button.submit()

   time.sleep(5)

   h_number_error_class = 'rt-input-container__meta rt-input-container__meta--error'
   h_number_error = selenium.find_element(By.CLASS_NAME, h_number_error_class)
   assert h_number_error.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

   #h1_class = 'card-container__title'
   #h1 = selenium.find_element(By.CLASS_NAME, h1_class)
   #assert h1.text == 'Код подтверждения отправлен'

   time.sleep(5)