import pytest
from Pages.job_page import JobPage
from utils.logger import logger

@pytest.mark.usefixtures("init", "login")
class TestJob:

    def test_create_job(self):
        job_page = JobPage(self.driver)

        checklist_name = "Automated checklist by JoneS"
        title = "RE Hunter quarterly service"
        tags = ["bike", "service"]
        description = "This is the report of quarterly service of your 2-wheeler"
        scheduled_date = "292025"
        cutoff_date = "11122025"
        assignee = "Jones Leo"
        supervisor = "Prod JoneS"

        job_page.create_job(
            checklist_name=checklist_name,
            title=title,
            tags=tags,
            description=description,
            scheduled_date=scheduled_date,
            cutoff_date=cutoff_date,
            assignee=assignee,
            supervisor=supervisor,
        )

        job_name = job_page.get_created_job_title()
        logger.info("Job created: %s", job_name)
        assert title in job_name
