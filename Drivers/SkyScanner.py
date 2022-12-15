
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from datetime import datetime


class SkyScanner:

    def __init__(self, driver):
        self.driver = driver
        self.queryMap = {
            "direct": lambda toClick: self.inputClick("//input[@name='directOnly']", By.XPATH, toClick),
            "from": lambda data: self.inputData("fsc-origin-search", By.NAME, data),
            "to": lambda data: self.inputData("fsc-destination-search", By.NAME, data),
            "depart": lambda date: self.selectDate("depart-fsc-datepicker-button", By.ID, date),
            "return": lambda date: self.selectDate("return-fsc-datepicker-button", By.ID, date),
            # "class": lambda cls: self.selectClass("class-travellers-trigger", By.name, cls),
            # "adults": lambda adults: self.selectAdults(adults),
            # "children": lambda children: self.selectChildren(children)
        }

    def inputData(self, id, by, data):
        inputSelector = self.driver.find_element(by, id)
        inputSelector.send_keys(data)
        sleep(3)

    def inputClick(self, id, by, toClick):
        inputSelector = self.driver.find_element(by, id)
        clicked = inputSelector.get_property('checked')
        if (not clicked and toClick):
            inputSelector.click()
        clicked = inputSelector.get_property('checked')
        sleep(3)

    def selectDate(self, id, by, date):
        # Get the date button
        dateButton = self.driver.find_element(by, id)
        dateButton.click()
        sleep(1)

        # Set the month/year
        pythonDate = datetime.strptime(date, "%d/%m/%Y")
        monthYear = pythonDate.strftime('%B %Y')
        dropDown = Select(self.driver.find_element(By.NAME, 'months'))
        sleep(2)
        dropDown.select_by_visible_text(monthYear)
        sleep(1)

        # Set the day
        dayLabel = pythonDate.strftime("%A, %d %B %Y")
        day = pythonDate.strftime('%d')

        if (int(day) < 10):
            dayLabel = dayLabel.replace('0', '', 1)
        print(dayLabel)
        dayButton = self.driver.find_element(
            By.XPATH, f"//tbody/tr/td/button[@aria-label='{dayLabel}']")
        dayButton.click()
        sleep(3)

    def openSite(self):
        self.driver.get("https://www.skyscanner.net/")
        assert "Skyscanner" in self.driver.title
        try:
            cookieButton = self.driver.find_element(
                By.ID, "acceptCookieButton")
            cookieButton.click()
        except Exception as e:
            pass
        sleep(5)

    def getFlights(self, query):

        # 1. Open Skyscanner
        self.openSite()

        # 2. Execute each key value
        for key, val in query.items():
            if key in self.queryMap:
                self.queryMap[key](val)
