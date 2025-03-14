from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CareersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sections = {
            "location section": (By.ID, "career-our-location"),
            "Teams section": (By.ID, "career-find-our-calling"),
            "Life at Insider Section": (By.XPATH, "//section[contains(@class, 'elementor-element-a8e7b90')]")
        }

    def is_section_visible(self, section_name):
        if section_name not in self.sections:
            print(f"'{section_name}' bölümü bulunamadı")
            return False

        locator = self.sections[section_name]
        is_visible = self.is_element_visible(locator)

        if is_visible:
            print(f"'{section_name}' başarıyla yüklendi!")
        else:
            print(f"'{section_name}' yüklenemedi!")

        return is_visible