import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage

class LeverPage(BasePage):
    POSITION_TITLE = (By.CSS_SELECTOR, ".posting-headline h2")
    LOCATION = (By.CSS_SELECTOR, ".posting-categories .location")
    DEPARTMENT = (By.CSS_SELECTOR, ".posting-categories .department")

    def validate_lever_page(self):
        self.wait.until(EC.url_contains("jobs.lever.co/useinsider/"))
        print("Lever Application sayfasına yönlendirildi!")

    def get_position_title(self):
        time.sleep(3)
        return self.wait.until(EC.presence_of_element_located(self.POSITION_TITLE)).text

    def get_location(self):
        time.sleep(3)
        return self.wait.until(EC.presence_of_element_located(self.LOCATION)).text

    def get_department(self):
        time.sleep(3)
        return self.wait.until(EC.presence_of_element_located(self.DEPARTMENT)).text

    def validate_lever_data(self):

        position_title = self.get_position_title()
        location = self.get_location()
        department = self.get_department()

        assert "Quality Assurance" in position_title or "QA" in position_title, f" Pozisyon hatalı: {position_title}"
        assert "Istanbul, Turkiye" in location, f" Lokasyon hatalı: {location}"
        assert "Quality Assurance" in department, f" Departman hatalı: {department}"

        print(" Lever sayfasındaki bilgiler doğru!")
