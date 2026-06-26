from django.core.management.base import BaseCommand
from core.models import Experience, ExperienceBullet, Project, ProjectBullet, Skill


class Command(BaseCommand):
    help = "Seed QA portfolio with resume content"

    def handle(self, *args, **options):
        # Delete children before parents to avoid FK/reference issues on
        # both SQLite and MongoDB backends.
        self.stdout.write("Clearing existing data...")
        ExperienceBullet.objects.all().delete()
        ProjectBullet.objects.all().delete()
        Experience.objects.all().delete()
        Project.objects.all().delete()
        Skill.objects.all().delete()

        # ── Experience ──────────────────────────────────────────────────────
        self.stdout.write("Seeding experience...")
        tcs = Experience.objects.create(
            company="Tata Consultancy Services",
            role="Selenium Tester | Tata Steel Netherlands Project",
            location="Pune, India",
            start_date="May 2024",
            end_date="Present",
            order=1,
        )
        ExperienceBullet.objects.bulk_create([
            ExperienceBullet(
                experience=tcs, label="Framework Eng.", order=1,
                text="Engineered a scalable automated validation framework using Python and Selenium "
                     "to systematically verify the structural migration of 100+ legacy Mainframe modules "
                     "to distributed microservices, securing 100% functional parity and zero regressions.",
            ),
            ExperienceBullet(
                experience=tcs, label="API Validation", order=2,
                text="Designed, developed, and executed modular automated API test suites using Python "
                     "and Postman to validate backend REST workflows; integrated automated database "
                     "verification via SQL queries, cutting manual validation cycle times by 15%.",
            ),
            ExperienceBullet(
                experience=tcs, label="RCA", order=3,
                text="Performed methodical root cause analysis, environment debugging, and isolation "
                     "for 30+ complex production infrastructure issues, systematically enhancing "
                     "overall application reliability.",
            ),
            ExperienceBullet(
                experience=tcs, label="Agile", order=4,
                text="Partnered within fast-paced Agile sprint cycles alongside 12+ cross-functional "
                     "squads to capture defects, reproduce edge cases, and ensure stable, "
                     "low-latency releases.",
            ),
            ExperienceBullet(
                experience=tcs, label="Leadership", order=5,
                text="Selected for the TCS Spot Performer Award (2025) after successfully mentoring "
                     "2 junior engineers, standardizing automation practices to accelerate onboarding "
                     "and team output.",
            ),
        ])

        # ── Projects ─────────────────────────────────────────────────────────
        self.stdout.write("Seeding projects...")
        mail = Project.objects.create(
            title="AI-Powered Smart Mail Client",
            slug="ai-smart-mail-client",
            tech_stack="Django, React, REST APIs, Google Pub/Sub",
            date_range="Feb 2025 – Feb 2026",
            severity="high",
            order=1,
        )
        ProjectBullet.objects.bulk_create([
            ProjectBullet(project=mail, order=1,
                text="Architected backend services using Django REST Framework, enabling modular and "
                     "scalable API design for simulating real-time inbox management with 5 APIs."),
            ProjectBullet(project=mail, order=2,
                text="Tested API workflows and validated backend responses to ensure reliable "
                     "synchronization and data consistency."),
            ProjectBullet(project=mail, order=3,
                text="Created event-driven architecture using Google Pub/Sub and Webhooks, "
                     "facilitating near real-time email synchronization and 25% reduction in "
                     "synchronization latency."),
            ProjectBullet(project=mail, order=4,
                text="Optimized query execution and filtering logic, resulting in a 25% decrease "
                     "in latency and a 15% increase in throughput."),
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
            ProjectBullet(project=wa, order=1,
                text="Built a robust integration and component testing suite using PyTest & Selenium "
                     "to simulate 50+ concurrent multi-user interactions and edge-case network conditions."),
            ProjectBullet(project=wa, order=2,
                text="Designed a modular command handling framework with Role-Based Access Control "
                     "(RBAC) for secure multi-user interactions."),
            ProjectBullet(project=wa, order=3,
                text="Performed automated testing and debugging to improve fault tolerance and "
                     "reduce downtime by 40%."),
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
            ProjectBullet(project=iot, order=1,
                text="Engineered an IoT-based safety system integrating 5+ sensors and GPS for "
                     "real-time vehicle monitoring."),
            ProjectBullet(project=iot, order=2,
                text="Implemented interrupt-driven embedded logic and GSM-based alert system, "
                     "transmitting violation data within 5 seconds."),
            ProjectBullet(project=iot, order=3,
                text="Achieved 95% detection accuracy in simulated driving environments through "
                     "sensor calibration and testing."),
        ])

        # ── Skills by CI/CD stage ────────────────────────────────────────────
        self.stdout.write("Seeding skills...")
        skills = [
            ("Agile/Scrum", "plan"), ("Jira", "plan"),
            ("Test Planning", "plan"), ("System Design", "plan"),
            ("Python", "code"), ("Java", "code"),
            ("JavaScript", "code"), ("SQL / PL/SQL", "code"), ("Embedded C", "code"),
            ("Docker", "build"), ("GitHub Actions", "build"),
            ("Jenkins", "build"), ("Databricks", "build"),
            ("Selenium", "test"), ("PyTest", "test"), ("Playwright", "test"),
            ("TestNG", "test"), ("Postman", "test"), ("REST Assured", "test"),
            ("Appium", "test"), ("API Testing", "test"),
            ("Git / GitHub", "release"), ("CI/CD Pipelines", "release"),
            ("Linux Debugging", "release"),
            ("Google Pub/Sub", "monitor"), ("MongoDB", "monitor"),
            ("MySQL", "monitor"), ("Root Cause Analysis", "monitor"),
            ("Distributed Systems", "monitor"),
        ]
        Skill.objects.bulk_create([
            Skill(name=name, stage=stage, order=i)
            for i, (name, stage) in enumerate(skills)
        ])

        self.stdout.write(self.style.SUCCESS("QA portfolio seeded successfully."))
