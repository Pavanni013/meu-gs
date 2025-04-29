
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def gerar_pix_bot():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://brjogos.app/login")
        time.sleep(3)

        driver.find_element(By.NAME, "username").send_keys("pavanni013")
        driver.find_element(By.NAME, "password").send_keys("Guitjs22")
        driver.find_element(By.CLASS_NAME, "login_btn").click()
        time.sleep(5)

        driver.find_element(By.XPATH, "//use[@xlink:href='#icon-btn-deposit']/..").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//*[contains(text(), 'R$100')]").click()
        time.sleep(4)

        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(4)

        chave = driver.find_element(By.XPATH, "//button[contains(@class, 'copy-btn')]/preceding-sibling::input").get_attribute("value")
        return chave
    finally:
        driver.quit()
