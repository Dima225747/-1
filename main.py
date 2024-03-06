from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://omsk.cian.ru/kupit-kvartiru-1-komn-ili-2-komn/'

# Инициализация драйвера браузера
driver = webdriver.Chrome()
driver.get(url)

# Ждем 10 секунд для полной загрузки страницы
driver.implicitly_wait(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')

apartments = soup.find_all('div', class_='_93444fe79c--wrapper--W0WqH')

data = []
for apartment in apartments:
    title_element = apartment.find('span', class_='_93444fe79c--color_primary_100--AuVro _93444fe79c--lineHeight_28px--KFXmc _93444fe79c--fontWeight_bold--BbhnX _93444fe79c--fontSize_22px--sFuaL _93444fe79c--display_block--KYb25 _93444fe79c--text--e4SBY _93444fe79c--text_letterSpacing__normal--tfToq' )
    title = title_element.text.strip() if title_element else 'Нет данных'

    price_element = apartment.find('span', class_='_93444fe79c--color_black_100--Ephi7 _93444fe79c--lineHeight_28px--KFXmc _93444fe79c--fontWeight_bold--BbhnX _93444fe79c--fontSize_22px--sFuaL _93444fe79c--display_block--KYb25 _93444fe79c--text--e4SBY _93444fe79c--text_letterSpacing__normal--tfToq')
    price = price_element.text.strip() if price_element else 'Цена не указана'

    data.append([title, price])

driver.quit()

df = pd.DataFrame(data, columns=['Название', 'Цена'])
df.to_excel('apartments.xlsx', index=False)
