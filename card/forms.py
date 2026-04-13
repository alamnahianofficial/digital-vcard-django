from django import forms
from .models import CardProfile


# form for editing the card profile
# django generates HTML inputs from this automatically
class CardProfileForm(forms.ModelForm):

    class Meta:
        model = CardProfile
        fields = [
            'name', 'job_title', 'location', 'about', 'photo',
            'phone', 'email', 'website',
            'whatsapp', 'telegram', 'viber',
            'facebook', 'instagram', 'twitter', 'tiktok', 'youtube', 'discord',
            'linkedin', 'github', 'behance', 'dribbble',
            'skills_text',
        ]
        widgets = {
            'name':       forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'job_title':  forms.TextInput(attrs={'placeholder': 'e.g. Web Developer & Designer'}),
            'location':   forms.TextInput(attrs={'placeholder': 'e.g. Dhaka, Bangladesh'}),
            'about':      forms.Textarea(attrs={'placeholder': 'Short bio about yourself...', 'rows': 4}),
            'phone':      forms.TextInput(attrs={'placeholder': '+880 1XXX-XXXXXX'}),
            'email':      forms.EmailInput(attrs={'placeholder': 'you@email.com'}),
            'website':    forms.URLInput(attrs={'placeholder': 'https://yourwebsite.com'}),
            'whatsapp':   forms.TextInput(attrs={'placeholder': '8801XXXXXXXXX (digits only with country code)'}),
            'telegram':   forms.TextInput(attrs={'placeholder': '@yourusername'}),
            'viber':      forms.TextInput(attrs={'placeholder': '8801XXXXXXXXX'}),
            'facebook':   forms.URLInput(attrs={'placeholder': 'https://facebook.com/yourname'}),
            'instagram':  forms.URLInput(attrs={'placeholder': 'https://instagram.com/yourname'}),
            'twitter':    forms.URLInput(attrs={'placeholder': 'https://twitter.com/yourname'}),
            'tiktok':     forms.URLInput(attrs={'placeholder': 'https://tiktok.com/@yourname'}),
            'youtube':    forms.URLInput(attrs={'placeholder': 'https://youtube.com/@channel'}),
            'discord':    forms.TextInput(attrs={'placeholder': 'username#1234'}),
            'linkedin':   forms.URLInput(attrs={'placeholder': 'https://linkedin.com/in/yourname'}),
            'github':     forms.URLInput(attrs={'placeholder': 'https://github.com/yourname'}),
            'behance':    forms.URLInput(attrs={'placeholder': 'https://behance.net/yourname'}),
            'dribbble':   forms.URLInput(attrs={'placeholder': 'https://dribbble.com/yourname'}),
            'skills_text':forms.TextInput(attrs={'placeholder': 'Python, Django, HTML, CSS, JavaScript'}),
        }
        labels = {
            'name':       'Full Name',
            'job_title':  'Job Title',
            'location':   'Location',
            'about':      'About / Bio',
            'photo':      'Profile Photo',
            'skills_text':'Skills (comma separated)',
            'whatsapp':   'WhatsApp Number',
            'telegram':   'Telegram Username',
            'viber':      'Viber Number',
        }
