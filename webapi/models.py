from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True)
    role = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    github_link = models.CharField(max_length=100, blank=True)
    live_link = models.CharField(max_length=100, blank=True)
    tags = ArrayField(
        models.CharField(max_length=100, blank=True),
        size=8,
    )
    pictures = ArrayField(
        models.CharField(max_length=100, blank=True),
        size=8,
    )

    def __str__(self):
        return '%s (%s)' % (self.id, self.title)

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=100, blank=True)
    start_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.job_title, self.company)

class Education(models.Model):
    school = models.CharField(max_length=100, unique=True, db_index=True)
    major = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True)
    start_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.school, self.major)
