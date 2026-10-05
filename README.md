# ⚡ SpeedForce — Home Services Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/Tailwind%20CSS-CDN-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
</p>

<p align="center">
  <strong>A Django-based home-services website prototype focused on cleaning, cooking, plumbing, electrical, babysitting, and elderly-care services.</strong>
</p>

---

## 🎯 What This Project Offers

**SpeedForce** is a Django web project designed as a modern home-services marketplace/interface.

The current repository focuses primarily on the **frontend experience and service presentation**, with Django providing the page routing and template system.

The UI presents services such as:

- 🧹 Home and kitchen cleaning
- 🍳 Cooking assistance
- 🔧 Plumbing
- ⚡ Electrical services
- 👶 Babysitting
- 👵 Elderly care

The project also includes designed sections for:

- 💰 Pricing
- ⭐ Customer testimonials
- ❓ Frequently asked questions
- 👥 Team members
- 📞 Contact support
- 📱 Responsive navigation
- 📧 Newsletter subscription UI

> **Current implementation status:** the repository currently contains only two application views — Home and Services. User authentication, real booking, payment processing, database-backed service management, and dashboards are not yet implemented in the backend.

---

## ✨ Highlighted Features

<table>
<tr>
<td width="50%">

### 🏠 Home Page

- Full-screen hero section
- Multiple promotional slides
- Automatic carousel rotation
- Previous/next controls
- Slide indicator dots
- Responsive hero layout
- Service call-to-action buttons

</td>

<td width="50%">

### 🧹 Service Catalogue

- Service categories
- Service cards
- Service descriptions
- Pricing
- Category filtering
- Price sorting
- Popularity sorting
- Responsive card layout

</td>
</tr>

<tr>
<td>

### 📱 Responsive Navigation

- Desktop navbar
- Mobile navigation menu
- Animated menu opening
- Mobile menu overlay behavior
- Keyboard `Escape` support
- Touch gesture handling

</td>

<td>

### 🎨 Modern UI

- Dark interface
- Blue accent system
- Tailwind utility classes
- Responsive layouts
- Smooth scrolling
- Hover transitions
- Backdrop blur effects

</td>
</tr>

<tr>
<td>

### 💰 Pricing Presentation

Current demo plans include:

- Basic — ₹299
- Standard — ₹699
- Premium — ₹1999

</td>

<td>

### 📣 Marketing Sections

- Customer testimonials
- FAQ
- Team section
- Contact CTA
- Newsletter interface
- Company information
- Legal navigation placeholders

</td>
</tr>
</table>

---

## 🧠 How It Works

The current architecture is deliberately simple:

```text
                    ┌───────────────────────┐
                    │      Web Browser      │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │        Django         │
                    │     URL Routing       │
                    └───────────┬───────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
              ┌───────────┐          ┌────────────┐
              │   Home    │          │  Services  │
              │   View    │          │    View    │
              └─────┬─────┘          └──────┬─────┘
                    │                       │
                    └───────────┬───────────┘
                                ▼
                    ┌───────────────────────┐
                    │      Templates        │
                    │ Django + HTML + JS    │
                    └───────────────────────┘
```

The application currently maps:

```text
/           → Main.views.index
/services/  → Main.views.services
/admin/     → Django Admin
```

---

## 🛠️ Software & Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Application language |
| 🟢 Django 5.2 | Web framework |
| 🗄️ SQLite | Default database |
| 🎨 Tailwind CSS | UI styling |
| 🌐 HTML5 | Page structure |
| ⚡ JavaScript | Interactive UI |
| 🧩 Django Templates | Template rendering |
| 🔐 Django Auth | Built-in authentication infrastructure |
| 🚀 ASGI | Async deployment interface |
| 🏗️ WSGI | Traditional deployment interface |

Tailwind is currently loaded through the CDN:

```html
<script src="https://cdn.tailwindcss.com"></script>
```

For production, compiling Tailwind into the project's static assets would be preferable.

---

## 💻 System Requirements

### Minimum

| Component | Requirement |
|---|---|
| OS | Windows / Linux / macOS |
| Python | 3.x |
| RAM | 4 GB |
| Storage | ~500 MB |
| Browser | Modern Chrome, Edge or Firefox |

### Recommended

| Component | Recommendation |
|---|---|
| RAM | 8 GB+ |
| Python | Recent Python 3 release |
| Browser | Latest Chrome / Edge |
| Database | PostgreSQL for production |
| Node.js | Required when replacing Tailwind CDN with a build pipeline |

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yasirkhan251/speedforce.git
cd speedforce
```

---

### 2️⃣ Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Django

The repository currently does not include a root `requirements.txt`.

Install Django with:

```bash
pip install django
```

Or specify the project's current major/minor version:

```bash
pip install "Django>=5.2,<5.3"
```

---

## 🗄️ Database Setup

The project uses SQLite:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Run migrations:

```bash
python manage.py migrate
```

Create an admin account:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the administrator credentials.

---

## ⚙️ Configuration

The Django project is located in:

```text
SpeedForce/
```

Important settings include:

```text
SpeedForce/settings.py
SpeedForce/urls.py
SpeedForce/asgi.py
SpeedForce/wsgi.py
```

The main application is:

```text
Main/
```

The project registers it through:

```python
INSTALLED_APPS += ['Main']
```

Templates are configured using:

```python
DIRS = [os.path.join(BASE_DIR, 'templates')]
```

---

## ▶️ How to Run

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

For LAN testing, the project currently allows:

```text
192.168.0.6
localhost
127.0.0.1
```

The exact address used depends on the machine's network configuration.

---

## 🎮 How to Use

### 🏠 Home Page

Visit:

```text
/
```

The home page contains a large hero carousel featuring different service categories.

The current slides promote:

```text
Professional Maid Services
Expert Plumbers
Professional Electricians
```

The carousel automatically changes every **5 seconds** and can also be controlled manually.

---

### 🧹 Services Page

Visit:

```text
/services/
```

The service page displays categories:

```text
A
B
C
```

with example offerings including:

| Service | Price |
|---|---:|
| A1 — Kitchen Cleaning | ₹299 |
| A2 — Full Home Sweep & Mop | ₹499 |
| B1 — Daily Cooking Help | ₹699 |
| B2 — Meal Prep + Grocery Assist | ₹999 |
| C1 — Babysitting (4 hrs) | ₹1299 |
| C2 — Elderly Care (4 hrs) | ₹1699 |

The frontend includes sorting options:

```text
Most Popular
Price: Low to High
Price: High to Low
```

---

## 📱 Responsive Mobile Menu

The shared `base.html` template contains a responsive navigation system.

Desktop navigation includes:

```text
Home
Services
Pricing
Contact
Login
Sign up
```

On smaller screens, the navigation switches to a mobile menu.

The JavaScript implementation supports:

- Open/close animation
- Menu button state
- `aria-expanded`
- Escape-key closing
- Link-based closing
- Touch swipe-to-close behavior

---

## 🎨 Template Structure

The project uses Django template inheritance.

The main base template is:

```text
templates/base.html
```

Child pages extend it:

```django
{% extends "base.html" %}
```

and inject content with:

```django
{% block content %}
...
{% endblock %}
```

The current primary pages are:

```text
templates/
├── base.html
├── login.html
├── signup.html
└── Main/
    ├── index.html
    └── service.html
```

---

## 🧩 Application Structure

The project contains a single custom Django application:

```text
Main
```

Its current backend implementation is intentionally small.

### `Main/views.py`

```python
def index(req):
    return render(req, 'Main/index.html')

def services(req):
    return render(req, 'Main/service.html')
```

### `Main/urls.py`

```python
urlpatterns = [
    path('', index, name='index'),
    path('services/', services, name='services'),
]
```

---

## 🗃️ Data Layer

The current `Main/models.py` does not define application-specific database models.

```python
from django.db import models
```

Therefore, the current services, prices, testimonials, team entries, FAQ content, and other marketing information are primarily **defined directly in the templates** rather than retrieved from a database.

---

## 📊 Current Project Status

| Area | Status |
|---|---|
| Django project | ✅ |
| Home page | ✅ |
| Services page | ✅ |
| Responsive navbar | ✅ |
| Hero carousel | ✅ |
| Service filtering UI | ✅ |
| Service sorting UI | ✅ |
| Pricing UI | ✅ |
| Testimonials UI | ✅ |
| FAQ UI | ✅ |
| Contact CTA | ✅ |
| Newsletter UI | ✅ |
| Django Admin | ✅ Built-in |
| Custom models | ⏳ Not implemented |
| User authentication | ⏳ UI placeholders only |
| Real service booking | ⏳ Not implemented |
| Payment gateway | ⏳ Not implemented |
| Customer dashboard | ⏳ Not implemented |
| Provider dashboard | ⏳ Not implemented |
| Database-backed services | ⏳ Not implemented |
| Notifications | ⏳ Not implemented |

---

## 📸 Screenshots

No dedicated screenshot collection was identified in the repository.

Recommended documentation structure:

```text
docs/
└── images/
    ├── home.png
    ├── services.png
    ├── pricing.png
    └── mobile-menu.png
```

Then add images to the README using:

```html
<p align="center">
  <img src="docs/images/home.png"
       width="90%"
       alt="SpeedForce Home Page">
</p>
```

---

## 🎞️ GIF Demonstrations

No GIF demonstrations are currently included.

Recommended examples:

```text
docs/demo/
├── hero-carousel.gif
├── mobile-navigation.gif
├── service-filter.gif
└── service-sort.gif
```

Example README usage:

```markdown
![SpeedForce Service Filtering](docs/demo/service-filter.gif)
```

---

## 🎥 Video Demonstration

No dedicated project demo video was identified in the repository.

Recommended format:

```html
<p align="center">
  <a href="YOUR_YOUTUBE_VIDEO_URL">
    <img src="https://img.youtube.com/vi/YOUR_VIDEO_ID/maxresdefault.jpg"
         alt="SpeedForce Video Demo"
         width="85%">
  </a>
</p>
```

---

## 📁 Project Structure

```text
speedforce/
│
├── manage.py
├── db.sqlite3
│
├── SpeedForce/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── Main/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
└── templates/
    ├── base.html
    ├── login.html
    ├── signup.html
    │
    └── Main/
        ├── index.html
        └── service.html
```

---

## ⚠️ Limitations & Development Notes

The repository is currently closer to a **frontend-oriented Django prototype** than a complete service marketplace.

Important limitations:

- No application-specific Django models
- Service data is hard-coded in templates
- Login and signup pages are present, but no corresponding custom authentication workflow is implemented in `Main`
- Service "Book Now" buttons do not currently connect to a backend booking system
- Pricing buttons are currently UI elements
- Newsletter form has no submission backend
- Contact section is primarily a mail link
- Testimonials are static content
- Team information is static content
- Pagination is currently a static visual component
- Several navbar links point back to the home page as placeholders
- Tailwind is loaded from CDN
- No `requirements.txt` is currently included
- Development settings are committed directly into the repository
- Generated `__pycache__` directories are present

---

## 🔐 Security Notes

The current `SpeedForce/settings.py` contains:

```python
DEBUG = True
```

and a Django secret key directly in source code.

For development this is common in generated Django projects, but before deployment:

### Move the secret key to an environment variable

```python
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
```

### Disable debug

```python
DEBUG = False
```

### Restrict allowed hosts

```python
ALLOWED_HOSTS = [
    "yourdomain.com",
]
```

### Add production security settings

For example:

```text
SECURE_SSL_REDIRECT
SESSION_COOKIE_SECURE
CSRF_COOKIE_SECURE
SECURE_HSTS_SECONDS
SECURE_CONTENT_TYPE_NOSNIFF
```

---

## 🔮 Future Improvements / Roadmap

### 🚀 Phase 1 — Backend Foundation

- Create service models
- Create provider/maid models
- Store pricing in database
- Add service categories
- Add availability management
- Add database-backed testimonials
- Add contact form model

### 👤 Phase 2 — User System

- User registration
- Login/logout
- Password reset
- Customer profile
- Customer dashboard
- Booking history

### 📅 Phase 3 — Booking System

- Service booking
- Date/time selection
- Professional selection
- Availability checking
- Booking confirmation
- Booking cancellation
- Booking status tracking

### 💳 Phase 4 — Payments

- Razorpay / Stripe / PhonePe integration
- Payment verification
- Transaction history
- Refund support
- Digital invoices

### 👨‍🔧 Phase 5 — Service Provider Platform

- Provider registration
- Provider dashboard
- Job assignments
- Availability calendar
- Earnings tracking
- Customer ratings
- Service completion workflow

### 📍 Phase 6 — Location

- Address management
- Google Maps
- Service-area validation
- Distance calculation
- Provider proximity matching

### 📱 Phase 7 — Platform Expansion

- REST API
- React frontend
- Mobile application
- Push notifications
- WhatsApp notifications
- Email notifications
- Admin analytics
- Revenue dashboard

### ☁️ Phase 8 — Production Deployment

- PostgreSQL
- Docker
- Gunicorn
- Nginx
- Cloud storage
- CI/CD
- Logging
- Monitoring
- Automated backups

---

## 👨‍💻 Author

<p align="center">
  <strong>Yasir Khan</strong><br>
  Python Developer • Django Developer • Web Developer • AI/ML Enthusiast
</p>

<p align="center">
  <a href="https://github.com/yasirkhan251">
    <img src="https://img.shields.io/badge/GitHub-yasirkhan251-181717?style=for-the-badge&logo=github">
  </a>
</p>

---

## 📄 License

No explicit `LICENSE` file was identified in the repository.

Until a license is added, the project should be treated as **all rights reserved** by the repository owner.

---

<p align="center">
  ⚡ <strong>SpeedForce</strong> — Fast, Reliable & Professional Home Services
</p>
