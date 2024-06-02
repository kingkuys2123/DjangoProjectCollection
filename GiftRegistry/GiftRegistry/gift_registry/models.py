from django.db import models


class Gift(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.name
