# Resident Evil Gunshop

A Django web application cataloging firearms featured in Resident Evil games and their real-life counterparts.

---

## 📂 Project Structure

- **core/** — universal views like Home and About
- **guns/** — manages Gun models, CRUD, categories
- **reviews/** — handles reviews for guns
- **media/** — uploaded images
- **static/** — static files (CSS, images, icons)
- **templates/** — HTML templates using Django template inheritance
- **residentevil_gunshop/** — project settings and URLs

---

## 🛠️ Technologies

- Python 3.12  
- Django 6.x  
- PostgreSQL  
- Bootstrap 5.3 for styling  
- Pillow (for image uploads)

---

## 💾 Setup Instructions

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd residentevil_gunshop
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## 🗄️ Database Setup (PostgreSQL Required)

This project uses PostgreSQL as required by the assignment.

1. Make sure PostgreSQL is installed and running.
2. Create a database:
   ```bash
   createdb residentevil_gunshop
   ```
3. If required, update the DATABASE settings in settings.py to match your PostgreSQL username and password (username/password is postgres/postgres by default).


4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create a superuser** (Optional)

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

7. **Open http://127.0.0.1:8000/ in your browser.**


8. **Add Guns/Categories to your database through their respective pages**

***Note: I recommend adding your categories first, so that they may appear when adding/editing a gun. After this you can also freely edit and delete your guns/categories.***
## 🔹 Features

- Full CRUD functionality for **Guns**, **Reviews** and **Categories**
- Categorized guns with **many-to-many relationships**
- Search guns by **name** or **game**
- Responsive layout using **Bootstrap 5**
- **Images** for guns (a ready-to-go sample of images will be located in the **media/guns** directory, ready for use.)
- Custom **404 page**
- Navigation with consistent **header/footer**
- **Edit/Delete** functionality for guns and reviews

---

## 📋 Notes

- All environment variables and credentials required for local testing are included in the project defaults; no additional configuration is needed for local testing.
- Gun images can be uploaded via the **admin panel** or the **Gun edit/add page**.
- The site is fully functional without authentication, as per project requirements.

---

## ⚡ License / Disclaimer

This project is for **educational purposes**.  
No copyrighted material has been copied, and all code is original.