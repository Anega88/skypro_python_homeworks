from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Shop import CheckTotalAmount


def test_total_amount():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
        )
    shop = CheckTotalAmount(driver)
    shop.log_in('standard_user', 'secret_sauce')
    shop.add_to_cart_and_checkout()
    shop.fill_in_form('Ekaterina', 'Kolesnikova', '053600')
    shop.check_total_amount(58.29)
    driver.quit()