from logging import Logger

from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.decorators import logger, log_decorator
from utils.test_data_reader import get_login_data


class ElementsPage(BasePage):
    logger = Logger("ElementsPage")

    def __init__(self,page):
        super().__init__(page)

    WEB_TABLES_LINK = "role=link[name='Web Tables']"
    ADD_BUTTON = "#addNewRecordButton"
    FIRST_NAME_FIELD = "#firstName"
    LAST_NAME_FIELD = "#lastName"
    EMAIL_FIELD = "#userEmail"
    AGE_FIELD = "#age"
    SALARY_FIELD = "#salary"
    DEPARTMENT_FIELD = "#department"
    SUBMIT_BUTTON = "#submit"
    SEARCH_BOX = "#searchBox"

    @log_decorator
    def navigate_to_add_web_tables_dialog(self):
        self.click(self.WEB_TABLES_LINK)
        self.click(self.ADD_BUTTON)

    @log_decorator
    def enter_web_table_add_details(self,user_details: dict):
        self.page.get_by_role("dialog").wait_for(state="visible")
        self.fill(self.FIRST_NAME_FIELD,user_details['first_name'])
        self.fill(self.LAST_NAME_FIELD,user_details['last_name'])
        self.fill(self.EMAIL_FIELD,user_details['email'])
        self.fill(self.AGE_FIELD,user_details['age'])
        self.fill(self.SALARY_FIELD,user_details['salary'])
        self.fill(self.DEPARTMENT_FIELD,user_details['department'])
        self.click(self.SUBMIT_BUTTON)


    @log_decorator
    def validate_web_table_addition(self):
        pass

    def get_web_table_records(self):
        table = self.page.locator(".rt-table")
        # Get headers
        headers = [ header.inner_text().strip() for header in table.locator("thead th").all() ]
        records = []
        # Get all rows
        rows = table.locator("tbody tr").all()
        for row in rows:
            cells = [ cell.inner_text().strip() for cell in row.locator("td").all() ]
            # Skip empty rows
            if any(cells):
                record = dict(zip(headers, cells))
                records.append(record)
        return records

    def validate_web_table_record_addition(self, user_details: dict):
        email = user_details['email']
        self.fill(self.SEARCH_BOX, email)
        email_cell = self.page.get_by_role("cell", name=email)
        expect(email_cell).to_have_text(email)
        return email_cell.is_visible()

    def validate_web_table_record_addition_2(self,user_details: dict):
        self.validate_web_table_record_addition(user_details['email'])
        records = self.get_web_table_records()
        for record in records:
            if record.get("Email") == user_details['email']:
                return True
        return False













