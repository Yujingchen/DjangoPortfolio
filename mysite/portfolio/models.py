from django.db import models

# Create your models here.
class Skill(models.Model):
    skill_text = models.CharField(max_length=200)
    def __str__(self):
        return self.skill_text