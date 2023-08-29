from selenium import webdriver


def create_screenshot(url, save_path):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.save_screenshot(save_path)
    driver.quit()
