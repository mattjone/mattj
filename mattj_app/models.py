from __future__ import unicode_literals

from django.db import models

class Experience(models.Model):
    exp_type = models.CharField(default = 'professional', max_length = 50, choices = [('education','Education'),('professional','Professional'),('Project','project')])
    start_date = models.DateField(blank = False)
    end_date = models.DateField(null = True)
    employer = models.CharField(max_length = 30)
    position = models.CharField(max_length = 50)
    description = models.CharField(max_length = 1000)
