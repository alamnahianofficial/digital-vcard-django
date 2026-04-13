from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import CardProfile
from .forms import CardProfileForm
from .utils import get_profile


# the password to login to admin panel
# change this to something secret!
ADMIN_PASSWORD = 'Str@ng3447493'





# ---- PUBLIC CARD PAGE ----
def card_view(request):
    profile = get_profile()

    # build list of social links to show
    # only includes ones that have a value
    socials = []

    if profile.whatsapp:
        socials.append({'label': 'WhatsApp',  'icon': '💬', 'css': 'whatsapp',  'url': 'https://wa.me/' + profile.whatsapp})
    if profile.telegram:
        socials.append({'label': 'Telegram',  'icon': '✈️', 'css': 'telegram',  'url': 'https://t.me/' + profile.telegram.replace('@','')})
    if profile.facebook:
        socials.append({'label': 'Facebook',  'icon': '📘', 'css': 'facebook',  'url': profile.facebook})
    if profile.instagram:
        socials.append({'label': 'Instagram', 'icon': '📸', 'css': 'instagram', 'url': profile.instagram})
    if profile.twitter:
        socials.append({'label': 'Twitter',   'icon': '🐦', 'css': 'twitter',   'url': profile.twitter})
    if profile.tiktok:
        socials.append({'label': 'TikTok',    'icon': '🎵', 'css': 'tiktok',    'url': profile.tiktok})
    if profile.youtube:
        socials.append({'label': 'YouTube',   'icon': '▶️', 'css': 'youtube',   'url': profile.youtube})
    if profile.discord:
        socials.append({'label': 'Discord',   'icon': '🎮', 'css': 'discord',   'url': '#'})
    if profile.linkedin:
        socials.append({'label': 'LinkedIn',  'icon': '💼', 'css': 'linkedin',  'url': profile.linkedin})
    if profile.github:
        socials.append({'label': 'GitHub',    'icon': '💻', 'css': 'github',    'url': profile.github})
    if profile.behance:
        socials.append({'label': 'Behance',   'icon': '🎨', 'css': 'behance',   'url': profile.behance})
    if profile.dribbble:
        socials.append({'label': 'Dribbble',  'icon': '🖌️', 'css': 'dribbble',  'url': profile.dribbble})
    if profile.viber:
        socials.append({'label': 'Viber',     'icon': '📞', 'css': 'viber',     'url': 'viber://chat?number=' + profile.viber})

    context = {
        'profile': profile,
        'socials': socials,
        'skills':  profile.get_skills(),
    }
    return render(request, 'card/card.html', context)


# ---- DOWNLOAD VCF CONTACT FILE ----
def download_vcf(request):
    profile = get_profile()

    # build the vcf text manually
    lines = ['BEGIN:VCARD', 'VERSION:3.0']
    lines.append('FN:' + profile.name)
    if profile.job_title: lines.append('TITLE:' + profile.job_title)
    if profile.phone:     lines.append('TEL;TYPE=CELL:' + profile.phone)
    if profile.email:     lines.append('EMAIL:' + profile.email)
    if profile.website:   lines.append('URL:' + profile.website)
    if profile.location:  lines.append('ADR;TYPE=HOME:;;' + profile.location + ';;;')
    lines.append('END:VCARD')

    vcf_content = '\n'.join(lines)
    filename = (profile.name or 'contact').replace(' ', '_') + '.vcf'

    response = HttpResponse(vcf_content, content_type='text/vcard')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    return response


# ---- ADMIN LOGIN ----
def admin_login(request):
    # if already logged in go to edit page
    if request.session.get('is_admin'):
        return redirect('admin_edit')

    error = ''

    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password == ADMIN_PASSWORD:
            request.session['is_admin'] = True
            return redirect('admin_edit')
        else:
            error = 'Wrong password. Try again.'

    return render(request, 'card/admin_login.html', {'error': error})


def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')


# ---- ADMIN EDIT PANEL ----
def admin_edit(request):
    # check login
    if not request.session.get('is_admin'):
        return redirect('admin_login')

    profile = get_profile()
    saved = False

    if request.method == 'POST':
        # handle photo removal
        if request.POST.get('remove_photo'):
            if profile.photo:
                profile.photo.delete()
            profile.photo = None
            profile.save()
            saved = True
        else:
            form = CardProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                saved = True
            else:
                context = {
                    'form': form,
                    'profile': profile,
                    'saved': False,
                    'tab': request.POST.get('active_tab', 'profile'),
                }
                return render(request, 'card/admin_edit.html', context)

    form = CardProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
        'saved': saved,
        'tab': request.POST.get('active_tab', 'profile') if request.method == 'POST' else 'profile',
    }
    return render(request, 'card/admin_edit.html', context)
