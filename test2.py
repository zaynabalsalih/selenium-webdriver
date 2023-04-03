import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest():
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_bibliotek_burlov_se(self):
        self.driver.get("https://bibliotek.burlov.se/-/arlovs-bibliotek")

        element = self.driver.find_element(By.LINK_TEXT, "Öppet och kontakt")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        self.driver.find_element(By.CSS_SELECTOR, "#navigation li:nth-child(2) span").click()
        self.driver.execute_script("window.scrollTo(0,160.8000030517578)")

        self.driver.find_element(By.CSS_SELECTOR, ".branch-list-container:nth-child(2) h2").click()
        self.driver.execute_script("window.scrollTo(0,202.39999389648438)")

        self.driver.find_element(By.CSS_SELECTOR, ".no-glutter").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".street:nth-child(1)").text == "Gata\\\\nLommavägen 2"
        self.driver.find_element(By.CSS_SELECTOR, ".street:nth-child(1)").click()

        self.driver.find_element(By.LINK_TEXT, "Språk").click()
        self.driver.find_element(By.CSS_SELECTOR, ".goog-te-combo").click()
        dropdown = self.driver.find_element(By.CSS_SELECTOR, ".goog-te-combo")
        dropdown.find_element(By.XPATH, "//option[. = 'arabiska']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#portlet_com_liferay_site_navigation_language_web_portlet_SiteNavigationLanguagePortlet > .modal__close").click()

        self.driver.find_element(By.ID, "i0-dynamic-cal-wrapper").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".dynamic-cal-header-library-name > font > font").text == "ساعات العمل"

        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) .header-shortcuts-link-icon").click()
        self.driver.find_element(By.CSS_SELECTOR, ".goog-te-combo").click()
        dropdown = self.driver.find_element(By.CSS_SELECTOR, ".goog-te-combo")
        dropdown.find_element(By.XPATH, "//option[. = 'svenska']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#portlet_com_liferay_site_navigation_language_web_portlet_SiteNavigationLanguagePortlet > .modal__close").click()

        self.driver.find_element(By.CSS_SELECTOR, "#navigation li:nth-child(4) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".article-basic-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".article-basic-title").click()
        self.driver.find_element(By.CSS_SELECTOR, ".article-basic-title").click()
        assert self.driver.title == "Barn och unga - Burlöv"
        self.driver.find_element(By.CSS_SELECTOR, ".article-basic-header").click()

        self.driver.find_element(By.CSS_SELECTOR, "#navigation li:nth-child(5) span").click()
        self.driver.find_element(By.CSS_SELECTOR, "#navigation li:nth-child(5) span").click