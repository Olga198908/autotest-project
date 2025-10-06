from locust import HttpUser, TaskSet, task, between
import random

#locust -f locust_orangehrm.py

class OrangeHRMUser(HttpUser):
    host = "https://opensource-demo.orangehrmlive.com"
    wait_time = between(2, 5)

    @task(5)
    def public_actions(self):
        pages = [
            "/web/index.php/auth/login",
            "/web/index.php/auth/requestPasswordResetCode",
            "/web/index.php/auth/sendPasswordReset",
            "/web/index.php/recruitment/viewJobs"
        ]
        self.client.get(random.choice(pages))

    @task(3)
    def try_login(self):
        self.client.post("/web/index.php/auth/validate", data={
            "username": "Admin",
            "password": "admin123"
        })

    @task(2)
    def browse_sections(self):
        sections = [
            "/web/index.php/dashboard/index",
            "/web/index.php/pim/viewEmployeeList",
            "/web/index.php/recruitment/viewCandidates",
            "/web/index.php/admin/viewSystemUsers",
            "/web/index.php/buzz/viewBuzz"
        ]
        for section in random.sample(sections, 2):
            self.client.get(section)