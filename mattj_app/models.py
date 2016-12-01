from __future__ import unicode_literals

from django.db import models

class Experience(models.Model):
    exp_type = models.CharField(default = 'professional', max_length = 30, choices = [('education','Education'),('professional','Professional'),('Project','project')])
    start_date = models.DateField(blank = False)
    end_date = models.DateField(blank = True, null = True)
    employer = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)

    def __str__(self):
        return "%s: %s" % (self.employer, self.position)
