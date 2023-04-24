# Тест-кейс: TC-RT-GP_005
# Описание: Проверить, что при вводе клиентом мобильного номера
# телефона система отправляет код на введеный номер. После введения
# кода система система аутенфицирует клиента.
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=1226354536
# Примечание: Автотест предполагает открытие окна для ввода кода как успешный результат, т.к. получить код приходящий
# на телефон не представляется возможным.

import time
from selenium.webdriver.common.by import By

def test_TC_RT_GP_005(selenium):
   selenium.get('https://rostov.rt.ru/')
   burger_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[1]'
   burger_button = selenium.find_element('xpath', burger_button_xpath)
   burger_button.click()

   time.sleep(5)

   login_link_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[4]/div/div/div/div/div/a'
   login_link =  selenium.find_element('xpath', login_link_xpath)
   login_link.click()

   time.sleep(10)

   input_field_id = 'address'
   input_field = selenium.find_element('id', input_field_id)
   input_field.send_keys('sf.gp.rt.2023@gmail.com')

   time.sleep(10)

   get_code_button_name = 'otp_get_code'
   get_code_button = selenium.find_element('name', get_code_button_name)
   get_code_button.submit()

   time.sleep(10)

   h1_class = 'card-container__title'
   h1 = selenium.find_element(By.CLASS_NAME, h1_class)
   assert h1.text == 'Код подтверждения отправлен'

   time.sleep(1)

   change_email_name = 'otp_back_phone'
   change_email = selenium.find_element('name', change_email_name)
   change_email.click()

   time.sleep(5)

   h2_class = 'card-container__title'
   h2 = selenium.find_element(By.CLASS_NAME, h2_class)
   assert h2.text == 'Авторизация по коду'

   time.sleep(5)