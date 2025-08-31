from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def test_dashboard_login():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://localhost")
        assert "Wazuh" in driver.title
        print("✓ Dashboard is accessible")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_dashboard_login()

