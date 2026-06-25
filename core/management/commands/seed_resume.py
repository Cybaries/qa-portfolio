from django.core.management.base import BaseCommand
from core.models import Experience, ExperienceBullet, Project, ProjectBullet, Skill


class Command(BaseCommand):
    help = "Seed QA portfolio with resume content"

    def handle(self, *args, **options):
        Experience.objects.all().delete()
        Project.objects.all().delete()
        Skill.objects.all().delete()

        # ── Experience ──
        tcs = Experience.objects.create(
            company="Tata Consultancy Services",
            role="Selenium Tester | Tata Steel Netherlands Project",
            location="Pune, India",
            start_date="May 2024",
            end_date="Present",
            order=1,
        )
        ExperienceBullet.objects.bulk_create([
            ExperienceBullet(experience=tcs, label="Framework Eng.", text="Engineered a scalable automated validation framework using Python and Selenium to systematically verify the structural migration of 100+ legacy Mainframe modules to distributed microservices, securing 100% functional parity and zero regressions.", order=1),
            ExperienceBullet(experience=tcs, label="API Validation", text="Designed, developed, and executed modular automated API test suites using Python and Postman to validate backend REST workflows; integrated automated database verification via SQL queries, cutting manual validation cycle times by 15%.", order=2),
            ExperienceBullet(experience=tcs, label="RCA", text="Performed methodical root cause analysis, environment debugging, and isolation for 30+ complex production infrastructure issues, systematically enhancing overall application reliability.", order=3),
            ExperienceBullet(experience=tcs, label="Agile", text="Partnered within fast-paced Agile sprint cycles alongside 12+ cross-functional squads to capture defects, reproduce edge cases, and ensure stable, low-latency releases.", order=4),
            ExperienceBullet(experience=tcs, label="Leadership", text="Selected for the TCS Spot Performer Award (2025) after successfully mentoring 2 junior engineers, standardizing automation practices to accelerate onboarding and team output.", order=5),
        ])

        # ── Projects ──
        mail = Project.objects.create(
            title="AI-Powered Smart Mail Client",
            slug="ai-smart-mail-client",
            tech_stack="Django, React, REST APIs, Google Pub/Sub",
            date_range="Feb 2025 – Feb 2026",
            severity="high",
            order=1,
        )
        ProjectBullet.objects.bulk_create([
            ProjectBullet(project=mail, text="Architected backend services using Django REST Framework, enabling modular and scalable API design for simulating real-time inbox management with 5 APIs.", order=1),
            ProjectBullet(project=mail, text="Tested API workflows and validated backend responses to ensure reliable synchronization and data consistency.", order=2),
            ProjectBullet(project=mail, text="Created event-driven architecture using Google Pub/Sub and Webhooks, facilitating near real-time email synchronization and 25% reduction in synchronization latency.", order=3),
            ProjectBullet(project=mail, text="Optimized query execution and filtering logic, resulting in a 25% decrease in latency and a 15% increase in throughput.", order=4),
        ])

        wa = Project.objects.create(
            title="WhatsApp Automation Bot",
            slug="whatsapp-automation-bot",
            tech_stack="Node.js, Express, MongoDB, PyTest, Selenium",
            date_range="Jun 2025 – Aug 2025",
            severity="critical",
            github_url="https://github.com/Cybaries/whatsapp-bot",
            order=2,
        )
        ProjectBullet.objects.bulk_create([
            ProjectBullet(project=wa, text="Built a robust integration and component testing suite using PyTest & Selenium to simulate 50+ concurrent multi-user interactions and edge-case network conditions.", order=1),
            ProjectBullet(project=wa, text="Designed a modular command handling framework with Role-Based Access Control (RBAC) for secure multi-user interactions.", order=2),
            ProjectBullet(project=wa, text="Performed automated testing and debugging to improve fault tolerance and reduce downtime by 40%.", order=3),
        ])

        iot = Project.objects.create(
            title="Alcohol & Overspeeding Detector",
            slug="iot-alcohol-overspeeding-detector",
            tech_stack="Arduino, Embedded C, GPS, GSM",
            date_range="Dec 2022 – Jan 2023",
            severity="medium",
            order=3,
        )
        ProjectBullet.objects.bulk_create([
            ProjectBullet(project=iot, text="Engineered an IoT-based safety system integrating 5+ sensors and GPS for real-time vehicle monitoring.", order=1),
            ProjectBullet(project=iot, text="Implemented interrupt-driven embedded logic and GSM-based alert system, transmitting violation data within 5 seconds.", order=2),
            ProjectBullet(project=iot, text="Achieved 95% detection accuracy in simulated driving environments through sensor calibration and testing.", order=3),
        ])

        # ── Skills by CI/CD stage ──
        skills = [
            # plan
            ("Agile/Scrum", "plan"), ("Jira", "plan"), ("Test Planning", "plan"), ("System Design", "plan"),
            # code
            ("Python", "code"), ("Java", "code"), ("JavaScript", "code"), ("SQL / PL/SQL", "code"), ("Embedded C", "code"),
            # build
            ("Docker", "build"), ("GitHub Actions", "build"), ("Jenkins", "build"), ("Databricks", "build"),
            # test
            ("Selenium", "test"), ("PyTest", "test"), ("Playwright", "test"), ("TestNG", "test"),
            ("Postman", "test"), ("REST Assured", "test"), ("Appium", "test"), ("API Testing", "test"),
            # release
            ("Git / GitHub", "release"), ("CI/CD Pipelines", "release"), ("Linux Debugging", "release"),
            # monitor
            ("Google Pub/Sub", "monitor"), ("MongoDB", "monitor"), ("MySQL", "monitor"),
            ("Root Cause Analysis", "monitor"), ("Distributed Systems", "monitor"),
        ]
        Skill.objects.bulk_create([
            Skill(name=name, stage=stage, order=i) for i, (name, stage) in enumerate(skills)
        ])

        self.stdout.write(self.style.SUCCESS("QA portfolio seeded successfully."))
