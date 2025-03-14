from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def find_and_click(self, by_locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(by_locator))
            element.click()
            return element
        except Exception as e:
            print(f"Elemente tıklanamadı: {by_locator}. Hata: {e}")
            return None

    def is_element_visible(self, by_locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(by_locator)) is not None
        except Exception as e:
            print(f"Element görünür değil: {by_locator}. Hata: {e}")
            return False