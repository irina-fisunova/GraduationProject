# Тест-кейс: TC-RT-GP_015
#
# Описание: Проверить, что при нажатии кнопку выбора вариантов тарифа открывается набор доступных тарифов.
# При нажании кнопки "Подключить", открывается окно "Заявка на подключение".
#
# Ссылка на тест-кейс: https://docs.google.com/spreadsheets/d/1PE9EcK4a1cdgjxku7rX65zSYG03LKn5U/edit#gid=465133267

import time
from settings import close_confirm_and_cookies

def test_TC_RT_GP_015(selenium):
   selenium.get('https://rostov.rt.ru/')

   close_confirm_and_cookies(selenium)

   tarif_change_button_xpath = '/html/body/div[2]/div/div/main/div/div/div[1]/div/div[3]/article[2]/div/div/div[2]/div/div/noindex/section/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/button'
   tarif_change_button = selenium.find_element('xpath', tarif_change_button_xpath)
   tarif_change_button.click()

   time.sleep(2)

   select_tarif_button_xpath = '/html/body/div[2]/div/div/main/div/div/div[1]/div/div[3]/article[2]/div/div/div[2]/div/div/noindex/section/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/section/div[2]/div/div/div[3]/button'
   select_tarif_button = selenium.find_element('xpath', select_tarif_button_xpath)
   select_tarif_button.click()

   time.sleep(7)

   requast_tarif_xpath = '/html/body/div[2]/div/div/main/div/div/div[1]/div/div[3]/article/div/div/div/section/div/div/div/div[1]/div[1]'
   requast_tarif = selenium.find_element('xpath', requast_tarif_xpath)
   assert requast_tarif.text == 'Заявка на подключение'

   h_tarif_xpath = '/html/body/div[2]/div/div/main/div/div/div[1]/div/div[3]/article/div/div/div/section/div/div/div/div[1]/div[3]/div[1]/div/div[1]/p[1]'
   h_tarif = selenium.find_element('xpath', h_tarif_xpath)
   assert h_tarif.text == 'Технологии выгоды'

   selenium.save_screenshot('screenshots/TC-RT-GP_015.png')




