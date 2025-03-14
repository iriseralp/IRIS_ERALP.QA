import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage

class QAPage(BasePage):
    SEE_ALL_JOBS = (By.CSS_SELECTOR, "a.btn-outline-secondary")
    RESULT_COUNTER = (By.ID, "deneme")
    CAREER_POSITION_LIST = (By.ID, "jobs-list")
    LOCATION_DROPDOWN = (By.ID, "select2-filter-by-location-container")
    ISTANBUL_OPTION = (By.XPATH, "//li[normalize-space()='Istanbul, Turkiye']")
    JOB_DROPDOWN = (By.ID, "select2-filter-by-department-container")
    QA_OPTION = (By.XPATH, "//li[normalize-space()='Quality Assurance']")
    JOB_LISTINGS = (By.CSS_SELECTOR, "#jobs-list .position-list-item")
    VIEW_ROLE_BUTTONS = (By.XPATH, "//a[contains(@href, 'jobs.lever.co')]")

    def navigate_qa(self):
        self.find_and_click(self.SEE_ALL_JOBS)
        career_position_element = self.wait.until(EC.visibility_of_element_located(self.CAREER_POSITION_LIST))
        self.driver.execute_script("arguments[0].scrollIntoView();", career_position_element)
        time.sleep(10)
        self.wait.until(EC.visibility_of_element_located(self.RESULT_COUNTER))
        print("Tüm iş ilanları tamamen yüklendi!")

    def filter(self):

        self.find_and_click(self.LOCATION_DROPDOWN)
        time.sleep(10)
        print("Lokasyon dropdown açıldı!")

        self.find_and_click(self.ISTANBUL_OPTION)
        time.sleep(10)
        print("İstanbul seçildi!")

        self.find_and_click(self.JOB_DROPDOWN)

        self.find_and_click(self.QA_OPTION)
        time.sleep(10)
        print("'Quality Assurance' departmanı seçildi!")

    def get_job_listings(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.JOB_LISTINGS))

    def click_view_button(self):

        try:
            view_buttons = self.wait.until(EC.presence_of_all_elements_located(self.VIEW_ROLE_BUTTONS))
            if len(view_buttons) > 0:
                view_buttons[0].click()
                print("'View Role' butonuna başarıyla tıklandı.")
            else:
                raise Exception("'View Role' butonları bulunamadı!")
        except Exception as e:
            print("HATA: 'View Role' butonuna tıklanamadı! {e}")


    def switch_to_lever_page(self):
        main_window = self.driver.current_window_handle
        self.wait.until(EC.number_of_windows_to_be(2))
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                break
        print("Yeni sekmeye geçildi ve Lever sayfası açıldı!")
