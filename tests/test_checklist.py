import pytest
from Pages.checklist_page import ChecklistPage
from utils.logger import logger



@pytest.mark.usefixtures("init", "login")
class TestChecklist():
    def test_create_checklist(self):
        checklist_page = ChecklistPage(self.driver)
        title = "Automated Checklist - August 22"
        tag = "automation"
        description = "Checklist created via Pytest + Selenium"
        question = "Which programming language do you prefer?"
        option1 = "Python"
        option2 = "Java"

        checklist_page.create_checklist(title, tag, description, question, option1, option2)
        created_title = checklist_page.get_checklist_title()
        logger.info(f"Checklist created: {created_title}")

        assert created_title == title, "Checklist title does not match"
