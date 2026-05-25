import time


class BasePage:
    def __init__(self, page):
        self.page = page

    def take_screenshot(self, step_name,retries=3):
        timestamp = int(time.time() * 1000)
        self.page.save_screenshot(f"screenshot_{step_name}_{timestamp}.png")

    def navigate(self, url):
        self.page.goto(url)
        self.take_screenshot()

    def click(self, locator,retries=3):
        for attempts in range(retries):
            try:
                self.page.locator(locator).click()
                break
            except Exception as e:
                if attempts < retries - 1:
                    print(f"Click failed on attempt {attempts + 1}. Retrying...")
                else:
                    print(f"Click failed after {retries} attempts.")
                    raise e

    def fill(self, locator, text,retries=3):
        for attempts in range(retries):
            try:
                self.page.locator(locator).fill(text)
                break
            except Exception as e:
                if attempts < retries - 1:
                    print(f"Fill failed on attempt {attempts + 1}. Retrying...")
                else:
                    print(f"Fill failed after {retries} attempts.")
                    raise e

    def get_text(self, locator,retries=3):
        for attempts in range(retries):
            try:
                return self.page.locator(locator).text_content()
            except Exception as e:
                if attempts < retries - 1:
                    print(f"Get text failed on attempt {attempts + 1}. Retrying...")
                else:
                    print(f"Get text failed after {retries} attempts.")
                    raise e
        return None

    def is_visible(self, locator,retries=3):
        for attempts in range(retries):
            try:
                return self.page.locator(locator).is_displayed()
            except Exception as e:
                if attempts < retries - 1:
                    print(f"Get text failed on attempt {attempts + 1}. Retrying...")
                else:
                    print(f"Get text failed after {retries} attempts.")
                    raise e
        return None

    def wait_for_element(self, locator):
        self.page.locator(locator).wait_for()

    def get_title(self,retries=3):
        for attempts in range(retries):
            try:
                return self.page.title()
            except Exception as e:
                if attempts < retries - 1:
                    print(f"Get title failed on attempt {attempts + 1}. Retrying...")
                else:
                    print(f"Get title failed after {retries} attempts.")
                    raise e
        return None