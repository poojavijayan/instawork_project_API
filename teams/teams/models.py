from django.db import models


# Model class for team members details
class TeamMembers(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    role = models.CharField(max_length=10)
