from django.db import models

# Create your models here.
# Creates model of University Classes
class UniversityCampus(models.Model): #create class
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False) # create database field
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)


    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.campus_name}: {0.state}' # define how object will be displayed in the browser
        return display_campus.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"
