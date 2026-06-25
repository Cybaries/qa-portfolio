from django.db import models


class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, default='Present')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} @ {self.company}"


class ExperienceBullet(models.Model):
    experience = models.ForeignKey(Experience, related_name='bullets', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)   # e.g. "Framework Engineering"
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']


class Project(models.Model):
    SEVERITY_CHOICES = [
        ('critical', 'Critical'),
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    tech_stack = models.CharField(max_length=300)
    date_range = models.CharField(max_length=100, blank=True)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='high')
    github_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class ProjectBullet(models.Model):
    project = models.ForeignKey(Project, related_name='bullets', on_delete=models.CASCADE)
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']


class Skill(models.Model):
    STAGE_CHOICES = [
        ('plan', 'Plan'),
        ('code', 'Code'),
        ('build', 'Build'),
        ('test', 'Test'),
        ('release', 'Release'),
        ('monitor', 'Monitor'),
    ]
    name = models.CharField(max_length=100)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['stage', 'order']
