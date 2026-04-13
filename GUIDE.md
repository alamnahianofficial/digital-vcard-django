# Django Digital vCard — Complete Guide

## Project Structure
```
vcard-django/
├── manage.py              ← runs the project
├── requirements.txt       ← packages needed
├── setup.sh               ← one click setup
├── db.sqlite3             ← created automatically (your database)
├── mycard/
│   ├── settings.py        ← project settings
│   ├── urls.py            ← main url routes
│   └── wsgi.py            ← for deployment
└── card/
    ├── models.py          ← database structure
    ├── views.py           ← page logic (change password here!)
    ├── forms.py           ← edit form fields
    ├── urls.py            ← card url routes
    └── templates/card/
        ├── card.html      ← public card page
        ├── admin_login.html
        └── admin_edit.html
```

---

## Step 1 — Change Your Password

Open `card/views.py` and find this line near the top:

```python
ADMIN_PASSWORD = 'admin123'
```

Change it to your own password. Save the file.

---

## Step 2 — Run Locally (Test on Your Computer)

You need Python installed. Check by running: `python --version`

```bash
# install packages
pip install -r requirements.txt

# setup database
python manage.py makemigrations card
python manage.py migrate

# run the server
python manage.py runserver
```

Now open your browser and go to:
- Card page: http://127.0.0.1:8000
- Edit panel: http://127.0.0.1:8000/admin-edit/

---

## Step 3 — Deploy to PythonAnywhere (Free Forever)

### A) Create Account
1. Go to https://www.pythonanywhere.com
2. Sign up free — use your name as username
3. Your site will be at `yourname.pythonanywhere.com`

### B) Upload Your Files
1. Go to **Files** tab in PythonAnywhere
2. Create a folder called `vcard`
3. Upload all your project files into it
   OR use the console to clone from GitHub

### C) Set Up via Console
1. Click **Consoles** tab → **Bash** → New console
2. Run these commands one by one:

```bash
cd vcard
pip install -r requirements.txt --user
python manage.py makemigrations card
python manage.py migrate
python manage.py collectstatic --noinput
```

### D) Create Web App
1. Go to **Web** tab → **Add a new web app**
2. Choose **Manual configuration**
3. Choose **Python 3.10**
4. Click Next

### E) Configure the Web App
In the Web tab, find these sections and fill them in:

**Source code:**
```
/home/yourusername/vcard
```

**WSGI configuration file** — click the link and replace everything with:
```python
import sys
import os

path = '/home/yourusername/vcard'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mycard.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Static files:**
- URL: `/static/`
- Directory: `/home/yourusername/vcard/staticfiles`

**Media files:**
- URL: `/media/`
- Directory: `/home/yourusername/vcard/media`

### F) Update Settings for Live Site
Open `mycard/settings.py` and change:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
```

### G) Reload
Click the green **Reload** button in the Web tab.

Your site is live at: `https://yourusername.pythonanywhere.com`

---

## How to Edit Your Card

1. Go to `https://yourusername.pythonanywhere.com/admin-edit/`
2. Enter your password
3. Edit Profile / Contact / Social / Skills tabs
4. Click Save in each tab
5. Changes show immediately on the public card

No re-uploading needed. Ever.

---

## How to Change Password Later

Open `card/views.py`, change `ADMIN_PASSWORD`, then:
- On PythonAnywhere: go to Web tab → click Reload

---

## Pages
| URL | What it is |
|-----|-----------|
| `/` | Your public card |
| `/admin-login/` | Login page |
| `/admin-edit/` | Edit your card |
| `/admin-logout/` | Logout |
| `/download-vcf/` | Download contact file |
