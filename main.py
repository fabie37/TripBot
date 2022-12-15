from Drivers import SkyScanner
import undetected_chromedriver as uc
import selenium.webdriver as webdriver
import datetime
from selenium_stealth import stealth
# Setup
# opts = uc.ChromeOptions()
# opts.add_argument("--window-size=1280,720")
# driver = uc.Chrome(options=opts, use_subprocess=True)

# driver = webdriver.Firefox()

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(
    driver,
    user_agent='Dalvik/2.1.0 (Linux; U; Android 8.1.0; MI 8 MIUI/8.8.24)',
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=False,
    run_on_insecure_origins=False,
)


skyscanner = SkyScanner(driver)
flightQuery = {
    "from": "Ediburgh (EDI)",
    "to": "Split (SPU)",
    "depart": "01/01/2023",
    "return": "27/02/2023",
    "direct": True,
    "class": "Economy",
    "adults": 3,
    "children": 0
}
skyscanner.openSite()
# skyscanner.getFlights(flightQuery)
