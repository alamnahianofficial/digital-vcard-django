from .models import CardProfile

def get_profile():
    profile, created = CardProfile.objects.get_or_create(id=1)
    return profile