from django.db import models

class Aspect(models.Model):
    description = models.CharField(max_length=128)
    free_invoke = models.BooleanField(default=False)

    def __str__(self):
        return self.description
