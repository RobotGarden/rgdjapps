from django.db import models

class RGUser(models.Model):
    "Table for storing information about Robot Garden members"
    name = models.CharField(max_length=256,
                            verbose_name="Member's full name")
    key_card = models.CharField(max_length=128, blank=True
                                verbose_name="Key card ID number"
                                help_text="Enter without dashes")
    cobot_id = models.CharField(max_length=128, blank=True,
                                verbose_name="Member's ID in the cobot system")
    primary_user = models.ForeignKey('self', blank=True, null=True,
                                     verbose_name="Family primary membership",
                                     help_text="ID of primary user for family memberships")
    created = models.DateTimeField(auto_now_add=True, editable=False,
                                   verbose_name="User entry created time stamp")
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name="User entry updated time stamp")
    email = models.EmailField(verbose_name="Member's contact email address")
    address = models.TextField(blank=True, null=True,
                               verbose_name="Member's mailing address",
                               help_text="(Optional) Street address (or P.O. Box), city and state")
    zip_code = models.CharField(max_length=10,
                                verbose_name="Mailing / home address zip code",
                                help_text="Required")
    emergency_contact = models.TextField(verbose_name="Emergency contact information",
                                         help_text="At minimum the name and mobile phone number of one person we can contact in the event of an emergency.")
    emergency_care = models.TextField(blank=True, null=True,
                                      verbose_name="Emergency care information for first responders",
                                      help_text="Please list any special emergency care instructions (medical conditions, etc.) to provide first responders in the event of an emergency.")
    url = models.URLField(blank=True,
                          verbose_name="User profile URL",
                          help_text="(Optional) a profile URL etc.")
    notes = models.TextField(blank=True, null=True,
                             verbose_name="Other notes on user")

class RGClass(models.Model):
    "Table for storing information about Robot Garden classes."
    name = models.CharField(max_length=256,
                            verbose_name="Class name")
    sbu = models.BooleanField(verbose_name="Course is an SBU",
                              help_text="Is this class a Safey and Basic Usage class (free with membership)?")
    description = models.TextField()
    audience = models.CharField(verbose_name="Indended audience",
                                help_text="E.g. all / teen / adult / under 10")
    prerequisites = models.CharField(help_text="Required backgrount to take this course")

class Trainig(models.Model):
    "Many to many table of classes users have taken."
    user = models.ForeignKey('RGUser', verbose_name="User ID for entry")
    cls  = models.ForeignKey('RGClass', verbose_name="Class ID for entry")

class Equipment(models.Model):
    "Stores information about a given piece of equipment"
    name = models.CharField(max_length=256,
                            verbose_name="Equipment name")
