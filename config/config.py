import allure

def attach_text(name, text):
    """Attach plain text logs to Allure report."""
    allure.attach(text, name=name, attachment_type=allure.attachment_type.TEXT)

def attach_screenshot(driver, name="Screenshot"):
    """Capture and attach a screenshot to Allure report."""
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

def attach_page_source(driver, name="Page Source"):
    """Capture and attach HTML source of the page to Allure report."""
    allure.attach(driver.page_source, name=name, attachment_type=allure.attachment_type.HTML)
