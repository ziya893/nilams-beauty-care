# Nilam's Beauty Care — Salon Website

A Django website for **Nilam's Beauty Care**, a salon in Bapunagar, Ahmedabad.

Includes:
- Home, Services, About, Contact pages
- Services organised by category: Hair Treatment, Face Treatment, Skin Care, Makeup, Bridal Packages, Spa & Body
- Online appointment booking form (saved to the database + visible in Django Admin)
- Click-to-call and WhatsApp buttons using your business number
- Elegant wine / gold / ivory colour theme
- Mobile-responsive design

---

## 1. Run it on your computer (VS Code)

**Requirements:** Python 3.10+ installed on your computer.

1. Open this folder in VS Code.
2. Open a terminal in VS Code (`Terminal → New Terminal`) and create a virtual environment:

   ```bash
   python -m venv venv
   ```

   Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database (this also loads the default services list):

   ```bash
   python manage.py migrate
   ```

5. Create an admin login (so you/your mom can manage services and appointments):

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set a username and password.

6. Start the website:

   ```bash
   python manage.py runserver
   ```

7. Open your browser at **http://127.0.0.1:8000/** to see the website.
   Open **http://127.0.0.1:8000/admin/** and log in to manage services and see appointment bookings.

---

## 2. Managing the website content

Everything (services, prices, appointments) is editable from the Django Admin at `/admin/`:

- **Services** → add/edit/remove treatments, prices, and categories. Tick "is_featured" to show a service on the homepage. Untick "is_active" to hide a service without deleting it.
- **Appointments** → see every booking request customers submit, and update its status (Pending / Confirmed / Completed / Cancelled).

To change the salon's phone number, WhatsApp number, or address, edit these lines near the bottom of `nilams_beauty_care/settings.py`:

```python
SALON_NAME = "Nilam's Beauty Care"
SALON_ADDRESS = "Vrundavan Complex, B/9, Hirawadi Road, Bapunagar, Ahmedabad, 382345"
SALON_PHONE = "+91 98240 83685"
SALON_PHONE_RAW = "919824083685"
SALON_WHATSAPP = "919824083685"
```

---

## 3. Before you deploy it live on the internet

1. Open `nilams_beauty_care/settings.py` and:
   - Change `SECRET_KEY` to a new random value. Generate one with:
     ```bash
     python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
     ```
   - Set `DEBUG = False`
   - Set `ALLOWED_HOSTS` to your actual domain, e.g. `ALLOWED_HOSTS = ['nilamsbeautycare.com', 'www.nilamsbeautycare.com']`

   Tip: instead of editing these directly, you can set them as environment variables on your hosting provider:
   `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`.

2. Collect static files (CSS) for production:
   ```bash
   python manage.py collectstatic
   ```

3. Run database migrations on the server:
   ```bash
   python manage.py migrate
   ```

## 4. Deploying (recommended: Render, Railway, or PythonAnywhere)

These platforms offer free/cheap tiers and are beginner-friendly for Django:

- **Render.com** — connect your GitHub repo, set the start command to:
  ```
  gunicorn nilams_beauty_care.wsgi:application
  ```
- **Railway.app** — similar process, auto-detects Django + the `Procfile` below.
- **PythonAnywhere** — good free option, upload the project via their web interface.

A `Procfile` is included for platforms that use it:
```
web: gunicorn nilams_beauty_care.wsgi:application
```

Whichever host you choose, remember to set the environment variables from step 3 above
(`DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, and your domain in `ALLOWED_HOSTS`).

---

## Project structure

```
nilams_beauty_care/
├── manage.py
├── requirements.txt
├── nilams_beauty_care/      # project settings & URLs
└── salon/                   # the app: models, views, templates, static CSS
    ├── models.py            # Service, Appointment
    ├── views.py
    ├── forms.py
    ├── admin.py
    ├── templates/salon/
    └── static/salon/css/style.css
```

---

Made with care for Nilam's Beauty Care 💐
