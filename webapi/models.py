from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True)
    tags = ArrayField(
        models.CharField(max_length=10, blank=True),
        size=8,
    )
    pictures = ArrayField(
        models.CharField(max_length=10, blank=True),
        size=8,
    )

    def __str__(self):
        return '%s (%s)' % (self.id, self.title)

class Experience(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    job_title = models.CharField(max_length=100, unique=True, db_index=True)
    company = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.job_title, self.company)

class Education(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    school = models.CharField(max_length=100, unique=True, db_index=True)
    major = models.CharField(max_length=100, unique=True, db_index=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.school, self.major)
