from django.db import models
from django.contrib import admin
from django.shortcuts import get_object_or_404


class Brief(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.TextField()
    phone = models.TextField()
    company = models.TextField()
    contactName = models.TextField()
    projectName = models.TextField()
    description = models.TextField()
    goals = models.TextField()
    price = models.IntegerField()
    projectLength = models.IntegerField()
    criteria = models.TextField()
    timeframe = models.TextField()
    target = models.TextField()
    technologies = models.TextField()
    mockup = models.TextField()
    comments = models.TextField()

    def __str__(self):
        return f"{self.id} {self.contactName} {self.email}"


def create(
        email,
        phone,
        company,
        contactName,
        projectName,
        description,
        goals,
        price,
        projectLength,
        criteria,
        timeframe,
        target,
        technologies,
        mockup,
        comments):
    br = Brief()
    br.email = email
    br.phone = phone
    br.company = company
    br.contactName = contactName
    br.projectName = projectName
    br.description = description
    br.goals = goals
    br.price = price
    br.projectLength = projectLength
    br.criteria = criteria
    br.timeframe = timeframe
    br.target = target
    br.technologies = technologies
    br.mockup = mockup
    br.comments = comments
    br.save()
    return [br.contactName, br.company]