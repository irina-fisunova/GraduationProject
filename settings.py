import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# Тестовые данные:

valid_number_phone = '+79188505515'
valid_email = 'sf.gp.rt.2023@gmail.com'
valid_password = 'SFGpRT2023'

invalid_number_phone = 'nomer'
invalid_email = 'pochta.cm'
invalid_password = '123'

wrong_number_phone = '+79000000000'
wrong_email = 'sf.gp.rt.2022@gmail.com'

# Вспомогательные функции.

def is_exist(selenium, param, locator):
    try:
        selenium.find_element(param, locator)
    except NoSuchElementException:
        return False
    return True

def close_confirm_and_cookies(selenium):
   time.sleep(5)

   confirm_region_button_xpath = '/html/body/div[2]/div/div/header/div[1]/div[1]/div/div[2]/div[5]/div/div/div[2]/div[3]/button[1]'
   confirm_region_button = selenium.find_element(By.XPATH, confirm_region_button_xpath)
   confirm_region_button.click()

   time.sleep(1)

   cookies_button_xpath = '/html/body/div[2]/div/div/div[1]/div[13]/div/div/div/div/div/div/div[2]/button'
   cookies_button = selenium.find_element(By.XPATH, cookies_button_xpath)
   cookies_button.click()

   time.sleep(1)

