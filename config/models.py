from django.db import models

# Create your models here.

#################
# Configuration #
#################

class Config(models.Model):
    config_var = models.CharField(max_length=16, default='did_init')
    config_val = models.CharField(max_length=2048, default='no')
    def __str__(self):
        return self.config_var


