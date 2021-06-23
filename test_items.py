import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_add_to_basket_btn(browser):
    browser.get(link)

    try:
        add_to_basket_btn = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'btn-add-to-basket'))
        )
    except TimeoutException:
        add_to_basket_btn = False

    assert add_to_basket_btn, '"Add to basket" button is missing on the product page'
