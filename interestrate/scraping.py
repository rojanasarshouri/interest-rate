from selenium import webdriver
from selenium.webdriver.common.by import By
from . import db, InterestRate

def scrape_interest_rates():
    driver = webdriver.Chrome()
    driver.get('https://tradingeconomics.com/country-list/interest-rate')

    table = driver.find_element(By.CLASS_NAME, 'card')

    for row in table.find_elements(By.TAG_NAME, 'tr')[1:]:  
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) > 1:  
            country = cells[0].text
            interest_rate = cells[1].text
            
            new_rate = InterestRate(country=country, interest_rate=interest_rate)
            db.session.add(new_rate)  

    db.session.commit()  
    driver.quit()