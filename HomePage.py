from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.Company_Menu = (By.XPATH, "//a[contains(text(), 'Company')]")
        self.Careers_Click = (By.XPATH, "//a[contains(text(), 'Careers')]")

    def navigate_careers(self):
        if self.find_and_click(self.Company_Menu):
            print("Company menüsü bulundu ve tıklandı")
        else:
            print("Company menüsü tıklanamadı")
            return

        self.wait.until(EC.element_to_be_clickable(self.Careers_Click)).click()
        print("Company menüsü içinden Careers bulundu ve tıklandı")