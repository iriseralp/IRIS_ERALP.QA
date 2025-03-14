import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.CareersPage import CareersPage
from pages.HomePage import HomePage
from pages.LeverPage import LeverPage
from pages.QAPage import QAPage

def test_insider_careers():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)

    home_page = HomePage(driver)
    careers_page = CareersPage(driver)
    qa_page = QAPage(driver)
    lever_page = LeverPage(driver)

    driver.get("https://useinsider.com/")
    home_page.navigate_careers()


    sections_to_test = ["location section", "Teams section", "Life at Insider Section"]
    for section in sections_to_test:
        is_visible = careers_page.is_section_visible(section)
        assert careers_page.is_section_visible(section), f" HATA: '{section}' yüklenemedi!"
    print(" Tüm bölümler başarıyla test edildi!")

    driver.get("https://useinsider.com/careers/quality-assurance/")
    qa_page.navigate_qa()
    qa_page.filter()

    job_listings = qa_page.get_job_listings()
    print(f"🔍 {len(job_listings)} adet iş ilanı bulundu.")

    for job in job_listings:
        position_text = job.find_element(By.CSS_SELECTOR, ".position-title").text
        department_text = job.find_element(By.CSS_SELECTOR, ".position-department").text
        location_text = job.find_element(By.CSS_SELECTOR, ".position-location").text

        assert "Quality Assurance" in position_text or "QA" in position_text, f" Pozisyon hatalı: {position_text}"
        assert "Quality Assurance" in department_text, f" Departman hatalı: {department_text}"
        assert "Istanbul, Turkiye" in location_text, f" Lokasyon hatalı: {location_text}"

    qa_page.click_view_button()
    qa_page.switch_to_lever_page()
    lever_page.validate_lever_page()
    lever_page.validate_lever_data()

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.quit()

    print(" Test başarıyla tamamlandı!")


if __name__ == "__main__":
    test_insider_careers()
