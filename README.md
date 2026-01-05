# Text Upload Django Application

A simple Django application for uploading long text passages that are displayed and managed in the Django admin panel. Built with Django, HTML, CSS, and vanilla JavaScript.

## Features
- 📝 Clean and modern UI for text uploads
- ✅ Character count in real-time
- 🎨 Beautiful gradient styling with responsive design
- 📊 View all submissions in a grid layout
- 🔐 Secure admin panel to manage submissions
- 📱 Fully responsive on mobile and desktop

## Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

## Setup & Run

### 1. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

### 2. Install requirements:
```bash
pip install -r requirements.txt
```

### 3. Apply migrations:
```bash
python manage.py migrate
```

### 4. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

### 5. Run the development server:
```bash
python manage.py runserver
```

### 6. Access the application:
- **Upload page**: http://127.0.0.1:8000/
- **View all submissions**: http://127.0.0.1:8000/submissions/
- **Admin panel**: http://127.0.0.1:8000/admin/ ===>
  - Default credentials:  UserNAme : admin , Password : Manas@754245

## Project Structure
- `contact/` - Main app containing models, forms, and views
- `templates/contact/` - HTML templates
- `mysite/` - Project configuration
- `manage.py` - Django management script

## Models
### TextUpload
- `title` - Title of the text submission
- `content` - The actual text content (any length)
- `created_at` - Automatic timestamp
- `updated_at` - Automatic timestamp on changes

## Admin Panel Features
- View all text submissions in a list
- Search by title and content
- Filter by creation/update date
- Character count display
- Edit and delete submissions
- Timestamps are read-only

## Technologies Used
- Django 5.2.8
- SQLite3
- HTML5
- CSS3 (Gradients, Flexbox, Grid)
- Vanilla JavaScript (Character counter)

## Notes
- All uploaded texts are stored in SQLite database
- No external dependencies for styling (pure CSS)
- JavaScript is minimal and vanilla (no frameworks)
- The application is ready for production deployment with proper configuration
