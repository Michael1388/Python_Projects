from django.db import models


PREFIX_CHOICES = {
    ('Mr.','Mr.'),
    ('Mrs.','Mrs.'),
    ('Ms.','Ms'),
}

class Profile(models.Model):
    prefix = models.CharField(max_length=60, null=True, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=60, default="", blank=True, null=False)
    last_name = models.CharField(max_length=60, default="", blank=True, null=False)
    e_mail = models.CharField(max_length=90, default="", blank=True, null=False)
    username = models.CharField(max_length=90, default="", blank=True, null=False)


    objects = models.Manager()

    def __str__(self):
        return self.first_name
