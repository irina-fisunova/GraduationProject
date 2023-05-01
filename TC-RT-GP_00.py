# Тест-кейс: TC-RT-GP_00
#
# Описание:
#
# Ссылка на тест-кейс:

import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_TC_RT_GP_00(selenium):
   selenium.get('https://rostov.rt.ru/')

   time.sleep(15)

