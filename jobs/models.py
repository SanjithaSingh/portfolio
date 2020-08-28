from django.db import models

# Create your models here.

class Stack(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Job(models.Model):
    image=models.ImageField(upload_to='images/')
    company=models.CharField(max_length=100)
    role=models.CharField(max_length=30)
    project=models.CharField(max_length=200)
    stack = models.ManyToManyField(Stack)
    description=models.TextField()
    contributions=models.TextField()
    startDate=models.DateField()
    endDate=models.DateField()
    def __str__(self):
        return self.company
    def contributions_as_list(self):
        return self.contributions.split('\n')

class Project(models.Model):
    title=models.CharField(max_length=100)
    summary=models.CharField(max_length=200)
    description=models.TextField()
    githubURL=models.URLField()
    liveURL=models.URLField(default=None)
    stack = models.ManyToManyField(Stack)

    def __str__(self):
        return self.title