from django.db import models


# this model stores everything about the card
# one row in the database = one person's card info
class CardProfile(models.Model):

    # basic info
    name      = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=150, blank=True)
    location  = models.CharField(max_length=150, blank=True)
    about     = models.TextField(blank=True)
    photo     = models.ImageField(upload_to='photos/', blank=True, null=True)

    # contact
    phone   = models.CharField(max_length=30,  blank=True)
    email   = models.EmailField(max_length=100, blank=True)
    website = models.URLField(max_length=200,   blank=True)

    # messaging
    whatsapp = models.CharField(max_length=20,  blank=True)
    telegram = models.CharField(max_length=50,  blank=True)
    viber    = models.CharField(max_length=20,  blank=True)

    # social networks
    facebook  = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    twitter   = models.URLField(max_length=200, blank=True)
    tiktok    = models.URLField(max_length=200, blank=True)
    youtube   = models.URLField(max_length=200, blank=True)
    discord   = models.CharField(max_length=50, blank=True)

    # professional
    linkedin = models.URLField(max_length=200, blank=True)
    github   = models.URLField(max_length=200, blank=True)
    behance  = models.URLField(max_length=200, blank=True)
    dribbble = models.URLField(max_length=200, blank=True)

    # skills stored as comma separated text
    # e.g. "Python,Django,HTML,CSS"
    skills_text = models.TextField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def get_skills(self):
        # split skills by comma and clean whitespace
        if not self.skills_text:
            return []
        return [s.strip() for s in self.skills_text.split(',') if s.strip()]

    def get_initials(self):
        # make initials from name like "Delwar Hossain" = "DH"
        words = self.name.strip().split()
        initials = ''
        for word in words[:2]:
            if word:
                initials += word[0].upper()
        return initials or '?'

    def __str__(self):
        return self.name or 'My Card'

    class Meta:
        verbose_name = 'Card Profile'
