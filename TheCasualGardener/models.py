from django.db import models

VEGETABLE_CHOICES = {
    ('Leafy Vegetable Mix','Leafy Vegetable Mix'),
    ('Multi Tomato Mix','Multi Tomato Mix'),
    ('Cucumber Eggplant Squash Mix','Cucumber Eggplant Squash Mix'),
    ('Eggplant','Eggplant'),
    ('Lettuce','Lettuce'),
    ('Cucumber','Cucumber'),
    ('Cherry Tomato','Cherry Tomato'),
}
SUBSCRIPTION_CHOICES = {
    ('Weekly','Weekly'),
    ('Bi-Weekly','Bi-Weekly'),
    ('Monthly','Monthly'),
    ('Semi-Annual','Semi-Annual'),
}

class Basket(models.Model):
    first_name = models.CharField(max_length=60, default="", blank=True, null=False)
    last_name = models.CharField(max_length=60, default="", blank=True, null=False)
    e_mail = models.CharField(max_length=90, default="", blank=True, null=False)
    subscription = models.CharField(max_length=60, null=True, choices=SUBSCRIPTION_CHOICES)
    vegetable = models.CharField(max_length=60, null=True, choices=VEGETABLE_CHOICES)
    # optional description of basket's ingredients
    description = models.TextField(max_length=255, default="ERASE this section - Enter your comments here, we will contact you about current selections and pricing shortly! Thank you! - ERASE this section", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.first_name

