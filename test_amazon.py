import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Replace with your LambdaTest credentials
USERNAME = "kashiramkamonica66"
ACCESS_KEY = "oHDSeBaQG0ay3aOQLE8hBmuzT5OWqXFwjZYwM6PJXEZBiwIhJc"

# Define capabilities fixture
@pytest.fixture(scope="function")
def capabilities(request):
    caps = {
        "build": "AmazonSearchTest",
        "name": request.node.name,
        "platform": "Windows 10",
        "browserName": "chrome",  # You can change this to "firefox" or other supported browsers
        "version": "latest",
        "selenium_version": "3.141.59",
        "visual": True,
        "network": True,
        "video": True,
        "console": True,
        "tunnel": False,
    }
    return caps

# Define driver fixture
@pytest.fixture(scope="function")
def driver(request, capabilities):
    browser = capabilities['browserName']

    if browser.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(
            command_executor="https://kashiramkamonica66:oHDSeBaQG0ay3aOQLE8hBmuzT5OWqXFwjZYwM6PJXEZBiwIhJc@hub.lambdatest.com/wd/hub",
            options=options,
        )
    elif browser.lower() == 'firefox':
        options = webdriver.FirefoxOptions()
        driver = webdriver.Remote(
            command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.lambdatest.com/wd/hub",
            options=options,
        )
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver

# Test case
def test_amazon_search(driver):
    driver.get("https://www.amazon.com")
    assert "Amazon.com" in driver.title

    search_box = driver.find_element("id", "twotabsearchtextbox")
    search_box.send_keys("iphone13")
    search_box.send_keys(Keys.RETURN)

    price_element = driver.find_element("xpath", "//span[@class='a-price']//span[@class='a-offscreen']")
    price = price_element.text

    print(f"Price: {price}")

if __name__ == "__main__":
    pytest.main(["-v", "test_amazon.py"])
